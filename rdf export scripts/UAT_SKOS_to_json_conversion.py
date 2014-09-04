# coding: utf-8

from datetime import datetime
import cStringIO
import rdflib
import json

#assign this variable to the name of the exported UAT SKOS-RDF file, found in the same location as this script.
rdf = "export_skos-xl_04092014115052.rdf"

print "Reading the SKOS file... this may take a few seconds."
#reads the SKOS-RDF file into a RDFlib graph for use in this script
g = rdflib.Graph()
result = g.parse((rdf).encode('utf8'))

#defines certain properties within the SKOS-RDF file
litForm = rdflib.term.URIRef('http://www.w3.org/2008/05/skos-xl#literalForm')
prefLabel = rdflib.term.URIRef('http://www.w3.org/2008/05/skos-xl#prefLabel')
narrower = rdflib.term.URIRef('http://www.w3.org/2004/02/skos/core#narrower')
TopConcept = rdflib.term.URIRef('http://www.w3.org/2004/02/skos/core#hasTopConcept')
broader = rdflib.term.URIRef('http://www.w3.org/2004/02/skos/core#broader')
Concept = rdflib.term.URIRef('http://www.w3.org/2004/02/skos/core#Concept')

#a list of all top concepts
alltopconcepts = [bv for bv in g.objects(predicate=TopConcept)]

#a list of all concepts
allconcepts = [gm for gm in g.subjects(rdflib.RDF.type, Concept)]

#a function to get a list of all narrower terms under a term
def getnarrowerterms(term):
    terminal = rdflib.term.URIRef(term)
    narrowerterms = {}
    try:
        for nts in g.objects(subject=terminal, predicate=narrower):
            try:
                narrowerterms[terminal].append(nts)
            except KeyError:
                narrowerterms[terminal] = [nts]
        return narrowerterms[terminal]
    except KeyError:
        pass   

def getbroaderterms(term):
    terminal = rdflib.term.URIRef(term)
    broaderterms = {}
    try:
        for bts in g.objects(subject=terminal, predicate=broader):
            try:
                broaderterms[terminal].append(bts)
            except KeyError:
                broaderterms[terminal] = [bts]
        return broaderterms[terminal]
    except KeyError:
        pass 

#a function to return the human readable form of the prefered version of a term.
def lit(term):
    d = rdflib.term.URIRef(term)
    for prefterm in g.objects(subject=d, predicate=prefLabel):
        for litterm in g.objects(subject=prefterm, predicate=litForm):
            return litterm

#Alex's Script Begins
flat_j = {}

for t in allconcepts:
    litt = unicode(lit(t))
    p = getbroaderterms(t)
    c = getnarrowerterms(t)
    pl = []
    rcl = []
    if p == None:
        pl = ["astro_thes"]
    else:
        for x in p:
            y = unicode(lit(x))
            pl.append(y)
    if c == None:
        pass
    else:
        for x in c:
            y = unicode(lit(x))
            rcl.append(y)
 
    flat_j[litt] = {

        "parents" : pl,
        "children" : [],
    "real_children": rcl,
    }

def recurse_traverse(info_dict, name_of_dict, flat_j):
    # step one: add all entries from flat_j to children dict that have parents that equal the key name from the dict
    for f in flat_j:
        if name_of_dict.encode("utf-8") in flat_j[f]["parents"]:
            info_dict["children"].append({"name": f, "children":[]})
    # step two: now that the entries are added, repeat the process on each of them. A full path to that 
    #child within the original "info_dict" becomes the new info_dict. If there were no entries added
    #to children, this will throw a key error, so we stop recursing on this branch
    if len(info_dict["children"])>0:
        #print info_dict["children"]
        #sort children (in info_dict[])
        for i, child_dict in enumerate(info_dict["children"]):  
            recurse_traverse(info_dict["children"][i], child_dict["name"], flat_j)
    else :
        del info_dict["children"]

astro_thes = {"children":[], "alternate": []}

print "Organizing the terms, almost finished."
print "You can ignore the UnicodeWarning if you get one..."
recurse_traverse(astro_thes, "astro_thes", flat_j)

#first, making a list of all unique label names
final_list =[]

labels = list(set([f['label'] for f in final_list]))

new_list = []
#now combining any dudes with multiple parents into one entry
dupes = []
for l in labels:
    id_ = l
    matches = []
    for f in final_list:
        if f['label']==id_:
            matches.append(f)
    if len(matches) >1:

        parents = []
        children = []
        weight = []
        for m in matches:
            parents.append(m['parents'])
            # just in case different instances of terms have diff children arrays (unlikely???)
            children.extend(m['children'])
            weight.append(m['weight'])
        # always going to choose the highest weight (the least far into the heirarchy)
        weight = max(weight)    
        children = list(set(children))
        # adding single entry back into final_list
        new_list.append({'label': m['label'], 'value': m['value'], 'parents': parents, 'children': children, 'weight': m['weight']})

    else:
        # just put the one match back in final_list
        # adding brackets around parents
        new_list.append({'label': matches[0]['label'], 'value': matches[0]['value'], 'parents': [matches[0]['parents']], 'children':  matches[0]['children'], 'weight':  matches[0]['weight']})

final_list = new_list

js_file = open("uat.json", "wb")
js_file.write(json.dumps(astro_thes))
js_file.close()

print "Finished.  See uat.json"
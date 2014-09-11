# coding: utf-8

from datetime import datetime
import cStringIO
import rdflib
import json

#assign this variable to the name of the exported UAT SKOS-RDF file, found in the same location as this script.
rdf = "export_skos-xl_11092014124732.rdf"

print "Reading the SKOS file... this may take a few seconds."
#reads the SKOS-RDF file into a RDFlib graph for use in this script
g = rdflib.Graph()
result = g.parse((rdf).encode('utf8'))

#defines certain properties within the SKOS-RDF file
litForm = rdflib.term.URIRef('http://www.w3.org/2008/05/skos-xl#literalForm')
prefLabel = rdflib.term.URIRef('http://www.w3.org/2008/05/skos-xl#prefLabel')
#narrower = rdflib.term.URIRef('http://www.w3.org/2004/02/skos/core#narrower')
broader = rdflib.term.URIRef('http://www.w3.org/2004/02/skos/core#broader')
Concept = rdflib.term.URIRef('http://www.w3.org/2004/02/skos/core#Concept')

#a list of all concepts
allconcepts = [gm for gm in g.subjects(rdflib.RDF.type, Concept)]

#find all terms that have the given term listed as a broader term, so they are therefore narrower terms
def getnarrowerterms(term):
    narrowerterms = {}
    terminal = rdflib.term.URIRef(term)
    try:
        for nts in g.subjects(predicate=broader, object=terminal):
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

print "Creating the json..."
#Alex's Script
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
    #step one: add all entries from flat_j to children dict that have parents that equal the key name from the dict
    for f in flat_j:
        if name_of_dict.encode("utf-8") in flat_j[f]["parents"]:
            info_dict["children"].append({"name": f, "children":[]})
    #step two: now that the entries are added, repeat the process on each of them. A full path to that 
    #child within the original "info_dict" becomes the new info_dict. If there were no entries added
    #to children, this will throw a key error, so we stop recursing on this branch
    if len(info_dict["children"])>0:
        children_dict = info_dict["children"]
        children_dict.sort(); #sorts child terms alphabetically
        for i, child_dict in enumerate(children_dict):  
            recurse_traverse(children_dict[i], child_dict["name"], flat_j)
    else:
        del info_dict["children"]

astro_thes = {"children":[]}

print "You can ignore the UnicodeWarning if you get one..."
recurse_traverse(astro_thes, "astro_thes", flat_j)

js_file = open("uat.json", "wb")
js_file.write(json.dumps(astro_thes))
js_file.close()

print "Finished!  See uat.json."
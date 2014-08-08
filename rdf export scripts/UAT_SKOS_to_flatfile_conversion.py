# coding: utf-8

from datetime import datetime
import cStringIO
import rdflib
import pandas as pd

#assign this variable to the name of the exported UAT SKOS-RDF file, found in the same location as this script.
rdf = "export_skos-xl_07052014030250.rdf"

print "Reading the SKOS file...this may take a few seconds."

#reads the SKOS-RDF file into a RDFlib graph for use in this script
g = rdflib.Graph()
result = g.parse((rdf).encode('utf8'))

#defines certain properties within the SKOS-RDF file
litForm = rdflib.term.URIRef('http://www.w3.org/2008/05/skos-xl#literalForm')
narrower = rdflib.term.URIRef('http://www.w3.org/2004/02/skos/core#narrower')
TopConcept = rdflib.term.URIRef('http://www.w3.org/2004/02/skos/core#hasTopConcept')

#a list of all top concepts
alltopconcepts = [bv for bv in g.objects(predicate=TopConcept)]

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

#a function to return the human readable form of a term.
def lit(term):
    d = rdflib.term.URIRef(term)
    for litterm in g.objects(subject=d, predicate=litForm):
        return litterm

#a function to travel all the way down each path in the thesarus and return this information into a list.
def descend(term, parents, out_list):
    lvln = getnarrowerterms(term)
    if lvln != None: #if there are narrower terms...
        for z in lvln:
            children = parents[:]
            w = lit(z)
            children.append(lit(term))
            if children not in out_list:
                out_list.append(children)
            descend(z, children, GLOBAL_OUT_LIST)
    else: #if there are no more narrower terms...
        children = parents[:]
        children.append(lit(term))
        if children not in out_list:
            out_list.append(children)


print "Organizing the terms, almost finished."

#runs the functions across all terms and outputs to pandas dataframe.
timestamp = datetime.now().strftime("_%Y_%m%d_%H%M%S")
GLOBAL_OUT_LIST = []
out_list = []
for term in alltopconcepts:
    descend(term, [],GLOBAL_OUT_LIST)
out_df = pd.DataFrame.from_dict(GLOBAL_OUT_LIST)

#counts the number of columns in the data frame and creates the header row.
numofcol = len(out_df.columns)
colnames = []
for i in range(1,numofcol+1):
    col = 'level '+str(i)
    colnames.append(col)
out_df.columns = [colnames]

#sorts the resulting csv file alphabetically
out_df_final = out_df.sort(colnames)

#utf-8-sig encoding fixs umlauts, etc, in the output csv.
out_df_final.to_csv('UAT_flatfile{}.csv'.format(timestamp), encoding='utf-8-sig',index=False)

print "Finished. See UAT_flatfile"+timestamp+".csv"
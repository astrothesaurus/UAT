# coding: utf-8

import rdflib

#assign this variable to the name of the exported UAT SKOS-RDF file, found in the same location as this script.
rdf = "export_skos-xl_15092014111447.rdf"

#reads the SKOS-RDF file into a RDFlib graph for use in this script
g = rdflib.Graph()
result = g.parse((rdf).encode('utf8'))

#defines certain properties within the SKOS-RDF file
litForm = rdflib.term.URIRef('http://www.w3.org/2008/05/skos-xl#literalForm')
prefLabel = rdflib.term.URIRef('http://www.w3.org/2008/05/skos-xl#prefLabel')
broader = rdflib.term.URIRef('http://www.w3.org/2004/02/skos/core#broader')
Concept = rdflib.term.URIRef('http://www.w3.org/2004/02/skos/core#Concept')
vocstatus = rdflib.term.URIRef('http://art.uniroma2.it/ontologies/vocbench#hasStatus')
altLabel = rdflib.term.URIRef('http://www.w3.org/2008/05/skos-xl#altLabel')
TopConcept = rdflib.term.URIRef('http://www.w3.org/2004/02/skos/core#topConceptOf')
ednotes = rdflib.term.URIRef('http://www.w3.org/2004/02/skos/core#editorialNote')
changenotes = rdflib.term.URIRef('http://www.w3.org/2004/02/skos/core#changeNote')
scopenotes = rdflib.term.URIRef('http://www.w3.org/2004/02/skos/core#scopeNote')
example = rdflib.term.URIRef('http://www.w3.org/2004/02/skos/core#example')
related = rdflib.term.URIRef('http://www.w3.org/2004/02/skos/core#related')

#a list of all top concepts
alltopconcepts = [bv for bv in g.subjects(predicate=TopConcept)]

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

#a function to get a list of all broader terms for a term
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

#a function to get a list of all alt terms for a term
def getaltterms(term):
    terminal = rdflib.term.URIRef(term)
    alternateterms = {}
    try:
        for ats in g.objects(subject=terminal, predicate=altLabel):
            try:
                alternateterms[terminal].append(ats)
            except KeyError:
                alternateterms[terminal] = [ats]
        return alternateterms[terminal]
    except KeyError:
        pass           

#a function to get a list of all related terms for a term
def getrelatedterms(term):
    terminal = rdflib.term.URIRef(term)
    relatedterms = {}
    try:
        for rts in g.objects(subject=terminal, predicate=related):
            try:
                relatedterms[terminal].append(rts)
            except KeyError:
                relatedterms[terminal] = [rts]
        return relatedterms[terminal]
    except KeyError:
        pass  

#a function to return editorial notes for a term
def getednotes(term):
    d = rdflib.term.URIRef(term)
    for ednoteterm in g.objects(subject=d, predicate=ednotes):
        return ednoteterm

#a function to return change notes for a term
def getchangenotes(term):
    d = rdflib.term.URIRef(term)
    for chnoteterm in g.objects(subject=d, predicate=changenotes):
        return chnoteterm

#a function to return scope notes for a term
def getscopenotes(term):
    d = rdflib.term.URIRef(term)
    for scnoteterm in g.objects(subject=d, predicate=scopenotes):
        return scnoteterm

#a function to return example notes for a term
def getexample(term):
    d = rdflib.term.URIRef(term)
    for termex in g.objects(subject=d, predicate=example):
        return termex

#a function to return the status of a term    
def getvocstatus(term):
    d=rdflib.term.URIRef(term)
    for vcstatus in g.objects(subject=d, predicate=vocstatus):
        return vcstatus

#a function to return the human readable form of the prefered version of a term
def lit(term):
    d = rdflib.term.URIRef(term)
    for prefterm in g.objects(subject=d, predicate=prefLabel):
        for litterm in g.objects(subject=prefterm, predicate=litForm):
            return litterm

#a function to return the human readable form of the alternate version of a term
def altlit(term):
    d = rdflib.term.URIRef(term)
    for altterm in g.objects(subject=d, predicate=litForm):
        return altterm

#returns a sorted list of terms, used for the alphabetical browser
def sortlist(unsortedlist):
    ustl = []
    sl = []
    for t in unsortedlist:
        ustl.append(lit(t))
    x = sorted(ustl)
    for s in x:
        for n in g.subjects(predicate=litForm, object=s):
            for m in g.subjects(predicate=prefLabel, object=n):
                sl.append(m)
    return sl

#returns a list of all deprecated terms in the file
deprecated = []
for term in allconcepts:
    termstats = getvocstatus(term)
    if termstats == "Deprecated":
        deprecated.append(lit(term))
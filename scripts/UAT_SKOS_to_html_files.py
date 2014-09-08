# coding: utf-8

from datetime import datetime
import csv
from unidecode import unidecode
import cStringIO
import rdflib
import json

#assign this variable to the name of the exported UAT SKOS-RDF file, found in the same location as this script.
rdf = "export_skos-xl_05092014050915.rdf"

print "Reading the SKOS file... this may take a few seconds."
#reads the SKOS-RDF file into a RDFlib graph for use in this script
g = rdflib.Graph()
result = g.parse((rdf).encode('utf8'))

#defines certain properties within the SKOS-RDF file
litForm = rdflib.term.URIRef('http://www.w3.org/2008/05/skos-xl#literalForm')
narrower = rdflib.term.URIRef('http://www.w3.org/2004/02/skos/core#narrower')
TopConcept = rdflib.term.URIRef('http://www.w3.org/2004/02/skos/core#hasTopConcept')
broader = rdflib.term.URIRef('http://www.w3.org/2004/02/skos/core#broader')
Concept = rdflib.term.URIRef('http://www.w3.org/2004/02/skos/core#Concept')
altLabel = rdflib.term.URIRef('http://www.w3.org/2008/05/skos-xl#altLabel')
prefLabel = rdflib.term.URIRef('http://www.w3.org/2008/05/skos-xl#prefLabel')
notes = rdflib.term.URIRef('http://www.w3.org/2004/02/skos/core#editorialNote')
status = rdflib.term.URIRef('http://purl.org/astronomy/uat/meta#status')
related = rdflib.term.URIRef('http://www.w3.org/2004/02/skos/core#related')

#list of all top level concepts
alltopconcepts = [bv for bv in g.objects(predicate=TopConcept)]

#list of all concepts
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

#a function to return the human readable form of the prefered version of a term.
def lit(term):
    d = rdflib.term.URIRef(term)
    for prefterm in g.objects(subject=d, predicate=prefLabel):
        for litterm in g.objects(subject=prefterm, predicate=litForm):
            return litterm

#a function to return the human readable form of the alternate version of a term.
def altlit(term):
    d = rdflib.term.URIRef(term)
    for altterm in g.objects(subject=d, predicate=litForm):
        return altterm

#a function to return the human readable form of a term.
def getnotes(term):
    d = rdflib.term.URIRef(term)
    for noteterm in g.objects(subject=d, predicate=notes):
        return noteterm

def getstatus(term):
    d = rdflib.term.URIRef(term)
    for cstatus in g.objects(subject=d, predicate=status):
        return cstatus

print "Writing term record files..."

for t in allconcepts:
    urlterm = unicode(lit(t)).replace(" ", "+").replace("/", "_")
    #get all the info for each term to use below
    usnts = getnarrowerterms(t)
    usbts = getbroaderterms(t)
    usats = getaltterms(t)
    usrts = getrelatedterms(t)
    stats = getstatus(t)
    notations = getnotes(t)
    
    #create file for this particular term
    fileterm = open("termrecords\\"+urlterm+".html", 'w')
    
    #file header
    fileterm.write("<html>\n")
    fileterm.write("<head><title>Term Record: "+lit(t).encode('utf-8')+"</title>\n")
    fileterm.write("<style>a,a:link,a:visited{color:#b4083a;text-decoration:underline}a:hover,a:active{text-decoration:none}a.tooltips,a.figure{color:#b4083a;font-weight:bold;text-decoration:none}h3{padding:0px; margin:0px;display:inline}</style>\n")
    fileterm.write("<meta charset='utf-8'></head>\n<body>\n")
    
    #term heading
    fileterm.write("<h3>"+lit(t).encode('utf-8')+"</h3>\n")
    
    #broader terms
    if usbts != None:
        fileterm.write("<dl>\n<p><dt><i>Broader Term(s)</i>:</dt>\n")
        usbt = []
        for ubt in usbts:
            usbt.append(unicode(lit(ubt)))
            sbt = sorted(usbt)
        for bt in sbt:
            bturl = bt.replace(" ", "+").replace("/", "")+".html"
            cbturl = bturl.encode('utf-8')
            fileterm.write("<dd><a href='"+cbturl+"'>"+bt.encode('utf-8')+"</a></dd>\n")
        fileterm.write("</p>\n")
    else:
        fileterm.write("<br /><a href='toplevelconcepts.html'>view all top level concepts</a>\n") 
    
    #narrower terms
    if usnts != None:
        fileterm.write("<p><dt><i>Narrower Term(s)</i>:</dt>\n")
        usnt = []
        for unt in usnts:
            usnt.append(unicode(lit(unt)))
            snt = sorted(usnt)
        for nt in snt:
            nturl = nt.replace(" ", "+").replace("/", "")+".html"
            cnturl = nturl.encode('utf-8')
            fileterm.write("<dd><a href='"+cnturl+"'>"+nt.encode('utf-8')+"</a></dd>\n")
        fileterm.write("</p>\n")
    
    #related terms
    if usrts != None:
        fileterm.write("<p><dt><i>Related Term(s)</i>:</dt>\n")
        usrt = []
        for urt in usrts:
            usrt.append(unicode(lit(urt)))
        srt = sorted(usrt)
        for rt in srt:
            rturl = rt.replace(" ", "+").replace("/", "")+".html"
            crturl = rturl.encode('utf-8')
            fileterm.write("<dd><a href='"+crturl+"'>"+rt.encode('utf-8')+"</a></dd>\n")
        fileterm.write("</p>\n")

    #alternate forms
    if usats != None:
        fileterm.write("<p><dt><i>Use For</i>:</dt>\n")
        usat = []
        for uat in usats:
            usat.append(unicode(altlit(uat)))
        sat = sorted(usat)
        for at in sat:
            fileterm.write("<dd>"+at.encode('utf-8')+"</dd>\n")
        fileterm.write("</p>\n")

    #notes
    if notations != None:
        fileterm.write("<p><dt><i>Editorial Notes</i>:</dt>\n")
        fileterm.write("<dd>"+notations.encode('utf-8')+"</dd>\n")
        fileterm.write("</p>\n")
    
    #status
    fileterm.write("<p><dt><i>Status</i>:</dt>\n")
    fileterm.write("<dd>"+stats.encode('utf-8')+"</dd></p>\n")
    
    #contribution link
    fileterm.write("<p><a target='_top' href='http://astrothesaurus.org/contributeterm/?term="+lit(t).encode('utf-8')+"'>Contribute</a></p>\n")
    
    #finish off html and close file
    fileterm.write("</dl>\n")
    fileterm.write("</body>\n</html>\n")
    fileterm.close()

print "Writing toplevelconcepts.html..."
#creates toplevelconcepts.html
filetop = open("termrecords\\toplevelconcepts.html", 'w')
filetop.write("<html>\n")
filetop.write("<head><title>Top Level Concepts</title>\n")
filetop.write("<style>a,a:link,a:visited{color:#b4083a;text-decoration:underline}a:hover,a:active{text-decoration:none}a.tooltips,a.figure{color:#b4083a;font-weight:bold;text-decoration:none}</style>\n")
filetop.write("<meta charset='utf-8'></head>\n<body>\n")
filetop.write("<h3>UAT Top Level Concepts</h3>\n")
ust = []
for ut in alltopconcepts:
    ust.append(unicode(lit(ut)))
st = sorted(ust)
for t in st:
    urlterm = t.replace(" ", "+").replace("/", "_")
    filetop.write("<a href='"+urlterm+".html'>"+t.encode('utf-8')+"</a></br>\n")
filetop.write("</body>\n</html>\n")
filetop.close()

print "Writing alphaleft.html..."
#creates alphabetial list of terms with first letter headers.
filealpha = open("alphaleft.html", 'w')
filealpha.write("<html>\n")
filealpha.write("<head><title>UAT Alphabetical List</title>\n")
filealpha.write("<style>f html,body,div,span,applet,object,iframe,h1,h2,h3,h4,h5,h6,p,blockquote,pre,a,abbr,acronym,address,big,cite,code,del,dfn,font,img,ins,kbd,q,s,samp,small,strike,sub,sup,tt,var,dl,dt,dd,ol,ul,li,fieldset,form,label,legend,table,caption,tbody,tfoot,thead,tr,th,td{margin:0;margin-top:0;padding:0;border:0;outline:0;font-weight:inherit;font-style:inherit;font-size:100%;font-family:inherit;vertical-align:baseline}html{font-size:100.01%}body{font-family:Arial,Tahoma,Verdana;font-size:0.9em;border:0;color:#222}ul,ol{list-style:none}img{border:none}.clear{clear:both}a,a:link,a:visited{color:#24041b;text-decoration:underline}a:hover,a:active{text-decoration:none}input,textarea{background-color:#f5f5f5;margin:5px;border-top:1px solid #eee;border-left:1px solid #eee;border-right:1px solid #ddd;border-bottom:1px solid #ddd;color:#333}#navi{float:left;width:890px;margin-top:0px;padding:0 5px;background:#24041b;font-family:Arial,Tahoma,Verdana}#nav,#nav ul{margin:0;padding:0;list-style-type:none;list-style-position:outside;position:relative}#nav li{float:left;position:relative}#nav a{display:block;padding:3px 15px;margin:7px 0;font-size:1em;font-weight:bold;text-decoration:none;color:#fff;border-right:1px solid #fff}#nav a:link,#nav a:visited{text-decoration:none}#nav a:hover{color:#24041b;background:#eee}#nav ul{position:absolute;display:none;z-index:99;border-top:1px solid #ccc}#nav ul a{width:180px;padding:10px;margin:0;float:left;color:#333;font-size:0.9em;background:#fff;border-top:none;border-left:2px solid #aaa;border-right:1px solid #bbb;border-bottom:1px solid #ccc}#nav ul a:hover{color:#444!important;background:#e0e0e0}#nav ul ul{margin-top:-1px;padding-left:2px}#nav li ul ul{margin-left:200px}#nav li:hover ul ul,#nav li:hover ul ul ul,#nav li:hover ul ul ul ul{display:none}#nav li:hover ul,#nav li li:hover ul,#nav li li li:hover ul,#nav li li li li:hover ul{display:block}</style>")
filealpha.write("<meta charset='utf-8'></head>\n<body>\n")
usac = []
for usc in allconcepts:
    usac.append(unicode(lit(usc)))
sac = sorted(usac, key=lambda s: s.lower())
previous = None  
for c in sac:
    if previous != c[0].lower():
        previous = c[0].lower()
        filealpha.write("<br /><b><a id='"+c[0]+"'>"+c[0]+"</a></b><br/><br/>")
    urlterm = c.replace(" ", "+").replace("/", "_")
    curl = urlterm.encode('utf-8')
    filealpha.write("<a href='termrecords/"+curl+".html' target='rightframe'>"+c.encode('utf-8')+"</a></br>\n")
filealpha.write("</body>\n</html>\n")
filealpha.close()

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
    #print sl
    return sl


def buildlist(termlist, filename):
    for xt in sortlist(termlist):
        xtr = lit(xt)
        urlxt = xtr.replace(" ", "+").replace("/", "_").encode('utf-8')
        filename.write("<li><a target='basefrm' href='termrecords/"+urlxt+".html'>"+lit(xt).encode('utf-8')+"</a>")
        yt = getnarrowerterms(xt)
        if yt != None:
            filename.write("\n<ul class='treeview'>\n")
            buildlist(yt, filename)
        if yt == None:
            filename.write("</li>\n")
    filename.write("</ul></li>\n")

print "Writing tree.html..."

filetree = open("tree.html", 'w')
filetree.write("<html>\n")
filetree.write("<head>\n<title>UAT Hierarchy Tree View</title>\n")
filetree.write("<script type='text/javascript' src='simpletreemenu.js'>\n")
filetree.write("/***********************************************\n")
filetree.write("* Simple Tree Menu- © Dynamic Drive DHTML code library (www.dynamicdrive.com)\n")
filetree.write("* This notice MUST stay intact for legal use\n")
filetree.write("* Visit Dynamic Drive at http://www.dynamicdrive.com/ for full source code\n")
filetree.write("***********************************************/\n")
filetree.write("</script>\n")
filetree.write("<link rel='stylesheet' type='text/css' href='simpletree.css' />\n")
filetree.write("<meta charset='utf-8'></head>\n<body>\n")
filetree.write("</head>\n")
filetree.write("</body>\n")
filetree.write("<h4>Unified Astronom Thesaurus</h4>\n")
filetree.write("<div class='advmenu'>\n")
filetree.write("<a href=\"javascript:ddtreemenu.flatten('treemenu1', 'expand')\">expand all</a> | <a href=\"javascript:ddtreemenu.flatten('treemenu1', 'collapse')\">collapse all</a>\n")
filetree.write("</div>\n")
filetree.write("<ul id='treemenu1' class='treeview'>\n")

buildlist(alltopconcepts, filetree)

filetree.write("<script type='text/javascript'>\n")
filetree.write("//ddtreemenu.createTree(treeid, enablepersist, opt_persist_in_days (default is 1))\n")
filetree.write("ddtreemenu.createTree('treemenu1', false)\n")
filetree.write("</script>\n")
filetree.write("</body>")

filetree.close()

print "Finished with everything!"
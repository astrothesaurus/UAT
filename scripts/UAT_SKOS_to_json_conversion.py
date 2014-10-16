# coding: utf-8

from datetime import datetime
import json

print "Reading the SKOS file...this may take a few seconds."

#all required rdf functions are found here
import rdfdefs as z

print "Creating the json... You can ignore the UnicodeWarning if you get one..."

#Alex's Script
flat_j = {}

for t in z.allconcepts:
    litt = unicode(z.lit(t))
    p = z.getbroaderterms(t)
    c = z.getnarrowerterms(t)
 
    pl = []
    rcl = []
    
    if p == None:
        pl = ["astro_thes"]
    else:
        for x in p:
            y = unicode(z.lit(x))
            pl.append(y)

    if c == None:
        pass
    else:
        for x in c:
            y = unicode(z.lit(x))
            rcl.append(y)
 
    flat_j[litt] = {

        "parents" : pl,
        "children" : [],
    "real_children": rcl,
    }

def recurse_traverse(info_dict, name_of_dict, flat_j):
    #step one: add all entries from flat_j to children dict that have parents that equal the key name from the dict
    for f in flat_j:
        if f in z.deprecated:
            pass
        else:
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

print "It might be a long pause here..."
recurse_traverse(astro_thes, "astro_thes", flat_j)

js_file = open("uat.json", "wb")
js_file.write(json.dumps(astro_thes))
js_file.close()

print "Finished!  See uat.json."
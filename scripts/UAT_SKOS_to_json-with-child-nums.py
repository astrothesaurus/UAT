print "You can ignore the UnicodeWarning if you get one..."

#Alex's script
flat_j = {}

for t in allconcepts:
    #litt = lit(t)
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
    
    emptylist = []
    getallchilds(t, emptylist)
    qw = len(emptylist)
    
    flat_j[litt] = {

        "parents" : pl,
        "children" : [],
        "real_children": rcl,
        "num_of_childs": qw
    }

import re
def recurse_traverse(info_dict, name_of_dict, flat_j):
    #step one: add all entries from flat_j to children dict that have parents that equal the key name from the dict
    for f in flat_j:
        if f in deprecated:
            pass
        else:
            if name_of_dict.encode("utf-8") in flat_j[f]["parents"]:
                we = f + " ("+str(flat_j[f]["num_of_childs"])+")"
                info_dict["children"].append({"name": we, "children":[]})
    #step two: now that the entries are added, repeat the process on each of them. A full path to that 
    #child within the original "info_dict" becomes the new info_dict. If there were no entries added
    #to children, this will throw a key error, so we stop recursing on this branch
    if len(info_dict["children"])>0:
        #print len(info_dict["children"])
        #print info_dict["children"]
        children_dict = info_dict["children"]
        children_dict.sort(); #sorts child terms alphabetically
        #print "children_dict"
        #print children_dict
        for i, child_dict in enumerate(children_dict):
            #print i
            dsf = child_dict["name"].replace(")","").replace("(","")
            dsf = re.sub("\d", "", dsf)[:-1]
            #print dsf
            recurse_traverse(children_dict[i], dsf, flat_j)
    else:
        del info_dict["children"]

astro_thes = {"children":[]}

print "It might be a long pause here as it loops through the UAT..."
recurse_traverse(astro_thes, "astro_thes", flat_j)

js_file = open("uat-childs.json", "wb")
js_file.write(json.dumps(astro_thes))
js_file.close()

print "Finished. See uat.json"
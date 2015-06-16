from collections import OrderedDict

alltermlist = []
for iall in allconcepts:
    alltermdict = {}
    alltermdict['prefLabel'] = lit(iall)
    alltermdict['@id'] = "http://uat.altbibl.io/term/"+lit(iall).replace(" ","_")
    alltermdict['hasStatus'] = getvocstatus(iall)

    alternate = getaltterms(iall) 
    if alternate != None:
        altdict = {}
        altlist= []

        for i in alternate:
            lita = altlit(i)
            altlist.append(lita)
            alltermdict['altLabel'] = altlist
        alltermlist.append(alltermdict)

    else:
        alltermlist.append(alltermdict)


print len(alltermlist)
sortedlist = sorted(alltermlist, key=lambda k: k['prefLabel']) 

js_file = open("uat_flat_api.json", "wb")
js_file.write(json.dumps(sortedlist))
js_file.close()

print "Finished. See uat_flat.json"
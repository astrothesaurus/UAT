#from collections import OrderedDict

import csv
import codecs
import cStringIO
from datetime import datetime

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

class UnicodeWriter:
    def __init__(self, f, dialect=csv.excel, encoding="utf-8-sig", **kwds):
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()
    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        data = self.encoder.encode(data)
        self.stream.write(data)
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)

timestamp = datetime.now().strftime("%Y_%m%d_%H%M")

resultFile2 = open("uat_flat"+timestamp+".csv",'wb')
resultFile = open("uat_flat_with_alts"+timestamp+".csv",'wb')

wr = UnicodeWriter(resultFile,dialect='excel',quoting=csv.QUOTE_ALL)
wr2 = UnicodeWriter(resultFile2,dialect='excel',quoting=csv.QUOTE_ALL)

wr.writerow(["preferred term"]+["alternate terms"])

alltermlist = []
for iall in allconcepts:
    alternate = getaltterms(iall)
    #print alternate
    altlist = []
    if alternate != None:
        for i in alternate:
            lita = altlit(i)
            print lita
            altlist.append(lita)
    else:
        altlist = []
    #print altlist
    lits = lit(iall)
    wr.writerow([lits]+altlist)
    wr2.writerow([lits])

resultFile.close()
resultFile2.close()

print "Finished. See uat_flat.csv"

#print allterms()

#    print iall
#print allconcepts
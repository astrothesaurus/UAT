# coding: utf-8

from datetime import datetime
import pandas as pd

print "Reading the SKOS file...this may take a few seconds."

#all required rdf functions are found here
import rdfdefs as z

#a function to travel all the way down each path in the thesarus and return this information into a list.
def descend(term, parents, out_list):
    lvln = z.getnarrowerterms(term)
    if lvln != None: #if there are narrower terms...
        for a in lvln:
            children = parents[:]
            if z.lit(a) in z.deprecated:
                children = parents[:]
                children.append(z.lit(term))
                if children not in out_list:
                    out_list.append(children)
            else:
                children.append(z.lit(term))
                if children not in out_list:
                    out_list.append(children)
                descend(a, children, GLOBAL_OUT_LIST)
    else: #if there are no more narrower terms...
        children = parents[:]
        children.append(z.lit(term))
        if children not in out_list:
            out_list.append(children)

print "Organizing the terms, almost finished."
#runs the functions across all terms and outputs to pandas dataframe.
timestamp = datetime.now().strftime("_%Y_%m%d_%H%M%S")
GLOBAL_OUT_LIST = []
out_list = []
for term in z.alltopconcepts:
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
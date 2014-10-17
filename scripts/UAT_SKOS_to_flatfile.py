# coding: utf-8

#a function to travel all the way down each path in the thesarus and return this information into a list.
def descend(term, parents, out_list):
    lvln = getnarrowerterms(term)
    if lvln != None: #if there are narrower terms...
        for a in lvln:
            children = parents[:]
            if lit(a) in deprecated:
                children = parents[:]
                children.append(lit(term))
                if children not in out_list:
                    out_list.append(children)
            else:
                children.append(lit(term))
                if children not in out_list:
                    out_list.append(children)
                descend(a, children, GLOBAL_OUT_LIST)
    else: #if there are no more narrower terms...
        children = parents[:]
        children.append(lit(term))
        if children not in out_list:
            out_list.append(children)

print "Organizing the terms..."
#runs the functions across all terms and outputs to pandas dataframe.
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
out_df_final.to_csv('uat.csv', encoding='utf-8-sig',index=False)

print "Finished. See uat.csv"
This XML to JSON converter was written by Alex Holachek.
It converts the XML exported from MAIstro into a JSON format that can be used in the D3.js dendrogram script.

To use this script you will need the following Python packages:
lxml, 
unidecode,
re

index.html contains the D3.js script used to create the dendrogram from the uat.json file that will result from running xmltojson.py on the astronomy_thesaurus.txt file
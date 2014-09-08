This contains the files needed to create the alphabetical, hierarchical, and dendrogram browsers of the UAT.





These are the files used to make the dendrogram browser at http://astrothesaurus.org/dendrogram/

UAT_SKOS_to_json_conversion.py is the Python script that converts the RDF version of the UAT as exported from VocBench into a JSON file.  Alex Holachek wrote the complicated bits of this script.

d3.v3.js is a modified version of the standard D3.js javascript library code that removes the mouse-wheel interaction.  This just an inelegant way to remove some of the mouse-wheel functionality that I did not want to have on the dendrogram.  D3.js is written and maintined by Michael Bostock (http://d3js.org/).

index.html contains the javascript used to activate the D3 library which creates the dendrogram from a JSON file.  The JSON file used is the result of running the the above python script on the RDF export from VocBench.

style.css is the file references by index.html to enchance the look and feel of the UAT dendrogram.

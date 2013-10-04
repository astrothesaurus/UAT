These are the files used to make the dendrogram browser at http://astrothesaurus.org/dendrogram/

xmltojson.py, nested_json_generator.py, and sample_word_freq_dict.py are Python scripts that converts the XML version of the UAT as exported from MAIstro into a JSON file.  These scripts were written by Alex Holachek, and her original work can be found here: https://github.com/aholachek/code_examples/tree/master/Data_Science_Final_Project/Interactive_Frequency_Histogram

d3.v3.js is a modified version of the standard D3.js javascript library code that removes the mouse-wheel interaction.  This just an inelegant way to remove some of the mouse-wheel functionality that I did not want to have on the dendrogram.

index.html contains the javascript used to activate the D3 library which creates the dendrogram from a JSON file.  The JSON file used is the result of running xmltojson.py on the astronomy_thesaurus.txt file.

style.css is the file references by index.html to enchance the look and feel of the UAT dendrogram.
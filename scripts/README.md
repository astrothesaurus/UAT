This folder contains scripts that manipulate the RDF file exported from VocBench into other useful and/or interesting formats.

Only run UAT_SKOS_master.py, it will call the other scripts.  However, you can comment out any of the others scripts from the bottom of the master script.

Resulting files:

1) A series of html files used to support both the hierarchical and alphabetical browers of the UAT
#execfile("UAT_SKOS_to_html.py")

2) A CSV flatfile that displays the hierarchy of the thesaurus
#execfile("UAT_SKOS_to_flatfile.py")

3) A json file with the structure of the UAT
#execfile("UAT_SKOS_to_json.py")

4) Another json file with the UAT structure that also includes the sum of each terms child terms
#execfile("UAT_SKOS_to_json-with-child-nums.py")

5) Two csv files, one of which is just a striaght list of all terms in the UAT, and the other has a straight list of all terms with all alternative terms.
#execfile("UAT_SKOS_to_csv_lists.py")

6) A javascript file for use in the UAT autocomplete widget
#execfile("UAT_SKOS_to_autocomplete.py")
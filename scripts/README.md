This folder contains scripts that manipulate the RDF file exported from VocBench into other useful and/or interesting formats.

Only run UAT_SKOS_master.py, it will call the other four scripts.  However, you can comment out any of the four scripts you want from the bottom of the master script.

Running the master script with no options commented out will produce:

1) A CSV flatfile that lists each path to each child term in the thesaurus.

2) A nested json file currently used in the dendrogram browser on astrothesaurus.org.  Alex Holachek of SAO/NASA ADS wrote the complicated bits of this script.

3) A series of html files used to support both the hierarchical and alphabetical browers of the UAT.

4) A javascript file used in the autocomplete widget.
This folder contains scripts that manipulate the RDF file exported from VocBench into other useful and/or interesting formats.

UAT_SKOS_to_flatfile_conversion.py will convert the RDF file from VocBench into a CSV flatfile, that lists each path to each child term in the thesaurus.  In order to run the script, you'll need to edit the script in order to assign the rdf variable to the name of the exported file, such as:
rdf = "export_skos-xl_07052014030250.rdf"

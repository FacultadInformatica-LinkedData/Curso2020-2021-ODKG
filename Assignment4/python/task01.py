# -*- coding: utf-8 -*-
"""Task01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F_-ecT8oUiazpj1s0llIUqqU_nPQS88V

**Task 01: Reading and writing RDF files**

Reading and writing files that contain triples is very simple in RDFlib, for this we will use two library methods: parse and serialize.
"""

!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4"

from rdflib import Graph, Namespace, Literal
g = Graph()

"""We can add triples to our graph using *parse*, which will read the provided resource. We must also indicate the format if it cannot be inferred."""

g.parse(github_storage+"/resources/example1.rdf", format="xml")

"""To view the graph in a specific format we can use *serialize*. For example here we show the output of the graph in turtle"""

print(g.serialize(format="ttl").decode("UTF-8"))

"""The resource can be local or remote, as in our case. The result is the same. We can add all the data we want to our graph, the data will be merged."""

g.parse(github_storage+"/resources/example2.rdf", format="xml")

"""Now we can check the result by showing the triples in a simple way."""

for subj, pred, obj in g:
  print(subj,pred,obj)

"""Now we can see the inverse operation, serializing this data to some format that allows it. This process also allows us a simple conversion between formats."""

print(g.serialize(format="xml").decode("UTF-8"))

"""We can also save the serialized result in a file, you can see this resulting file in the left panel."""

g.serialize("example1.ttl", format="ttl")
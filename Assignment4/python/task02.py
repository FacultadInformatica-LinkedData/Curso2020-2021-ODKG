# -*- coding: utf-8 -*-
"""Task02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hqe3-1wN3c7nQmThrIYmj7gsO_Q4c0RT

**Task 02: Managing statements**

We start with an empty graph
"""

!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4"

from rdflib import Graph, Namespace, Literal
g = Graph()

"""We create John Smith resources: subject and object"""

fullName = Literal("John Smith")
EX = Namespace("http://example.org/")
johnURI = EX.JohnSmith

"""And generate the complete resource adding the full statement"""

VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

resource = (johnURI, VCARD.FN, fullName)

print(resource)

g.add(resource)

"""We create another resource for Jane with her full name and email

We can reduce a bit what we have done in the previous task, pay attention to the double parentheses, add () accepts a single parameter in the form of a tuple, not 3 parameters.
"""

g.add((EX.JaneSmith, VCARD.FN, Literal("Jane Smith")))
g.add((EX.JaneSmith, VCARD.hasEmail, Literal("jsmith@example.org")))

"""We add a relationship between John and Jane using the FOAF vocabulary

There are certain namespaces that are native to RDFlib, FOAF is one of them and we don't need to declare it ourselves
"""

from rdflib import FOAF

g.add((EX.JohnSmith, FOAF.knows, EX.JaneSmith))

"""See the final result"""

print(g.serialize(format="ttl").decode("UTF-8"))
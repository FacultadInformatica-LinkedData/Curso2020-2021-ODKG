# -*- coding: utf-8 -*-
"""Task09.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eDDHOQPTQK6iVd-Uj_ht5jwMqcO0FCpa

**Task 09: Data linking**
"""

!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4/"

from rdflib import Graph, Namespace, Literal, URIRef
g1 = Graph()
g2 = Graph()
g3 = Graph()
g1.parse(github_storage+"resources/data03.rdf", format="xml")
g2.parse(github_storage+"resources/data04.rdf", format="xml")

print(" *************** data 01 ************************")
for s1,p1,o1 in g1:
  print(s1,p1,o1)

print(" *************** data 02 ************************")
for s2,p2,o2 in g2:
  print(s2,p2,o2)

"""Search for individuals in the two graphs and link them using the OWL: sameAs property, insert these matches in g3. We consider that two individuals are the same if they have the same nickname and family name. Keep in mind that the URIs do not have to be the same for the same individual in the two graphs."""

from rdflib.plugins.sparql import prepareQuery
from rdflib.namespace import RDF, RDFS
from rdflib import XSD
ng1=Namespace("http://data.three.org#")
ng2=Namespace("http://data.four.org#")
vcard=Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
owl=Namespace("http://www.w3.org/2002/07/owl#")

q1 = prepareQuery('''
   SELECT 
      ?x ?nickname1 ?familyname1
   WHERE { 
      ?x rdf:type  ng1:Person.
      ?x  vcard:Given ?nickname1.
      ?x vcard:Family  ?familyname1.
    }
    ''', initNs = { "ng1": ng1, "vcard":vcard,"rdf":RDF}
)
q2 = prepareQuery('''
     construct{ ?x owl:sameAs ?y}
      WHERE { 
        ?x rdf:type  ng2:Person.
        ?x  vcard:Given ?nickname2.
        ?x vcard:Family  ?familyname2.
        FILTER(?nickname2= ?nickname1).
        FILTER(?familyname2= ?familyname1)
    }
    ''', initNs = { "ng2": ng2, "vcard":vcard,"xsd":XSD,"owl":owl,"rdf":RDF}
)

for r in g1.query(q1):
  for r2 in g2.query(q2,initBindings = {'?nickname1': Literal(r.nickname1,datatype=XSD.string),'?familyname1': Literal(r.familyname1,datatype=XSD.string),
                                        '?y':r.x}):
    print(r2)
    g3.add(r2)
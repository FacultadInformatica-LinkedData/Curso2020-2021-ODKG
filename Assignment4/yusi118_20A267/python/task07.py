# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UC1io2Dncy7ZTsaIKLi0RFDdAFM838nH

**Task 07: Querying RDF(s)**
"""

!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4"

"""Read the RDF file"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/resources/example6.rdf", format="xml")
for s,p,o in g:
  print(s,p,o)

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""
#RDFLib 
ns=Namespace("http://somewhere#")

for s in g.subjects(RDFS.subClassOf, ns.Person):
  print(s)
  for r in g.subjects(RDFS.subClassOf,s):
    print(r)

# SPARQL 
from rdflib.plugins.sparql import prepareQuery

q1 = prepareQuery('''
  SELECT 
    ?x
  WHERE { 
    ?x  rdfs:subClassOf/rdfs:subClassOf*  ns:Person. 
  }
  ''', initNs = { "ns": ns,"rdfs":RDFS}
)
for r in g.query(q1):
  print(r)
"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**"""
#RDFLib
sub=[]
for s in g.subjects(RDF.type,ns.Person):
  print(s)
  sub.append(s)

for s in g.subjects(RDF.type/RDFS.subClassOf,ns.Person):
  print(s) 
  sub.append(s)

  #SPARQL 

q1 = prepareQuery('''
  SELECT 
    ?ind
  WHERE { 
    ?ind a/rdfs:subClassOf*  ns:Person. 
  }
  ''', initNs = { "ns": ns,"rdfs":RDFS}
)
for r in g.query(q1):
  print(r)

""" **TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
"""
#RDFLib
for i in range(len(sub)):
  for s,p,o in  g.triples((sub[i],None,None)):
    if(p!=RDF.type):
      print(s,p)

#SPARQL
q1 = prepareQuery('''
  SELECT 
    ?ind ?p 
  WHERE { 
    ?ind a/rdfs:subClassOf*  ns:Person. 
    ?ind ?p  ?value
    FILTER(?p!=rdf:type)
  }
  ''', initNs = { "ns": ns,"rdfs":RDFS}
)
for r in g.query(q1):
  print(r)

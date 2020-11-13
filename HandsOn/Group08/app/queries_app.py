# -*- coding: utf-8 -*-

from rdflib import Graph, Namespace, Literal, XSD

g = Graph()
g.parse("output-with-links.nt", format="nt")

print(len(g))

from rdflib.plugins.sparql import prepareQuery

s = Namespace("http://schema.org/")
ex = Namespace("http://www.publicProcurementMurciaCOVID19.es/ontology#")
o= Namespace("http://www.w3.org/2002/07/owl#")

"""
print("INICIO QUERY 1: Top 10 productos mas pedidos el dia 04/06")
print()
q1 = prepareQuery('''
  SELECT
      ?p (SUM(?c) as ?nc)
  WHERE {

     ?order s:orderDate '2020-04-06T00:00:00Z'^^s:Date.
     ?order ex:hasProductQuantity ?c.
     ?order s:orderedItem ?p.
     ?p rdf:type s:Product.

  }
  GROUP BY ?p
  ORDER BY DESC(?nc)
  LIMIT 30

  ''',
  initNs={"s": s, "ex": ex}
  )
for r in g.query(q1):
  print(r.p, r.nc)
"""

print()
print()
print("INICIO QUERY 1: Top 10 productos mas pedidos por dia")
print()
q2 = prepareQuery('''
  SELECT
      ?d ?p (SUM(?c) as ?nc)
  WHERE {

     ?order s:orderDate ?d.
     ?order ex:hasProductQuantity ?c.
     ?order s:orderedItem ?pr.
     ?pr rdf:type s:Product.
     ?pr s:name ?p.

  }
  GROUP BY ?d ?pr
  ORDER BY ?d DESC(?nc)
  LIMIT 100

  ''',
  initNs={"s": s, "ex": ex}
  )
for r in g.query(q2):
  print(r.d, r.p, r.nc)

print()
print()
print("INICIO QUERY 2: Top 10 servicios mas pedidos por dia")
print()
q3 = prepareQuery('''
  SELECT
      ?d ?s (COUNT(?s) as ?ns)
  WHERE {

     ?order s:orderDate ?d.
     ?order s:orderedItem ?sv.
     ?sv rdf:type s:Service.
     ?sv s:name ?s.

  }
  GROUP BY ?d ?sv
  ORDER BY ?d DESC(?ns)
  LIMIT 100

  ''',
  initNs={"s": s, "ex": ex}
  )
for r in g.query(q3):
  print(r.d, r.s, r.ns)

"""
print()
print()
print("INICIO QUERY 4: Cantidad pendiente a lo largo del tiempo")
print()
q4 = prepareQuery('''
  SELECT
      ?d ?p (SUM(?c) as ?nc)
  WHERE {

     ?order s:orderDate ?d.
     ?order ex:hasProductQuantityPending ?c.
     FILTER (?c > 0).
     ?order s:orderedItem ?pr.
     ?pr rdf:type s:Product.
     ?pr s:name ?p.

  }
  GROUP BY ?d ?pr
  ORDER BY ?d DESC(?nc)
  LIMIT 100

  ''',
  initNs={"s": s, "ex": ex}
  )
for r in g.query(q4):
  print(r.d, r.p, r.nc)
"""

print()
print()
print("INICIO QUERY 3: Cantidad pendiente a lo largo del tiempo con numero de hospitalizaciones")
print()
q5 = prepareQuery('''
  SELECT
      ?d ?cases ?p (SUM(?c) as ?nc)
  WHERE {

     ?order s:orderDate ?d.
     ?order ex:hasProductQuantityPending ?c.
     FILTER (?c > 0).
     ?order s:orderedItem ?pr.
     ?pr rdf:type s:Product.
     ?pr s:name ?p.
     ?order s:customer ?ccaa.
     ?ccaa ex:hasCovidStatus ?covid.
     ?covid ex:inDate ?d.
     ?covid ex:numberHospitalizations ?cases.

  }
  GROUP BY ?d ?p
  ORDER BY ?d DESC(?nc)
  LIMIT 100

  ''',
  initNs={"s": s, "ex": ex}
  )
for r in g.query(q5):
  print(r.d, r.cases, r.p, r.nc)


exit(0)
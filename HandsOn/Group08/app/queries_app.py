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




#Incidencia covid por comunidades
q2 = prepareQuery('''
  SELECT
    ?iso ?fecha ?na ?np ?nh ?nu
  WHERE {
    
    ?CCAA ex:hasCovidStatus  ?CS.
    ?CCAA ex:hasISOCode ?iso.
    ?CS ex:numPositiveAC ?na.
    ?CS ex:numPositivePCR ?np.
    ?CS ex:numberHospitalizations ?nh.
    ?CS ex:numberUCI ?nu.
    ?CS ex:inDate ?fecha .
    
  }
  
  ORDER BY ASC(?fecha)
  LIMIT 30
  ''',
  initNs = { "s": s, "ex": ex}
)

print("\n Incidencia covid por comunidades ")
for r in g.query(q2):
  print(r.iso, r.fecha ,r.na, r.np, r.nh ,r.nu)



#Incidencia covid por comunidades en una fecha dada
q21 = prepareQuery('''
  SELECT
    ?iso ?na ?np ?nh ?nu
  WHERE {
    
    
    ?CCAA ex:hasCovidStatus  ?CS.
    ?CCAA ex:hasISOCode ?iso.
    ?CS ex:inDate '2020-04-06T00:00:00Z'^^s:Date.
    ?CS ex:numPositiveAC ?na.
    ?CS ex:numPositivePCR ?np.
    ?CS ex:numberHospitalizations ?nh.
    ?CS ex:numberUCI ?nu.
    ?CS ex:inDate ?fecha .
    
  }
  ''',
  initNs = { "s": s, "ex": ex,"res":res}
)

print("\n Incidencia covid por comunidades en una fecha dada ")
for r in g.query(q21):
  print(r.iso ,r.na, r.np, r.nh ,r.nu)

#Incidencia acumulada hasta el final de las fechas por comunidades
q3 = prepareQuery('''
  SELECT
      ?iso ?link (SUM(?na) as ?nCount) (SUM(?np) as ?npCount) (SUM(?nh) as ?nhCount) (SUM(?nu) as ?nuCount)
  WHERE {       
    ?CCAA ex:hasISOCode ?iso.
    ?CCAA o:sameAs ?link.
    ?CCAA ex:hasCovidStatus ?CS.  
    ?CS ex:numPositiveAC ?na.
    ?CS ex:numPositiveAC ?na.  
    ?CS ex:numPositivePCR ?np.
    ?CS ex:numberHospitalizations ?nh.
    ?CS ex:numberUCI ?nu. 
    
  }
  GROUP BY ?CCAA
  
  ''',
  initNs = { "s": s, "ex": ex,"o":o }
)

print("\n Incidencia covid  acumulada por comunidades hasta el final ")
for r in g.query(q3):
  print(r.iso ,r.link ,r.nCount,  r.npCount ,r.nhCount, r.nuCount)


#numero de contratos por organizacion en el  total de las fechas
q4 = prepareQuery('''
  SELECT
    ?name ?link (COUNT(?Order) as ?orderCount) (SUM(?coste) as ?ncoste)
  WHERE {
    ?company s:name ?name.
    ?Order s:seller ?company.
    ?Order ex:hasOrderAmount ?coste.
    OPTIONAL { ?company o:sameAs  ?link. }
  }
  GROUP BY ?company
  ORDER BY DESC(?orderCount)
  LIMIT 10
  ''',
  initNs = { "s": s, "ex": ex, "o":o}
)
print("\n numero de contratos por organizacion en el  total de las fechas ")
for r in g.query(q4):
  print(r.name ,r.link ,r.orderCount, r.ncoste)


#numero de contratos por organizacion en una fecha
q41 = prepareQuery('''
  SELECT
    ?name ?link (COUNT(?Order) as ?orderCount) (SUM(?coste) as ?ncoste)
  WHERE {
    ?Order s:orderDate '2020-04-07T00:00:00Z'^^s:Date.
    ?Order ex:hasOrderAmount ?coste.
    ?Order s:seller ?company.
    ?company s:name ?name.
    OPTIONAL { ?company o:sameAs  ?link. }
  }
  GROUP BY ?company
  ORDER BY DESC(?orderCount)
  LIMIT 10
  ''',
  initNs = { "s": s, "ex": ex, "o":o}
)

print("\n #numero de contratos por organizacion en una fecha ")
for r in g.query(q41):
  print(r.name ,r.link ,r.orderCount, r.ncoste)




exit(0)
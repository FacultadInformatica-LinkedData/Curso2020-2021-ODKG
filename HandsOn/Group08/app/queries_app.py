# -*- coding: utf-8 -*-

from rdflib import Graph, Namespace, Literal, XSD

g = Graph()
g.parse("output-with-links.nt", format="nt")

print(len(g))

from rdflib.plugins.sparql import prepareQuery

s = Namespace("http://schema.org/")
ex = Namespace("http://www.publicProcurementMurciaCOVID19.es/ontology#")
o= Namespace("http://www.w3.org/2002/07/owl#")


print()
print()
print("INICIO QUERY 01: Productos mas pedidos y su cantidad")
print()
q01 = prepareQuery('''
  SELECT
     ?prod (SUM(?quantity) as ?totalQuantity)
  WHERE {

     ?order s:orderedItem ?pr.
     ?pr rdf:type s:Product.
     ?pr s:name ?prod.
     ?order ex:hasProductQuantity ?quantity.
  }
  GROUP BY ?pr
  ORDER BY DESC(?totalQuantity) ?prod
  LIMIT 100

  ''',
  initNs={"s": s, "ex": ex}
  )
for r in g.query(q01):
  print(r.prod, r.totalQuantity)


print()
print()
print("INICIO QUERY 02: Servicios mas pedidos y el numero de veces pedidos")
print()
q02 = prepareQuery('''
  SELECT
     ?service (COUNT(?service) as ?totalNumber)
  WHERE {

     ?order s:orderedItem ?serv.
     ?serv rdf:type s:Service.
     ?serv s:name ?service.
     
  }
  GROUP BY ?service
  ORDER BY DESC(?totalNumber) ?service
  LIMIT 100

  ''',
  initNs={"s": s, "ex": ex}
  )
for r in g.query(q02):
  print(r.service, r.totalNumber)


print()
print()
print("INICIO QUERY 03: Dado un producto (NAME), ver evoluacion temporal de la cantidad pedida y lo que falta")
print()
#uriProduct type String
def query03(nameProduct):
  q03 = prepareQuery('''
    SELECT
      ?date (SUM(?quantity) as ?nQuantity) (SUM(?pending) as ?nPending)
    WHERE {
       ?pr rdf:type s:Product.
       ?pr s:name ?product.
       ?order s:orderedItem ?pr.
       ?order s:orderDate ?date.
       ?order ex:hasProductQuantity ?quantity.
       ?order ex:hasProductQuantityPending ?pending.
    }
    GROUP BY ?date
    ORDER BY ?date
    LIMIT 100
    ''',
        initNs={"s": s, "ex": ex}
    )

  for r in g.query(q03, initBindings={'?product': Literal(nameProduct, datatype=XSD.string)}):
    print(r.date, r.nQuantity, r.nPending)


query03("GUANTE VINILO")
print()
query03("GUANTES DE NITRILO, CON Y SIN POLVO")


print()
print()
print("INICIO QUERY 04: Top 10: Lista de los productos mas pedidos por dia")
print()
q04 = prepareQuery('''
  SELECT
     ?date ?product (SUM(?quantity) as ?nq)
  WHERE {

     ?order s:orderDate ?date.
     ?order ex:hasProductQuantity ?quantity.
     ?order s:orderedItem ?pr.
     ?pr rdf:type s:Product.
     ?pr s:name ?product.

  }
  GROUP BY ?date ?pr
  ORDER BY ?date DESC(?nq)
  LIMIT 100

  ''',
  initNs={"s": s, "ex": ex}
  )
for r in g.query(q04):
  print(r.date, r.product, r.nq)


print()
print()
print("INICIO QUERY 04_1: Dado un dia, el Top 10 de la Lista de los productos mas pedidos")
print()
def query04_1(date):
  q04_1 = prepareQuery('''
    SELECT
      ?product (SUM(?quantity) as ?nq)
    WHERE {
  
       ?order s:orderDate ?date.
       ?order ex:hasProductQuantity ?quantity.
       ?order s:orderedItem ?pr.
       ?pr rdf:type s:Product.
       ?pr s:name ?product
  
    }
    GROUP BY ?pr
    ORDER BY DESC(?nq)
    LIMIT 10
    ''',
        initNs={"s": s, "ex": ex}
    )

  for r in g.query(q04_1, initBindings={'?date': Literal(date, datatype=s+"Date")}):
    print(r.product, r.nq)


query04_1("2020-04-06T00:00:00Z")
print()



print()
print()
print("INICIO QUERY 05: Top 10: Lista de los servicios mas pedidos por dia")
print()
q05 = prepareQuery('''
  SELECT
      ?date ?service (COUNT(?service) as ?ns)
  WHERE {

     ?order s:orderDate ?date.
     ?order s:orderedItem ?sv.
     ?sv rdf:type s:Service.
     ?sv s:name ?service.

  }
  GROUP BY ?date ?sv
  ORDER BY ?date DESC(?ns) ?service
  LIMIT 100

  ''',
    initNs={"s": s, "ex": ex}
  )

for r in g.query(q05):
  print(r.date, r.service, r.ns)


print()
print()
print("INICIO QUERY 05_1: Dado un dia, el Top 10: Lista de los servicios mas pedidos por dia")
print()
def query05_1(date):
  q05_1 = prepareQuery('''
    SELECT
      ?service (COUNT(?service) as ?ns)
    WHERE {
  
       ?order s:orderDate ?date.
       ?order s:orderedItem ?sv.
       ?sv rdf:type s:Service.
       ?sv s:name ?service.
  
    }
    GROUP BY ?sv
    ORDER BY DESC(?ns) ?service
    LIMIT 10
    ''',
        initNs={"s": s, "ex": ex}
    )

  for r in g.query(q05_1, initBindings={'?date': Literal(date, datatype=s + "Date")}):
    print(r.service, r.ns)


query05_1("2020-04-22T00:00:00Z")
print()



print()
print()
print("INICIO QUERY 06: Cantidad pendiente a lo largo del tiempo con el numero de hospitalizaciones")
print()
q6 = prepareQuery('''
  SELECT
      ?date ?cases ?product (SUM(?quantity) as ?nq)
  WHERE {

     ?order s:orderDate ?date.
     ?order ex:hasProductQuantityPending ?quantity.
     FILTER (?quantity > 0).
     ?order s:orderedItem ?pr.
     ?pr rdf:type s:Product.
     ?pr s:name ?product.
     ?order s:customer ?ccaa.
     ?ccaa ex:hasCovidStatus ?covid.
     ?covid ex:inDate ?date.
     ?covid ex:numberHospitalizations ?cases.

  }
  GROUP BY ?date ?pr
  ORDER BY ?date DESC(?nq)
  LIMIT 100

  ''',
  initNs={"s": s, "ex": ex}
  )
for r in g.query(q6):
  print(r.date, r.cases, r.product, r.nq)


print()
print()
print("INICIO QUERY 06_1: Cantidad pendiente a lo largo del tiempo")
print()
q06_1 = prepareQuery('''
  SELECT
      ?date ?product (SUM(?quantity) as ?nq)
  WHERE {

     ?order s:orderDate ?date.
     ?order ex:hasProductQuantityPending ?quantity.
     FILTER (?quantity > 0).
     ?order s:orderedItem ?pr.
     ?pr rdf:type s:Product.
     ?pr s:name ?product.

  }
  GROUP BY ?date ?pr
  ORDER BY ?date DESC(?nq)
  LIMIT 100

  ''',
  initNs={"s": s, "ex": ex}
  )
for r in g.query(q06_1):
  print(r.date, r.product, r.nq)



print()
print()
print("INICIO QUERY 07: Incidencia covid por comunidades")
print()
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
                  initNs={"s": s, "ex": ex}
                  )

for r in g.query(q2):
  print(r.iso, r.fecha, r.na, r.np, r.nh, r.nu)

# Incidencia covid por comunidades en una fecha dada
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
     initNs={"s": s, "ex": ex}
  )

print("\n Incidencia covid por comunidades en una fecha dada ")
for r in g.query(q21):
  print(r.iso, r.na, r.np, r.nh, r.nu)

# Incidencia acumulada hasta el final de las fechas por comunidades
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
                  initNs={"s": s, "ex": ex, "o": o}
                  )

print("\n Incidencia covid  acumulada por comunidades hasta el final ")
for r in g.query(q3):
  print(r.iso, r.link, r.nCount, r.npCount, r.nhCount, r.nuCount)

# numero de contratos por organizacion en el  total de las fechas
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
                  initNs={"s": s, "ex": ex, "o": o}
                  )
print("\n numero de contratos por organizacion en el  total de las fechas ")
for r in g.query(q4):
  print(r.name, r.link, r.orderCount, r.ncoste)

# numero de contratos por organizacion en una fecha
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
                   initNs={"s": s, "ex": ex, "o": o}
                   )

print("\n #numero de contratos por organizacion en una fecha ")
for r in g.query(q41):
  print(r.name, r.link, r.orderCount, r.ncoste)

exit(0)
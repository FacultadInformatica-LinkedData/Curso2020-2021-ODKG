# -*- coding: utf-8 -*-

from rdflib import Graph, Namespace, Literal, XSD
import pandas as pd


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
def getQ01():
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
    
      ''',
      initNs={"s": s, "ex": ex}
      )
    output = g.query(q01)
    df = pd.DataFrame(output, columns=["Produc", "Quantity"])
    return df
print(getQ01())


print()
print()
print("INICIO QUERY 02: Servicios mas pedidos, el numero de veces pedidos, el dinero obtenido y el dinero pendiente")
print()
def getQ02():
    q02 = prepareQuery('''
      SELECT
         ?service (COUNT(?service) as ?totalNumber) (SUM(?amount) as ?totalAmount) (SUM(?pending) as ?totalPending)
      WHERE {
    
         ?order s:orderedItem ?serv.
         ?serv rdf:type s:Service.
         ?serv s:name ?service.
		 ?order ex:hasOrderAmount ?amount.
         ?order ex:hasPendingAmount ?pending.
      }
      GROUP BY ?service
      ORDER BY DESC(?totalNumber) ?service
    
      ''',
      initNs={"s": s, "ex": ex}
      )
    output = g.query(q02)
    df = pd.DataFrame(output, columns=["Service", "Requested times", "Total amount", "Pending amount"])
    return df
print(getQ02())


print()
print()
print("INICIO QUERY 03: Dado un producto (NAME), ver evoluacion temporal de la cantidad pedida y lo que falta")
print()
#uriProduct type String
def getQ03(nameProduct):
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
    ''',
        initNs={"s": s, "ex": ex}
    )

  output = g.query(q03, initBindings={'?product': Literal(nameProduct, datatype=XSD.string)})
  df = pd.DataFrame(output, columns=["Date", "Quantity", "Quantity Pending"])
  df["Date"] = df["Date"].astype(str)
  df['Date'] = pd.to_datetime(df['Date'])
  return df


print(getQ03("GUANTE VINILO"))
print()
print(getQ03("GUANTES DE NITRILO, CON Y SIN POLVO"))



print()
print()
print("INICIO QUERY 03_1: Dado un servicio (NAME), ver evoluacion temporal del numero de veces que se pide un servicio (acumulativo)")
print()
#uriProduct type String
def getQ03_1(nameService):
  q03_1 = prepareQuery('''
    SELECT
      ?date (COUNT(?ser) as ?nSer)
    WHERE {
       ?ser rdf:type s:Service.
       ?ser s:name ?service.
       ?order s:orderedItem ?ser.
       ?order s:orderDate ?date.
    }
    GROUP BY ?date
    ORDER BY ?date
    ''',
        initNs={"s": s, "ex": ex}
    )

  output = g.query(q03_1, initBindings={'?service': Literal(nameService, datatype=XSD.string)})
  df = pd.DataFrame(output, columns=["Date", "Requested times"])
  df["Date"] = df["Date"].astype(str)
  df['Date'] = pd.to_datetime(df['Date'])
  return df

print(getQ03_1('MANTENIMIENTO CENTROS SANITARIOS'))


#TODO: Ver como seleccionar los 10 productos por dia
print()
print()
print("INICIO QUERY 04: Top 10: Lista de los productos mas pedidos por dia")
print()
def getQ04():
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
    
      ''',
      initNs={"s": s, "ex": ex}
      )

    output = g.query(q04)
    df = pd.DataFrame(output, columns=["Date", "Product", "Quantity"])
    df["Date"] = df["Date"].astype(str)
    df['Date'] = pd.to_datetime(df['Date'])
    return df


print()
print()
print("INICIO QUERY 04_1: Dado un dia, el Top 10 de la Lista de los productos mas pedidos")
print()
def getQ04_1(date):
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

    output = g.query(q04_1, initBindings={'?date': Literal(date, datatype=s+"Date")})
    df = pd.DataFrame(output, columns=["Product", "Quantity"])
    #df["Date"] = df["Date"].astype(str)
    #df['Date'] = pd.to_datetime(df['Date'])
    return df


print(getQ04_1("2020-04-06T00:00:00Z"))
print()


#TODO: Ver como coger los 10 servicios mas pedidos por cada dia
print()
print()
print("INICIO QUERY 05: Top 10: Lista de los servicios mas pedidos por dia")
print()
def getQ05():
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

    output = g.query(q05)
    df = pd.DataFrame(output, columns=["Date", "Service", "Requested times"])
    df["Date"] = df["Date"].astype(str)
    df['Date'] = pd.to_datetime(df['Date'])
    return df


print()
print()
print("INICIO QUERY 05_1: Dado un dia, el Top 10: Lista de los servicios mas pedidos por dia")
print()
def getQ05_1(date):
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

    output = g.query(q05_1, initBindings={'?date': Literal(date, datatype=s + "Date")})
    df = pd.DataFrame(output, columns=["Service", "Requested times"])
    return df


print(getQ05_1("2020-04-22T00:00:00Z"))
print()



print()
print()
print("INICIO QUERY 06: Cantidad pendiente a lo largo del tiempo con el numero de hospitalizaciones")
print()
def getQ06():
    q06 = prepareQuery('''
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
    
      ''',
      initNs={"s": s, "ex": ex}
      )
    output = g.query(q06)
    df = pd.DataFrame(output, columns=["Date", "Number Hospitalizations", "Product", "Quantity pending"])
    df["Date"] = df["Date"].astype(str)
    df['Date'] = pd.to_datetime(df['Date'])
    return df


print()
print()
print("INICIO QUERY 06_1: Cantidad pendiente a lo largo del tiempo")
print()
def getQ06_1():
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
    
      ''',
      initNs={"s": s, "ex": ex}
      )

    output = g.query(q06_1)
    df = pd.DataFrame(output, columns=["Date", "Product", "Quantity Pending"])
    df["Date"] = df["Date"].astype(str)
    df['Date'] = pd.to_datetime(df['Date'])
    return df


print(getQ06_1())

print()
print()
print("INICIO QUERY 07: Incidencia por comunidades, Test AC, PCR, Hospitalizados y UCI")
print()

def getQ07():
    q07 = prepareQuery('''
      SELECT
        ?iso ?link ?fecha ?na ?np ?nh ?nu
      WHERE {

        ?CCAA ex:hasCovidStatus  ?CS.
        ?CCAA ex:hasISOCode ?iso.
        ?CCAA o:sameAs ?link.
        ?CS ex:numPositiveAC ?na.
        ?CS ex:numPositivePCR ?np.
        ?CS ex:numberHospitalizations ?nh.
        ?CS ex:numberUCI ?nu.
        ?CS ex:inDate ?fecha .

      }

      ORDER BY ASC(?fecha)

      ''',
                       initNs={"s": s, "ex": ex, "o": o}
                       )

    df = pd.DataFrame(g.query(q07), columns=['CCAA', 'Link', 'Date', 'AC', 'PCR', 'Hospitalizations', 'UCI'])
    df["Date"] = df["Date"].astype(str)
    df['Date'] = pd.to_datetime(df['Date'])
    return df


print(getQ07())

print()
print()
print("INICIO QUERY 07_1: Incidencia covid por comunidades en una fecha dada")
print()

def getQ07_01(date):
    # Incidencia covid por comunidades en una fecha dada
    q07_1 = prepareQuery('''
      SELECT
        ?iso ?link ?na ?np ?nh ?nu
      WHERE {


        ?CCAA ex:hasCovidStatus  ?CS.
        ?CCAA ex:hasISOCode ?iso.
        ?CCAA o:sameAs ?link.
        ?CS ex:inDate ?date.
        ?CS ex:numPositiveAC ?na.
        ?CS ex:numPositivePCR ?np.
        ?CS ex:numberHospitalizations ?nh.
        ?CS ex:numberUCI ?nu.
        ?CS ex:inDate ?fecha .

      }
      ''',
                         initNs={"s": s, "ex": ex, "o": o}
                         )
    r = g.query(q07_1, initBindings={'?date': Literal(date, datatype=s + "Date")})
    df = pd.DataFrame(r, columns=['CCAA', 'Link', 'AC', 'PCR', 'Hospitalizations', 'UCI'])
    return df
print(getQ07_01('2020-04-07T00:00:00Z'))

print()
print()
print("INICIO QUERY 08: Valores Test AC y PCR acumulados covid por comunidades")
print()


def getQ08():
    # Incidencia acumulada hasta el final de las fechas por comunidades
    q08 = prepareQuery('''
      SELECT
          ?iso ?link (SUM(?na) as ?nCount) (SUM(?np) as ?npCount) 
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
    df = pd.DataFrame(g.query(q08), columns=['CCAA', 'Link', 'AC', 'PCR'])
    return df

print(getQ08())

print()
print()
print("INICIO QUERY 09: Numero de contratos por organizacion en el total de las fechas registradas y dinero total de esos contratos")
print()


# numero de contratos por organizacion en el  total de las fechas
def getQ09():
    q09 = prepareQuery('''
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
    r = g.query(q09)
    df = pd.DataFrame(r, columns=['Company', 'Link', 'Orders', 'Benefits'])
    return df
print(getQ09())

print()
print()
print("INICIO QUERY 09_1: Numero de contratos por organizacion en una fecha y dinero total de esos contratos")
print()


def getQ09_1(date):
    # numero de contratos por organizacion en una fecha
    q09_1 = prepareQuery('''
      SELECT
        ?name ?link (COUNT(?Order) as ?orderCount) (SUM(?cost) as ?ncoste)
      WHERE {
        ?Order s:orderDate ?date.
        ?Order ex:hasOrderAmount ?cost.
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
    df = pd.DataFrame(g.query(q09_1, initBindings={'?date': Literal(date, datatype=s + "Date")}),
                      columns=['Company', 'Link', 'Orders', 'Benefits'])
    return df


print(getQ09_1('2020-04-07T00:00:00Z'))




print()
print()
print("QUERY 10: Numero de contratos en total por organizacion. Se anade: numero de contratos inacabados, el link, dinero recaudado")
#Se entiende por contrato inacabado aquel que tenga una cantidad pendiente
print()
def getQ10():
    q10 = prepareQuery('''
      SELECT
        ?name ?link (SUM(?amount) as ?totalAmount) (COUNT(?order) as ?orderCount)
      WHERE {
        ?company s:name ?name.
        ?order s:seller ?company.
        OPTIONAL { ?company o:sameAs  ?link. }
		?order ex:hasOrderAmount ?amount.
      }
      GROUP BY ?company
      ORDER BY DESC(?orderCount)
      ''',
         initNs={"s": s, "ex": ex, "o": o}
      )

    output = g.query(q10)
    df = pd.DataFrame(output, columns=["Organization", "Link", "Total Amount", "Number of contracts"])

    print()
    #notFinisehd
    q10_1 = prepareQuery('''
      SELECT
        ?name (COUNT(?order) as ?orderCount)
      WHERE {
        ?company s:name ?name.
        ?order s:seller ?company.
        ?order ex:hasProductQuantityPending ?quantity.
        FILTER(?quantity > 0).
      }
      GROUP BY ?company
      ORDER BY DESC(?orderCount)
      ''',
         initNs={"s": s, "ex": ex, "o": o}
      )

    output2 = g.query(q10_1)
    df2 = pd.DataFrame(output2, columns=["Organization", "Number of contracts not finished"])
    df_final = pd.merge(left=df, right=df2, on="Organization")

    return df_final

print(getQ10())




print()
print()
print("QUERY 11_1: Dada una organizacion, cantidad de producto y cantidad pendiente por dia SIN ESPECIFICAR PRODUCTO")
#La idea es que de aqui se calcule el porcentaje por dia de projectos satisfecho
print()
def getQ11_1(organization):
    q11_1 = prepareQuery('''
    SELECT
        ?date (SUM(?quantity) as ?nq) (SUM(?pending) as ?np)
    WHERE {
        ?order s:orderDate ?date.
        ?order s:seller ?company.
        ?company s:name ?name.
        ?order ex:hasProductQuantityPending ?pending.
        ?order ex:hasProductQuantity ?quantity.
    }
    GROUP BY ?date
    ORDER BY ?date
    ''',
       initNs={"s": s, "ex": ex, "o": o}
    )

    output = g.query(q11_1, initBindings={'?name': Literal(organization, datatype=XSD.string)})
    df = pd.DataFrame(output, columns=["Date", "Product", "Quantity", "Quantity Pending"])
    df["Date"] = df["Date"].astype(str)
    df['Date'] = pd.to_datetime(df['Date'])
	df["Contracts satisfied"] = (df["Quantity Pending"]/df["Quantity"])*100
	df.pop("Quantity")
	df.pop("Quantity Pending")
    return df

print(getQ11("MARCOM MEDICA, S.L."))




print()
print()
print("QUERY 11: Dada una organizacion, cantidad de producto y cantidad pendiente por dia ")
print()
def getQ11(organization):
    q11 = prepareQuery('''
    SELECT
        ?date ?product (SUM(?quantity) as ?nq) (SUM(?pending) as ?np)
    WHERE {
        ?order s:orderDate ?date.
        ?order s:seller ?company.
        ?company s:name ?name.
        ?order s:orderedItem ?pr.
        ?pr s:name ?product.
        ?order ex:hasProductQuantityPending ?pending.
        ?order ex:hasProductQuantity ?quantity.
    }
    GROUP BY ?date ?pr
    ORDER BY ?date ?product
    ''',
       initNs={"s": s, "ex": ex, "o": o}
    )

    output = g.query(q11, initBindings={'?name': Literal(organization, datatype=XSD.string)})
    df = pd.DataFrame(output, columns=["Date", "Product", "Quantity", "Quantity Pending"])
    df["Date"] = df["Date"].astype(str)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

print(getQ11("MARCOM MEDICA, S.L."))



print()
print()
print("QUERY 12: Dada una organizacion, evolucion temporal de los contratos")
print()
def getQ12(organization):
    q12 = prepareQuery('''
    SELECT
        ?date (COUNT(?order) as ?nContracts)
    WHERE {
        ?order s:orderDate ?date.
        ?order s:seller ?company.
        ?company s:name ?name.
    }
    GROUP BY ?date 
    ORDER BY ?date 
    ''',
       initNs={"s": s, "ex": ex, "o": o}
    )

    output = g.query(q12, initBindings={'?name': Literal(organization, datatype=XSD.string)})
    df = pd.DataFrame(output, columns=["Date", "Number of contracts"])
    df["Date"] = df["Date"].astype(str)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

print(getQ12("MARCOM MEDICA, S.L."))
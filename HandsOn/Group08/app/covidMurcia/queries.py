# -*- coding: utf-8 -*-
import pandas as pd
from rdflib import Graph, Namespace, Literal, XSD
from rdflib.plugins.sparql import prepareQuery


desired_width = 320
pd.set_option("display.max_columns", 20)
pd.set_option("display.width", desired_width)

g = Graph()
g.parse("data/output-with-links.nt", format="nt")


s = Namespace("http://schema.org/")
ex = Namespace("http://www.publicProcurementMurciaCOVID19.es/ontology#")
o= Namespace("http://www.w3.org/2002/07/owl#")



#print("INICIO QUERY 01: Productos mas pedidos y su cantidad")



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
      LIMIT 10
      ''',
                     initNs={"s": s, "ex": ex}
                     )
  output = g.query(q01)
  df = pd.DataFrame(output, columns=["Product", "Quantity"])
  return df


#print("INICIO QUERY 02: Servicios mas pedidos y el numero de veces pedidos")


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




#print("INICIO QUERY 03: Dado un producto (NAME), ver evoluacion temporal de la cantidad pedida y lo que falta")



# uriProduct type String
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


#print(getQ03("GUANTE VINILO"))

#print(getQ03("GUANTES DE NITRILO, CON Y SIN POLVO"))

# TODO: Ver como seleccionar los 10 productos por dia


#print("INICIO QUERY 04: Top 10: Lista de los productos mas pedidos por dia")



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




#print("INICIO QUERY 04_1: Dado un dia, el Top 10 de la Lista de los productos mas pedidos")



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

  output = g.query(q04_1, initBindings={'?date': Literal(date, datatype=s + "Date")})
  df = pd.DataFrame(output, columns=["Product", "Quantity"])
  # df["Date"] = df["Date"].astype(str)
  # df['Date'] = pd.to_datetime(df['Date'])
  return df


#print(getQ04_1("2020-04-06T00:00:00Z"))


# TODO: Ver como coger los 10 servicios mas pedidos por cada dia


#print("INICIO QUERY 05: Top 10: Lista de los servicios mas pedidos por dia")



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




#print("INICIO QUERY 05_1: Dado un dia, el Top 10: Lista de los servicios mas pedidos por dia")



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


#print(getQ05_1("2020-04-22T00:00:00Z"))




#print("INICIO QUERY 06: Cantidad pendiente a lo largo del tiempo con el numero de hospitalizaciones")



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
  df["Quantity pending"] = df["Quantity pending"].astype(str)
  df['Quantity pending'] = pd.to_numeric(df['Quantity pending'])
  df = df.groupby(by=["Date", "Number Hospitalizations"]).sum()
  df.reset_index(inplace=True)
  return df




#print("INICIO QUERY 06_1: Cantidad pendiente a lo largo del tiempo")



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


#print(getQ06_1())



#print("INICIO QUERY 07: Incidencia por comunidades, Test AC, PCR, Hospitalizados y UCI")



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


#print(getQ07())



#print("INICIO QUERY 07_1: Incidencia covid por comunidades en una fecha dada")



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


#print(getQ07_01('2020-04-07T00:00:00Z'))



#print("INICIO QUERY 08: Valores Test AC y PCR acumulados covid por comunidades")



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


#print(getQ08())



#print("INICIO QUERY 09: Numero de contratos por organizacion en el total de las fechas registradas y dinero total de esos contratos")



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


#print(getQ09())



#print("INICIO QUERY 09_1: Numero de contratos por organizacion en una fecha y dinero total de esos contratos")



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


#print(getQ09_1('2020-04-07T00:00:00Z'))



#print("QUERY 10: Numero de contratos en total por organizacion. Se anade: numero de contratos inacabados y el link")
# Se entiende por contrato inacabado aquel que tenga una cantidad pendiente



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




#print("QUERY 11: Dada una organizacion, cantidad de producto y cantidad pendiente por dia ")



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
  df["Quantity"] = df["Quantity"].astype(str)
  df['Quantity'] = pd.to_numeric(df['Quantity'])
  return df

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

def getQuantityTopProducts():
    df = pd.DataFrame(columns=["Product","Date", "Quantity", "Quantity Pending"])
    for i in getQ01()["Product"]:
        dfi=getQ03(i)
        dfi["Product"]=i
        df=pd.concat([df, dfi])
    return df

def getQuantityTopServices():
    df = pd.DataFrame(columns=["Service","Date", "Order Amount", "Pending Amount"])
    for i in getQ02()["Service"]:
        dfi=getQ03_1(i)
        dfi["Service"]=i
        df=pd.concat([df, dfi])
    return df

def getQuantityTopOrganizations():
    df = pd.DataFrame(columns=["Organization", "Date", "Number of contracts"])
    for i in getQ10()["Organization"]:
        dfi=getQ12(i)
        dfi["Organization"]=i
        df=pd.concat([df, dfi])
    return df

def getQuantityTopOrganizationsProjects():
    df = pd.DataFrame(columns=["Date", "Contracts satisfied"])
    for i in getQ10()["Organization"]:
        dfi=getQ11_1(i)
        df=pd.concat([df, dfi])
    df = df.groupby(by=["Date"]).mean()
    df.reset_index(inplace=True)
    return df

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
    df = pd.DataFrame(output, columns=["Date", "Quantity", "Quantity Pending"])
    df['Quantity']=pd.to_numeric(df['Quantity'])
    df['Quantity Pending']=pd.to_numeric(df['Quantity Pending'])
    df["Contracts satisfied"] = (100-(df["Quantity Pending"]/df["Quantity"])*100)
    df.pop("Quantity")
    df.pop("Quantity Pending")
    df["Date"] = df["Date"].astype(str)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

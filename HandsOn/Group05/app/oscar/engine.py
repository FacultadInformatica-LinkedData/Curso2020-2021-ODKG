import rdflib
from rdflib import Graph, Namespace
from rdflib.plugins.sparql import prepareQuery
from rdflib.plugins.sparql.results.jsonresults import JSONResultSerializer
import sys


def unique(list1):
    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    for x in unique_list:
        print(x)


g = Graph()
g.parse("../static/data/data.nt", format="nt")


VCARD = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
selfVCARD = Namespace("http://contsem.unizar.es/def/sector-publico/pproc#")
sVCard = Namespace("http://eit-upm-opendata.com/ted/")
universalContract = Namespace("http://contsem.unizar.es/def/sector-publico/pproc#")

q = prepareQuery('''
              SELECT 
                ?predictor ?object
                WHERE { 
                vcard:%s ?predict ?object.
              } 
              '''%("20184427"),
                 initNs={"vcard":  Namespace("https://eit-opendata.arken-cloud.ir/contract/notice/")
                         }
        )

majid = g.query(q)

eleDic = {}
for row in majid:
  # predicate = (str(row[0]).split("#"))[1]
  # object = str(row[1])
  # eleDic[predicate] = object
  print(row)

# print(eleDic)
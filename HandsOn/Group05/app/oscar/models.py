import urllib

import rdflib
from django.db import models
from rdflib import Graph, Namespace
from rdflib.plugins.sparql import prepareQuery

class Country:
    def __init__(self, query, name):
        eleDic = {}
        for row in query:
            predicate = (str(row[0]).split("#"))[1]
            object = str(row[1])
            eleDic[predicate] = object
        self.name = name
        self.wikidataLink = eleDic.get('sameAs', None)
        self.type = eleDic.get('type', None)

class Locality:
    def __init__(self, query, name):
        eleDic = {}
        for row in query:
            predicate = (str(row[0]).split("#"))[1]
            object = str(row[1])
            eleDic[predicate] = object
        self.name = name
        self.wikidataLink = eleDic.get('sameAs', None)
        self.type = eleDic.get('type', None)


class ContractNotice:
    def __init__(self, query, id):
        eleDic = {}
        for row in query:
            predicate = (str(row[0]).split("#"))[1]
            object = str(row[1])
            eleDic[predicate] = object
        self.id = id
        self.hasContractType = eleDic['hasContractType']
        self.mainObject = float(eleDic['mainObject'])
        self.hasPriceSpecification = eleDic['hasPriceSpecification']
        self.contractActivities = eleDic['contractActivities']
        self.isCancelled = self.boolDetector(eleDic['isCancelled'])
        self.duration = float(eleDic['duration'])
        self.contractingAuthority = eleDic['contractingAuthority']
        self.contractingAuthorityId = (eleDic['contractingAuthority'].split("/"))[-1]
        self.type = eleDic['type']
        self.hasIDType = int(eleDic['hasIDType'])
        self.procedureType = eleDic['procedureType']
        self.isEUFunded = self.boolDetector(eleDic['isEUFunded'])
        self.hasMultipleCAE = self.boolDetector(eleDic['hasMultipleCAE'])
        self.isElectronic = self.boolDetector(eleDic['isElectronic'])
        self.isGPA = self.boolDetector(eleDic['isGPA'])
        self.noticeDate = self.boolDetector(eleDic['noticeDate'])

    def boolDetector(self, booleanVariable):
        if booleanVariable == 'false':
            return False
        else:
            return True

class ContractBodeis:
    def __init__(self, query, id):
        eleDic = {}
        for row in query:
            if str(row[0]).find("#") > -1:
                predicate = (str(row[0]).split("#"))[1]
            else:
                predicate = (str(row[0]).split("/"))[-1]
            object = str(row[1])
            eleDic[predicate] = object
        self.id = id
        self.informationKind = eleDic.get('informationKind', '')
        self.addressCountry = eleDic['addressCountry']
        self.country = (eleDic['addressCountry'].split("/"))[-1]
        self.hasNationalID = eleDic['hasNationalID']
        self.addressLocality = eleDic['addressLocality']
        self.town = (eleDic['addressLocality'].split("/"))[-1]
        self.type = eleDic['type']
        self.name = eleDic['name']

class RDFStore:
    def __init__(self):
        self.g = Graph()
        self.g.parse("static/data/data.nt", format="nt")

        self.ownNamespaceContractNotice = Namespace("https://eit-opendata.arken-cloud.ir/contract/notice/")
        self.w3Namespace = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
        self.universalContract = Namespace("http://contsem.unizar.es/def/sector-publico/pproc#")
        self.ownNamespaceContractBodies = Namespace("https://eit-opendata.arken-cloud.ir/contract/body/")

    def allData(self):
        q = prepareQuery('''
        SELECT ?subject ?predicate ?object
        WHERE {?subject ?predicate ?object} 
        LIMIT 100
        ''')
        queryResult = self.g.query(q)
        return queryResult

    def getAllContractNotices(self, procedureType = None, contractType=None):
        procedureTypeQuery = ''
        contractTypeQuery= ''

        if procedureType != None and procedureType != "":
            procedureTypeQuery = "?subject ptcard:procedureType ?ptterm."

        if contractType != None and contractType != "":
            contractTypeQuery = "?subject ctcard:hasContractType ?ctterm."

        q = prepareQuery('''
              SELECT 
                ?subject
                WHERE { 
                ?subject vcard:type scard:ContractNotice.
                %s
                %s
              } LIMIT 100
          '''%(procedureTypeQuery, contractTypeQuery),
         initNs = { "vcard": self.w3Namespace,
                    "scard":self.universalContract,
                    "ptcard": Namespace("http://contsem.unizar.es/def/sector-publico/pproc#"),
                    "ctcard": Namespace("http://eit-upm-opendata.com/ted#")}
         )
        result = []
        queryResult = self.g.query(q, initBindings = {'ptterm' : rdflib.term.Literal(procedureType),
                                                      'ctterm' : rdflib.term.Literal(contractType)})
        for noticeTuple in queryResult:
            noticeId = (noticeTuple[0].split("/"))[-1]
            notice = self.getContractNotice(noticeId)
            result.append(notice)
        return result

    def getAllContractBodies(self, name):
        nameQuery = ''
        if name != None and name != "":
            nameQuery = 'FILTER contains(?oname, "%s")'%(name)

        q = prepareQuery('''
              SELECT 
                ?subject
                WHERE { 
                ?subject vcard:type scard:ContractBodies.
                ?subject nameCard:name ?oname .
                %s
              } LIMIT 100
          '''%(nameQuery),
         initNs = { "vcard": self.w3Namespace,
                    "scard":self.universalContract,
                    "nameCard" : Namespace("http://schema.org/")
                    }
         )
        queryResult =  list(self.g.query(q))
        result = []
        for caeTuple in queryResult:
            caeId = (caeTuple[0].split("/"))[-1]
            notice = self.getContractBodies(caeId)
            result.append(notice)
        return result

    def getContractNotice(self, contractId):
        q = prepareQuery('''
              SELECT 
                ?predict ?object
                WHERE { 
                vcard:%s ?predict ?object.
              } 
              '''%(contractId),
            initNs = { "vcard": self.ownNamespaceContractNotice}
        )
        return ContractNotice(self.g.query(q), contractId)

    def getContractBodies(self, contractId):
        q = prepareQuery('''
              SELECT 
                ?predict ?object
                WHERE { 
                vcard:%s ?predict ?object.
              } 
              '''%(contractId),
            initNs = { "vcard": self.ownNamespaceContractBodies}
        )
        return ContractBodeis(self.g.query(q), contractId)

    def getCountry(self, link):
        countryName = (link.split("/"))[-1]
        countryName = urllib.parse.quote(countryName, safe='')
        q = prepareQuery('''
                             SELECT 
                                ?predict ?object
                                WHERE { 
                                vcard:%s ?predict ?object.
                              }
                         ''' % (countryName),
                         initNs={"vcard": Namespace("https://eit-opendata.arken-cloud.ir/country/")}
                         )
        return Country(self.g.query(q), countryName)

    def getCAEofCountry(self, countryName):
        cn = str(urllib.parse.quote(countryName, safe=''))
        print(cn)
        q = prepareQuery('''
                         SELECT 
                            ?subject
                            WHERE { 
                            ?subject scard:addressCountry vcard:%s.
                          } LIMIT 50
                         ''' % (cn),
                         initNs={"scard": Namespace("http://schema.org/"),
                             "vcard": Namespace("https://eit-opendata.arken-cloud.ir/country/")
                                 }
                         )
        queryResult = self.g.query(q)
        return list(map(lambda x: self.getContractBodies((str(x[0]).split("/"))[-1]) , queryResult))

    def getCAEofTown(self, townName):
        q = prepareQuery('''
                         SELECT 
                            ?subject
                            WHERE { 
                            ?subject scard:addressLocality vcard:%s.
                          } LIMIT 50
                         ''' % (townName),
                         initNs={"scard": Namespace("http://schema.org/"),
                             "vcard": Namespace("https://eit-opendata.arken-cloud.ir/town/")
                                 }
                         )
        queryResult = self.g.query(q)
        return list(map(lambda x: self.getContractBodies((str(x[0]).split("/"))[-1]) , queryResult))

    def getLocality(self, link):
        localName = (link.split("/"))[-1]
        q = prepareQuery('''
                             SELECT 
                                ?predict ?object
                                WHERE { 
                                vcard:%s ?predict ?object.
                              }
                         ''' % (localName),
                         initNs={"vcard": Namespace("https://eit-opendata.arken-cloud.ir/town/")}
                         )
        return Locality(self.g.query(q), localName)

    def getProcedureTypes(self):
        q = prepareQuery('''
                      SELECT DISTINCT 
                        ?object
                        WHERE { 
                        ?subject scard:%s ?object.
                      } 
                      ''' % ("procedureType"),
                         initNs={"scard": Namespace("http://contsem.unizar.es/def/sector-publico/pproc#")}
                         )
        query = self.g.query(q)
        return list(map(lambda x: str(x[0]), query))

    def getContractTypes(self):
        q = prepareQuery('''
                      SELECT DISTINCT 
                        ?object
                        WHERE { 
                        ?subject scard:%s ?object.
                      } 
                      ''' % ("hasContractType"),
                         initNs={"scard": Namespace("http://eit-upm-opendata.com/ted#")}
                         )
        query = self.g.query(q)
        return list(map(lambda x: str(x[0]), query))



store = RDFStore()
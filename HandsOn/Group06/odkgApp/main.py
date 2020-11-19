from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery
from rdflib import XSD, URIRef

import numpy as np 
import matplotlib.pyplot as plt

# Declaration of the namespaces (prefixes)
ns = Namespace("http://publicprocurement.odkg.es/group06/ontology/ppg6#")
owl = Namespace("http://www.w3.org/2002/07/owl#")
pproc = Namespace("http://contsem.unizar.es/def/sector-publico/pproc#")
org = Namespace("http://www.w3.org/ns/org#")
myInitNs = { "ns" : ns, "RDFS": RDFS, "org" : org, "pproc" : pproc, "owl" : owl}

# Declaration of some constant values used during the execution
contractPrefix = "http://publicprocurement.odkg.es/group06/resource/Contract/"
dateSufix = "T00:00:00+00:00"

#####################################################
# Declaration of the queries used in the application#
#####################################################
# Menu option 1
getAllPublicOrganizations = prepareQuery('''
  SELECT DISTINCT
    ?name ?wikidataLink
  WHERE { 
    ?publicOrg a org:Organization .
    ?publicOrg <http://schema.org/name> ?name .
    ?publicOrg owl:sameAs ?wikidataLink .
  }
  ''',
  initNs = myInitNs
)

# Menu option 2
getAllPrivateOrganizations = prepareQuery('''
  SELECT DISTINCT
    ?name 
  WHERE { 
    ?privateOrg a pproc:AwardedTender.
    ?privateOrg <http://schema.org/name> ?name 
  }
  ''',
  initNs = myInitNs
)

# Menu option 3
getContractsWithParts = prepareQuery('''
  SELECT DISTINCT
    ?publiceOrgName ?contract ?privateOrgName 
  WHERE { 
    ?privateOrg a pproc:AwardedTender .
    ?privateOrg <http://schema.org/name> ?privateOrgName .
    ?publicOrg a org:Organization .
    ?publicOrg <http://schema.org/name> ?publiceOrgName .
    ?contract a pproc:Contract .
    ?contract pproc:contractingBody ?publicOrg .
    ?contract ns:contractor ?privateOrg
  }
  ''',
  initNs = myInitNs
)

# Menu option 4
getContractsOfPublicOrganization = prepareQuery('''
  SELECT DISTINCT
    ?contract ?publicOrg 
  WHERE { 
    ?contract a pproc:Contract .
    ?contract pproc:contractingBody ?publicOrg .
    ?publicOrg a org:Organization .
    ?publicOrg <http://schema.org/name> ?inputText  
  }
  ''',
  initNs = myInitNs
)

# Menu option 5
getContractsOfContractor = prepareQuery('''
  SELECT DISTINCT
    ?contract ?privateOrg 
  WHERE { 
    ?contract a pproc:Contract .
    ?contract ns:contractor ?privateOrg .
    ?privateOrg a pproc:AwardedTender .
    ?privateOrg <http://schema.org/name> ?inputText  
  }
  ''',
  initNs = myInitNs
)

# Menu option 6
getContractsByType = prepareQuery('''
  SELECT DISTINCT
    ?contract 
  WHERE { 
    ?contract a pproc:Contract .
    ?contract ns:typeOfContract ?inputText .
  }
  ''',
  initNs = myInitNs
)

# Menu option 7
getDataContractsByType = prepareQuery('''
  SELECT DISTINCT
    ?typeC (COUNT(?contract) as ?count) (AVG(?price) as ?avg) 
  WHERE { 
    ?contract a pproc:Contract .
    ?contract ns:typeOfContract ?typeC .
    ?contract ns:awardAmount ?price .
  }
  GROUP BY ?typeC
  ''',
  initNs = myInitNs
)

# Menu option 8
getDataContractsOfPublicOrganization = prepareQuery('''
  SELECT DISTINCT
    ?inputText (COUNT(?contract) as ?count) (AVG(?price) as ?avg) 
  WHERE { 
    ?contract a pproc:Contract .
    ?contract pproc:contractingBody ?publicOrg .
    ?publicOrg a org:Organization .
    ?publicOrg <http://schema.org/name> ?inputText .
    ?contract ns:awardAmount ?price .
  }
  GROUP BY ?typeC
  ''',
  initNs = myInitNs
)

# Menu option 9
getDataContractsOfContractor = prepareQuery('''
  SELECT DISTINCT
    ?inputText (COUNT(?contract) as ?count) (AVG(?price) as ?avg) 
  WHERE { 
    ?contract a pproc:Contract .
    ?contract ns:contractor ?privateOrg .
    ?privateOrg a pproc:AwardedTender .
    ?privateOrg <http://schema.org/name> ?inputText .
    ?contract ns:awardAmount ?price .
  }
  GROUP BY ?typeC
  ''',
  initNs = myInitNs
)

# Menu option 10
getContractByID = prepareQuery('''
  SELECT DISTINCT
    ?x ?y
  WHERE { 
    ?inputText a pproc:Contract .
    ?inputText ?x ?y
  }
  ''',
  initNs = myInitNs
)

# Menu option 11
getContractDescriptionByID = prepareQuery('''
  SELECT DISTINCT
    ?inputText ?description ?obj 
  WHERE { 
    ?inputText a pproc:Contract .
    ?inputText <http://purl.org/dc/terms/description> ?description .
    ?inputText ns:contractObject ?obj .
  }
  ''',
  initNs = myInitNs
)

# Menu option 12
getContractGreaterThanDate = prepareQuery('''
  SELECT DISTINCT
    ?contract ?date
  WHERE { 
    ?contract a pproc:Contract .
    ?contract ns:awardDate ?date.
    FILTER (?date > ?inputText) 
  }
  ''',
  initNs = myInitNs
)

# Menu option 12
getContractLessThanDate = prepareQuery('''
  SELECT DISTINCT
    ?contract ?date
  WHERE { 
    ?contract a pproc:Contract .
    ?contract ns:awardDate ?date.
    FILTER (?date < ?inputText) 
  }
  ''',
  initNs = myInitNs
)

# Menu option 12
getContractEqualThanDate = prepareQuery('''
  SELECT DISTINCT
    ?contract ?date
  WHERE { 
    ?contract a pproc:Contract .
    ?contract ns:awardDate ?date.
    FILTER (?date = ?inputText) 
  }
  ''',
  initNs = myInitNs
)

# Menu option 13
getContractMaxAwardAmount = prepareQuery('''
  SELECT DISTINCT
    ?contract (MAX(?price) as ?max) 
  WHERE { 
    ?contract a pproc:Contract .
    ?contract ns:awardAmount ?price .
  } 
  ''',
  initNs = myInitNs
)

# Menu option 14
getContractMinAwardAmount = prepareQuery('''
  SELECT DISTINCT
    ?contract (MIN(?price) as ?min) 
  WHERE { 
    ?contract a pproc:Contract .
    ?contract ns:awardAmount ?price .
  } 
  ''',
  initNs = myInitNs
)

# Menu option 15
getCountContractsMonth = prepareQuery('''
  SELECT DISTINCT
    ?month (COUNT(?contract) as ?numContracts) 
  WHERE { 
    ?contract a pproc:Contract .
    ?contract ns:awardDate ?date.
  } 
  GROUP BY (month(?date) AS ?month)
  ''',
  initNs = myInitNs
)

# Menu option 16
getAvgAwardAmountMonth = prepareQuery('''
  SELECT DISTINCT
    ?month (AVG(?price) as ?avgAwardAmount) 
  WHERE { 
    ?contract a pproc:Contract .
    ?contract ns:awardDate ?date .
    ?contract ns:awardAmount ?price .
  } 
  GROUP BY (month(?date) AS ?month)
  ''',
  initNs = myInitNs
)

# Menu option 17
getAvgAwardAmountPublicOrganization = prepareQuery('''
  SELECT DISTINCT
    ?publicOrgName (AVG(?price) as ?avgAwardAmount) 
  WHERE { 
    ?contract a pproc:Contract .
    ?contract ns:awardAmount ?price .
    ?contract pproc:contractingBody ?publicOrg .
    ?publicOrg a org:Organization .
    ?publicOrg <http://schema.org/name> ?publicOrgName .
  } 
  GROUP BY ?publicOrgName
  ORDER BY DESC(?avgAwardAmount)
  LIMIT 5
  ''',
  initNs = myInitNs
)


#############################
# End of queries declaration#
#############################

# Function for loading the graph with a nt file (reduced = smaller)
def init(reduced = True):
  g = Graph()
  if reduced:
    g.parse("output-updated.nt",format="nt")  
  else:
    # This option does not work because the .nt file is too big for github
    g.parse("output-updated-app",format="nt") 
  return g

# Function to run a query with default options
def runQuery(query, graph):
  queryResults = graph.query(query)
  for _ in queryResults:
    pass
  printResults(queryResults)

# Function to run a query with specific initBindings
def runQuerywithOptions(query, graph, initBindings):
  queryResults = graph.query(query, initBindings=initBindings)
  for _ in queryResults:
    pass
  printResults(queryResults)

# Function to print the results of the queries
def printResults(queryResults):
  # Get outputs names from the query
  for row in queryResults:
    keys = row.asdict().keys()
    break

  print("""
  -----------------
  START OF RESULTS:
  -----------------
  """)
  
  # Do the actual printing
  for row in queryResults:
    for key in keys:
      print(key, end = ' = ')
      print(row[key], end = ', ')
    print()

  print("""
  ---------------
  END OF RESULTS:
  ---------------
  """)
# Function to plot an histogram with the results of a query
# The query must have only 2 outputs (x, y)
def histogramQuery(query, graph, title):
  # Execute a query
  queryResults = graph.query(query)

  # Get outputs names from the query
  for row in queryResults:
    keys = row.asdict().keys()
    break
  
  # Initialize the result variable
  result = {}
  mykeys = []
  for key in keys:
    result[key] = []
    mykeys.append(key)

  # Extract and store the results in the result variable
  for row in queryResults:
    for key in keys:
      re = row.asdict()[key].toPython()
      result[key].append(re)

  # Plot the histogram with the 2 first variables of the result variable
  # Take only the first two outputs of a query
  plt.bar(result[mykeys[0]],result[mykeys[1]])
  plt.xlabel(mykeys[0])
  plt.ylabel(mykeys[1])
  plt.title(title)
  plt.show()

if __name__ == "__main__":
  g = init()

  menuOpt = True
  inputText = ""

  while(menuOpt):
    print("""
    ----------------------------------------------
    Catalonia public procurement application menu:
    ----------------------------------------------
    
    1)  List all public organizations with wikidata links
    2)  List all private organizations
    3)  List all contracts with contractingBody and contractor
    4)  List contracts from a Public Organization name
    5)  List contracts from a Contractor name
    6)  List all contracts of an specific type of contract
    7)  Get num of contracts and avg of award amount of the types of contracts
    8)  Get num of contracts and avg of award amound from a Public Organization name
    9)  Get num of contracts and avg of award amound from a Contractor name
    10) Get all the information about a contract given its ID
    11) Get the description of a contract given its ID
    12) Get all the contracts filtered by date
    13) Get the contract with the maximum award amount
    14) Get the contract with the minimum award amount
    15) Histogram with the number of contracts per month
    16) Histogram with the average of award amount per month
    17) Histogram with the average of award amount per public organization (top 5 in desc order) 

    0) Exit application
    """)

    menuOpt = input("Select from menu: ")

    if menuOpt == "1" :
      runQuery(getAllPublicOrganizations, g)

    elif menuOpt == "2" :
      runQuery(getAllPrivateOrganizations, g)

    elif menuOpt == "3" :
      runQuery(getContractsWithParts, g)

    elif menuOpt == "4" :
      inputText = input("Insert the name of the Public Organization: ")
      initBindings={'?inputText' : Literal(inputText, datatype=XSD.string)}
      runQuerywithOptions(getContractsOfPublicOrganization, g, initBindings)

    elif menuOpt == "5" :
      inputText = input("Insert the name of the Contractor: ")
      initBindings={'?inputText' : Literal(inputText, datatype=XSD.string)}
      runQuerywithOptions(getContractsOfContractor, g, initBindings)

    elif menuOpt == "6" :
      inputText = input("Insert the type of contract (Serveis, Subministraments, Obres): ")
      initBindings={'?inputText' : Literal(inputText, datatype=XSD.string)}
      runQuerywithOptions(getContractsByType, g, initBindings)
        
    elif menuOpt == "7" :
      runQuery(getDataContractsByType, g)
        
    elif menuOpt == "8" :
      inputText = input("Insert the name of the public Organization: ")
      initBindings={'?inputText' : Literal(inputText, datatype=XSD.string)}
      runQuerywithOptions(getDataContractsOfPublicOrganization, g, initBindings)

    elif menuOpt == "9" :
      inputText = input("Insert the name of the Contractor: ")
      initBindings={'?inputText' : Literal(inputText, datatype=XSD.string)}
      runQuerywithOptions(getDataContractsOfContractor, g, initBindings)

    elif menuOpt == "10":
      inputText = input("Insert the id of the contract (xxxx): ")
      initBindings={'?inputText' : URIRef(contractPrefix + inputText)}
      runQuerywithOptions(getContractByID, g, initBindings)

    elif menuOpt == "11":
      inputText = input("Insert the id of the contract (xxxx): ")
      initBindings={'?inputText' : URIRef(contractPrefix + inputText)}
      runQuerywithOptions(getContractDescriptionByID, g, initBindings)

    elif menuOpt == "12":
      inputText = input("Insert a valid date (yyyy-mm-dd): ").replace("/","-")
      inputText2 = input("Select an operator (<,>,=): ") 
      initBindings={'?inputText' : Literal(inputText+dateSufix, datatype=XSD.dateTime)}

      if ">" in inputText2:
        runQuerywithOptions(getContractGreaterThanDate, g, initBindings)

      elif "<" in inputText2:
        runQuerywithOptions(getContractLessThanDate, g, initBindings)

      elif "=" in inputText2:
        runQuerywithOptions(getContractEqualThanDate, g, initBindings)

      else:
        print(f"{inputText2} is not a valid operator, please try again")

    elif menuOpt == "13":
      runQuery(getContractMaxAwardAmount, g)

    elif menuOpt == "14":
      runQuery(getContractMinAwardAmount, g)

    elif menuOpt == "15":
      histogramQuery(getCountContractsMonth,g, "Number of contracts per month")
      
    elif menuOpt == "16":
      histogramQuery(getAvgAwardAmountMonth, g, "Average award amount per month")

    elif menuOpt == "17":
      histogramQuery(getAvgAwardAmountPublicOrganization, g, "Average award amount per public organization")

    elif menuOpt == "0":
      print("Quitting the application ....")
      menuOpt = False

    else:
      print("not a valid option, please try again")



'''
Some examples to test the program:
PublicOrg = Institut Català de la Salut (ICS)
Contractor = TACKLEN MEDICAL TECHNOLOGY SLN
ContractID = 0058
Date = 2020-07-23
Types of contract = [Serveis, Subministraments, Obres]
'''
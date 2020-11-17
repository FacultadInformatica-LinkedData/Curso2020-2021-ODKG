---
layout: default
title: Madrid Public Procurement
description: Open Data and Knowledge graphs - Group 2
---

# [Back to application](./app_main.html) 


## Looking for an specific contract

Here we have an example of looking for a contract by its ID, we can also loof for contract from a specific month,  contract type...

	SELECT ?FIELD ?VALUE
		WHERE {
			<http://MadridPublicContracts/resources/contract/202000001> ?FIELD ?VALUE
		}


### Results

**Data about the contract**

|   Property                                                  |   Value                                                                                                                      | 
|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------| 
| "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"           | "http://MadridPublicContracts/ontology/Contrato"                                                                             | 
| "http://MadridPublicContracts/ontology/hasMonth"            | "Enero"                                                                                                                      | 
| "http://MadridPublicContracts/ontology/hasExpNumber"        | "MDC/2019/00177"                                                                                                             | 
| "http://MadridPublicContracts/ontology/hasDescription"      | "espectaculo teatral quien es el sr schmitt en la sala principal del teatro del 16 de octubre al 10 de noviembre (t.espaol)" | 
| "http://MadridPublicContracts/ontology/hasContractType"     | "Servicios"                                                                                                                  | 
| "http://MadridPublicContracts/ontology/hasProcedure"        | "Negociado sin publicidad"                                                                                                   | 
| "http://MadridPublicContracts/ontology/hasArticle"          | "168"                                                                                                                        | 
| "http://MadridPublicContracts/ontology/hasSection"          | "a) apartado 2"                                                                                                              | 
| "http://MadridPublicContracts/ontology/hasContractDate"     | "2019-09-13T00:00:00Z"                                                                                                       | 
| "http://MadridPublicContracts/ontology/hasContractee"       | "http://MadridPublicContracts/resources/contractee/B82917063"                                                                | 
| "http://MadridPublicContracts/ontology/isDeal"              | "false"                                                                                                                      | 
| "http://MadridPublicContracts/ontology/unitaryAdjudication" | "false"                                                                                                                      | 

**Graph**

![Contract](./assets/contract_graph.svg)


## Contracts and contractors

Let's see some district boards and their associated contracts

	SELECT ?FIELD ?VALUE
		WHERE {
			?contract <http://MadridPublicContracts/ontology/hasContractor> ?junta.
	      	?junta <http://www.w3.org/1999/02/22-rdf-syntax-ns/type> <http://MadridPublicContracts/ontology/Junta>
		} LIMIT 50


### Results

**Some contracts and their district boards**

|                                                             |                                                                                                          | 
|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------| 
| "http://MadridPublicContracts/resources/contract/202000021" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Hortaleza"       | 
| "http://MadridPublicContracts/resources/contract/202000160" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Hortaleza"       | 
| "http://MadridPublicContracts/resources/contract/202000037" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Hortaleza"       | 
| "http://MadridPublicContracts/resources/contract/202000103" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Hortaleza"       | 
| "http://MadridPublicContracts/resources/contract/202000156" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Hortaleza"       | 
| "http://MadridPublicContracts/resources/contract/202000158" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Hortaleza"       | 
| "http://MadridPublicContracts/resources/contract/202000159" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Hortaleza"       | 
| "http://MadridPublicContracts/resources/contract/202000320" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Hortaleza"       | 
| "http://MadridPublicContracts/resources/contract/202000513" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Hortaleza"       | 
| "http://MadridPublicContracts/resources/contract/202000514" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Hortaleza"       | 
| "http://MadridPublicContracts/resources/contract/202000520" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Hortaleza"       | 
| "http://MadridPublicContracts/resources/contract/202000521" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Hortaleza"       | 
| "http://MadridPublicContracts/resources/contract/202000522" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Hortaleza"       | 
| "http://MadridPublicContracts/resources/contract/202000546" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Hortaleza"       | 
| "http://MadridPublicContracts/resources/contract/202000547" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Hortaleza"       | 
| "http://MadridPublicContracts/resources/contract/202000568" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Hortaleza"       | 
| "http://MadridPublicContracts/resources/contract/202000570" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Hortaleza"       | 
| "http://MadridPublicContracts/resources/contract/202000626" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Hortaleza"       | 
| "http://MadridPublicContracts/resources/contract/202000627" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Hortaleza"       | 
| "http://MadridPublicContracts/resources/contract/202000628" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Hortaleza"       | 
| "http://MadridPublicContracts/resources/contract/202000647" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Moncloa-Aravaca" | 
| "http://MadridPublicContracts/resources/contract/202000548" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Moncloa-Aravaca" | 
| "http://MadridPublicContracts/resources/contract/202000555" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Moncloa-Aravaca" | 
| "http://MadridPublicContracts/resources/contract/202000655" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Moncloa-Aravaca" | 
| "http://MadridPublicContracts/resources/contract/202000656" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Moncloa-Aravaca" | 
| "http://MadridPublicContracts/resources/contract/202000658" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Moncloa-Aravaca" | 
| "http://MadridPublicContracts/resources/contract/202000015" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Moratalaz"       | 
| "http://MadridPublicContracts/resources/contract/202000714" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Moratalaz"       | 
| "http://MadridPublicContracts/resources/contract/202000024" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Chamart%C3%ADn"  | 
| "http://MadridPublicContracts/resources/contract/202000025" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Chamart%C3%ADn"  | 
| "http://MadridPublicContracts/resources/contract/202000026" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Chamart%C3%ADn"  | 
| "http://MadridPublicContracts/resources/contract/202000028" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Chamart%C3%ADn"  | 
| "http://MadridPublicContracts/resources/contract/202000029" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Chamart%C3%ADn"  | 
| "http://MadridPublicContracts/resources/contract/202000153" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Chamart%C3%ADn"  | 
| "http://MadridPublicContracts/resources/contract/202000187" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Chamart%C3%ADn"  | 
| "http://MadridPublicContracts/resources/contract/202000188" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Chamart%C3%ADn"  | 
| "http://MadridPublicContracts/resources/contract/202000189" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Chamart%C3%ADn"  | 
| "http://MadridPublicContracts/resources/contract/202000190" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Chamart%C3%ADn"  | 
| "http://MadridPublicContracts/resources/contract/202000307" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Chamart%C3%ADn"  | 
| "http://MadridPublicContracts/resources/contract/202000342" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Chamart%C3%ADn"  | 
| "http://MadridPublicContracts/resources/contract/202000679" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Chamart%C3%ADn"  | 
| "http://MadridPublicContracts/resources/contract/202000713" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Chamart%C3%ADn"  | 
| "http://MadridPublicContracts/resources/contract/202000720" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Chamart%C3%ADn"  | 
| "http://MadridPublicContracts/resources/contract/202000035" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Villaverde"      | 
| "http://MadridPublicContracts/resources/contract/202000056" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Villaverde"      | 
| "http://MadridPublicContracts/resources/contract/202000077" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Villaverde"      | 
| "http://MadridPublicContracts/resources/contract/202000558" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Villaverde"      | 
| "http://MadridPublicContracts/resources/contract/202000581" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Villaverde"      | 
| "http://MadridPublicContracts/resources/contract/202000583" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Villaverde"      | 
| "http://MadridPublicContracts/resources/contract/202000669" | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Villaverde"      | 



**Graph**

![Contract](./assets/contracts_and_contractors.svg)





## Information about the contract and contractor

If you want to see the information of a contract and also the contact information of its corresponding contractor (i.e. the district board). In this example: contract 15, whose contractor is Moratalaz district board.

	SELECT ?PROP ?VAL
	WHERE {
      	{<http://MadridPublicContracts/resources/contract/202000015> ?PROP ?VAL.}
      UNION {
        <http://MadridPublicContracts/resources/contract/202000015> <http://MadridPublicContracts/ontology/hasContractor> ?junta.
      	?junta ?PROP ?VAL.
      }
	}


### Results

**Data about the contract and district board**

|                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 
|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| "http://contsem.unizar.es/def/sector-publico/pproc#awardDate" | "2019-11-27T00:00:00Z"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 
| "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"             | "http://purl.org/procurement/public-contracts#Contract"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 
| "http://MadridPublicContracts/ontology/hasMonth"              | "Enero"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 
| "http://MadridPublicContracts/ontology/hasExpNumber"          | "300/2019/01029"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 
| "http://purl.org/terms/description"                           | "cabalgata de reyes 2020"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 
| "http://MadridPublicContracts/ontology/hasContractType"       | "Servicios"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 
| "http://MadridPublicContracts/ontology/hasProcedure"          | "Abierto simplificado"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 
| "http://MadridPublicContracts/ontology/hasContractee"         | "http://MadridPublicContracts/resources/contractee/B79944864"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 
| "http://MadridPublicContracts/ontology/isDeal"                | "false"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 
| "http://purl.org/goodrelations/v1#UnitPriceSpecifications"    | "false"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 
| "http://MadridPublicContracts/ontology/hasCriteria"           | "http://purl.org/procurement/public-contracts#AwardCriterion/Pluralidad%20de%20criterios"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 
| "http://MadridPublicContracts/ontology/hasContractor"         | "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Moratalaz"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 
| "http://www.w3.org/1999/02/22-rdf-syntax-ns/type"             | "http://MadridPublicContracts/ontology/Junta"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 
| "http://MadridPublicContracts/ontology/hasSchedule"           | "De lunes a viernes de 9 a 14 horas.Los horarios especiales se especifican en cada una de las dependencias."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 
| "http://MadridPublicContracts/ontology/hasDescription"        | "Los Distritos obedecen a un proyecto de descentralizaci�n del Ayuntamiento de Madrid que tiene como objetivos acercar la prestaci�n de los servicios municipales a la ciudadan�a y promover la participaci�n de la ciudadan�a en la vida local. Los ciudadanos y ciudadanas pueden acudir a su Distrito a informarse y realizar gestiones tan diversas como reservas de matrimonios civiles, presentar reclamaciones de consumo, solicitar prestaciones de servicios sociales o realizar tr�mites relacionados con el padr�n municipal, licencias urban�sticas, v�as y espacios p�blicos, entre otros. Adem�s, los Distritos realizan actividades dirigidas a la promoci�n de la salud, la difusi�n de la cultura, la pr�ctica del deporte, apoyo a la educaci�n y en materia de inspecci�n sanitaria y comercial. Se admiten perros gu�a." | 
| "http://MadridPublicContracts/ontology/publicTransport"       | "Metro: Pavones (l�nea 9) Bus: 8, 20, 30, 32, 71, 100, 142, 144, E4"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 
| "http://MadridPublicContracts/ontology/hasRoadType"           | "CALLE"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 
| "http://MadridPublicContracts/ontology/locality"              | "http://MadridPublicContracts/resources/locality/Madrid"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 
| "http://MadridPublicContracts/ontology/province"              | "http://MadridPublicContracts/resources/province/Province%20of%20Madrid"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 
| "http://MadridPublicContracts/ontology/neighborhood"          | "http://MadridPublicContracts/resources/neighborhood/Pavones"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 
| "http://MadridPublicContracts/ontology/district"              | "http://MadridPublicContracts/resources/district/Moratalaz"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 
| "http://MadridPublicContracts/ontology/hasCoordenateX"        | "445952"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 
| "http://MadridPublicContracts/ontology/hasCoordenateY"        | "4472195"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 
| "http://MadridPublicContracts/ontology/hasEmail"              | "jmmoratalaz@madrid.es"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 
| "http://www.w3.org/2002/07/owl#sameAs"                        | "http://www.wikidata.org/entity/Q56191300"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 


## Visualize the number of contracts for each district

If you want to see some analytics, e.g. how many contracts belong to each district board, you can obtain this data and usi it to generate graphical information.

	SELECT ?Org (COUNT(?Contract) as ?Number_of_contrancts)
    WHERE {
      ?Contract <http://MadridPublicContracts/ontology/hasContractor> ?Org.
    }GROUP BY ?Org


### Results

**Data table**

|**District board**                                                                                               | **N**| 
|-----------------------------------------------------------------------------------------------------------------|------| 
| "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Moratalaz"              | "2"  | 
| "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Hortaleza"              | "20" | 
| "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Villaverde"             | "9"  | 
| "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Retiro"                 | "6"  | 
| "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Latina"                 | "10" | 
| "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Salamanca"              | "8"  | 
| "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Carabanchel"            | "16" | 
| "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Puente%20de%20Vallecas" | "6"  | 
| "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Fuencarral-El%20Pardo"  | "15" | 
| "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Arganzuela"             | "7"  | 
| "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Ciudad%20Lineal"        | "3"  | 
| "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20Centro"                      | "5"  | 
| "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Moncloa-Aravaca"        | "6"  | 
| "http://MadridPublicContracts/resources/junta/Junta%20Municipal%20del%20Distrito%20de%20Villa%20de%20Vallecas"  | "5"  | 




**Charts**

Bar chart example

![Bar chart](./assets/bar_chart.png)


## Visualize the number of emergency contracts by month

For developing this query, a regex filter was implemented to seach for contracts in which description appeared the word "emergency". This information can also be graphically represented.

	SELECT ?Month (COUNT(?Contract) as ?Number_of_contrancts)
    WHERE {
      ?Contract <http://purl.org/terms/description> ?emergency. 
      FILTER REGEX(?emergency ,"emergencia", "i").   
      ?Contract <http://MadridPublicContracts/ontology/hasMonth> ?Month.
       }GROUP BY ?Month


### Results

**Data table**

|**Month**|**N** | 
|---------|------| 
| "Enero" | "2"  | 
| "Marzo" | "1"  | 
| "Abril" | "24" | 
| "Mayo"  | "55" | 
| "Junio" | "38" | 

**Charts**

Pie chart

![Pie chart](./assets/pie_chart2.png)
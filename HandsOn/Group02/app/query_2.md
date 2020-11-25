---
layout: default
title: Madrid Public Procurement
description: Open Data and Knowledge graphs - Group 2
---

# [Back to application](./app_main.html) 

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





 
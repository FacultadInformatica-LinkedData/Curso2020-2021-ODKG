---
layout: default
title: Madrid Public Procurement
description: Open Data and Knowledge graphs - Group 2
---

# [Back](./index.html) 

* * *

# Ontology

This is the developed ontology for the selected data.

![app mock](./assets/ontology.png)

	@prefix : <http://MadridPublicContracts/ontology/> .
	@prefix owl: <http://www.w3.org/2002/07/owl#> .
	@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
	@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
	@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
	@prefix vocab: <http://vocab.linkeddata.es/datosabiertos/def/sector-publico/territorio/>.
	@prefix pc: <http://purl.org/procurement/public-contracts#> .
	@prefix t: <http://purl.org/terms/> .
	@prefix gr:	<http://purl.org/goodrelations/v1#> .
	@prefix pproc: <http://contsem.unizar.es/def/sector-publico/pproc#> .

	# Classes
	### Distrito
	:District rdf:type vocab:District

	### Barrio
	:Neighborhood rdf:type vocab:Neighborhood

	### Provincia
	:Province rdf:type vocab:Province.

	### Localidad 
	:Locality rdf:type vocab:Locality

	### Contrato
	pc:Contract rdf:type owl:Class .

	### Tipo de contrato
	pc:ContractType rdfs:subClassOf pc:Contract .

	### Contratado
	pc:Tender rdf:type owl:Class .

	### Contratante
	pc:ContractingAuthority rdf:type owl:Class .

	###Junta
	:Junta rdfs:subClassOf pc:ContractingAuthority .


	# Contract properties

	### Año 
	:hasYear rdf:type owl:DatatypeProperty ;
	             rdfs:domain pc:Contract ;
	             rdfs:range xsd:gYear.			 
	### Mes			 
	:hasMonth rdf:type owl:DatatypeProperty ;
	             rdfs:domain pc:Contract ;
	             rdfs:range xsd:gMonth.
				 
	### Numero Expediente		 
	:hasExpNumber rdf:type owl:DatatypeProperty ;
	             rdfs:domain pc:Contract ;
	             rdfs:range xsd:string.
				 
	### Descripcion Contrato 			 
	t:description rdf:type owl:DatatypeProperty ;
	             rdfs:domain pc:Contract ;
	             rdfs:range xsd:string.
				 
	### Tipo Contrato			 
	:hasContractType rdf:type owl:DatatypeProperty ;
	             rdfs:domain pc:ContractType ;
	             rdfs:range xsd:string.
				 
	### Procedimiento Adjudicacion		 
	:hasProcedure rdf:type owl:DatatypeProperty ;
	             rdfs:domain pc:Contract ;
	             rdfs:range xsd:string.
				 
	### Articulo
	:hasArticle rdf:type owl:DatatypeProperty ;
	             rdfs:domain pc:Contract ;
	             rdfs:range xsd:integer.
				 
	### Apartado		 
	:hasSection rdf:type owl:DatatypeProperty ;
	             rdfs:domain pc:Contract ;
	             rdfs:range xsd:string.
				 
	### Criterios Adjudicacion			 
	:hasCriteria rdf:type owl:DatatypeProperty ;
	             rdfs:domain pc:Contract ;
	             rdfs:range pc:AwardCriterion.
				 
	### Presupuesto Total(IVA Incluido)			 
	pproc:budgetPrice rdf:type owl:DatatypeProperty ;
	             rdfs:domain pc:Contract ;
	             rdfs:range xsd:double.
				 
	### Importe Adjudicacion (IVA Incluido)	 
	pc:actualPrice rdf:type owl:DatatypeProperty ;
	             rdfs:domain pc:Contract ;
	             rdfs:range xsd:double.
				 
	### Fecha Adjudicacion
	pproc:awardDate rdf:type owl:DatatypeProperty ;
	             rdfs:domain pc:Contract ;
	             rdfs:range xsd:dateTime.
				 
	### Acuerdo Marco			 
	:isDeal rdf:type owl:DatatypeProperty ;
	             rdfs:domain pc:Contract ;
	             rdfs:range xsd:bool.
				 
	### Ingreso/Coste Cero	 
	:isZeroCost rdf:type owl:DatatypeProperty ;
	             rdfs:domain pc:Contract ;
	             rdfs:range xsd:bool.

	### Adjudicado por precios unitarios 
	gr:UnitPriceSpecifications rdf:type owl:DatatypeProperty ;
	             	     	   rdfs:domain pc:Contract ;
	                           rdfs:range xsd:bool.

	### Organismo contratado 
	:hasContractee rdf:type owl:ObjectProperty ;
	                  rdfs:domain pc:Contract ;
	                  rdfs:range pc:Tender .

	### Nombre/Razon Social		 
	:nameSR rdf:type owl:DatatypeProperty ;
	             rdfs:domain pc:Tender ;
	             rdfs:range xsd:string.
					  
	###Organismo contratante			  
	:hasContractor rdf:type owl:ObjectProperty ;
	                  rdfs:domain pc:Contract ;
	                  rdfs:range pc:ContractingAuthority .	
					  
	### Descripcion Centro (empresa, ayuntamiento de Madrid)		 
	:orgType rdf:type owl:DatatypeProperty ;
	             rdfs:domain pc:ContractingAuthority ;
	             rdfs:range xsd:string.				  


	# Public organization properties (juntas)

	### Descripcion
	:hasDescription rdf:type owl:DatatypeProperty ;
		rdfs:domain :Junta ;
		rdfs:range xsd:string.

	### Horario
	:hasSchedule rdf:type owl:DatatypeProperty ;
		rdfs:domain :Junta ;
		rdfs:range xsd:string.

	### Transporte
	:publicTransport rdf:type owl:DatatypeProperty ;
		rdfs:domain :Junta ;
		rdfs:range xsd:string.
	### Web 
	:hasWeb rdf:type owl:DatatypeProperty ;
		rdfs:domain :Junta ;
		rdfs:range xsd:string.
	### Nombre via
	:isinRoad rdf:type owl:DatatypeProperty ;
		rdfs:domain :Junta ;
		rdfs:range xsd:string.
	### Tipo via
	:hasRoadType rdf:type owl:DatatypeProperty ;
		rdfs:domain :Junta ;
		rdfs:range xsd:string.
	### Num 
	:isinRoadNumber rdf:type owl:DatatypeProperty ;
		rdfs:domain :Junta ;
		rdfs:range xsd:integer.
	### Localidad
	:locality rdf:type owl:DatatypeProperty ;
		rdfs:domain :Junta ;
		rdfs:range :Locality.
	### Provincia
	:province rdf:type owl:DatatypeProperty ;
		rdfs:domain :Junta ;
		rdfs:range Province.
	### CP
	:pc rdf:type owl:DatatypeProperty ;
			rdfs:domain :Junta ;
			rdfs:range xsd:integer.
	### Barrio
	:neighborhood rdf:type owl:DatatypeProperty ;
		rdfs:domain :Junta ;
		rdfs:range :Neighborhood.
	###Distrito
	:district rdf:type owl:DatatypeProperty ;
		rdfs:domain :Junta ;
		rdfs:range :District.
	###Coordenada-x
	:hasCoordenateX rdf:type owl:DatatypeProperty ;
		rdfs:domain :Junta ;
		rdfs:range xsd:integer.
	###Coordenada-y
	:hasCoordenateY rdf:type owl:DatatypeProperty ;
		rdfs:domain :Junta ;
		rdfs:range xsd:integer.
	###EMAIL
	:hasEmail rdf:type owl:DatatypeProperty ;
		rdfs:domain :Junta ;
		rdfs:range xsd:string.
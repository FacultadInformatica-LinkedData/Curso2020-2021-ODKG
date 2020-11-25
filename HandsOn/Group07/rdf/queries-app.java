package com.example.demo.model;

public class Queries {
	
	
	public Queries() {
		
	}
	/*
	 * Show all contents
	 */
	public static String showAll() {	
		return "SELECT * {?s ?p ?o}";
	}
	
	public static String showAllResearchers() {
		return "SELECT ?s ?p ?o WHERE {?x <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://linkedscience.org/lsc/ns#Researcher> . ?x ?p ?o }";
	}
	
	public static String showAllOrganizations() {
		return "SELECT ?s ?p ?o WHERE {?x <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2006/vcard/ns#Organization> . ?x ?p ?o }";
	}
	
	public static String showAllProjects() {
		return "SELECT ?s ?p ?o WHERE {?x <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Project> . ?x ?p ?o }";
	}
	
	public static String showAllParticipations() {
		return "SELECT ?s ?p ?o WHERE {?x <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.example.org/group07/ontology/Participation> . ?x ?p ?o }";
	}
	
	/*
	 * Show the organizations based on the country
	 */
	public static String getOrganizations(String Country) {
		
		return  "PREFIX ns: <http://www.w3.org/2006/vcard/ns#>"
				+ "PREFIX sch: <http://schema.org/>"
				+ "SELECT DISTINCT ?x ?p ?o"
				+ " WHERE"
				+ "{"
				+ "?x <http://schema.org/addressCountry> <http://www.example.com/group07/ontology/Country/"+ Country +">." 
				+ "?x ?p ?o"
				+ "}";
	}
	
	/*
	 * Show the organizations based on the name
	 */
	public static String getOrganizationsByName(String Name) {
		
		return  "SELECT DISTINCT ?x ?p ?o " + 
				"WHERE " + 
				"{ " + 
				"  ?x <http://www.w3.org/2006/vcard/ns#organization-name> ?n." + 
				"  FILTER(regex(str(?n),'"+Name+"')) " + 
				"  ?x ?p ?o " + 
				"}";
	}
	
	/*
	 * Show the projects based on the title
	 */
	public static String getProjectsByTitle(String Name) {
		
		return  "SELECT DISTINCT ?x ?p ?o " + 
				"WHERE " + 
				"{ " + 
				"  ?x <http://purl.org/dc/terms/title> ?n. " + 
				"  FILTER(regex(str(?n),\"Cancer\")) " + 
				"  ?x ?p ?o " + 
				"}";
	}
	
	/*
	 * Show the researchers based on the name
	 */
	public static String getResearchersByName(String Name) {
		
		return  "SELECT DISTINCT ?x ?p ?o " + 
				"WHERE " + 
				"{ " + 
				"  ?x <http://xmlns.com/foaf/0.1/givenName>|<http://xmlns.com/foaf/0.1/familyName> ?n. " + 
				"  FILTER(regex(str(?n),'"+Name+"')) " + 
				"  ?x ?p ?o " + 
				"}";
	}
    
	/*
	 * Contribuction of each project 
	 */
	public static String getProjectContribution(String Contribution) {
		
		return "PREFIX foaf: <http://xmlns.com/foaf/0.1/> " + 
				"PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> " + 
				"PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> " + 
				"PREFIX ex:<http://www.example.org/group07/> " + 
				"PREFIX ns: <http://www.w3.org/2006/vcard/ns#> " + 
				"PREFIX owl: <http://www.w3.org/2002/07/owl#> " +
				"SELECT DISTINCT ?x ?p ?o" + 
				" WHERE {" + 
				" ?x <http://dbpedia.org/ontology/cost> ?cost. "+
				" FILTER (?cost >= "+Contribution+") "+
				" ?x ?p ?o "+
				"}"; 
	}
	/*
	 * Project states
	 */
	public static String getStateProject(String state) {
		
		return "PREFIX foaf: <http://xmlns.com/foaf/0.1/>" + 
				"PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>" + 
				"PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>" + 
				"PREFIX ex:<http://www.example.org/group07/>" + 
				"PREFIX ns: <http://www.w3.org/2006/vcard/ns#>" + 
				"PREFIX owl: <http://www.w3.org/2002/07/owl#>" + 
				"SELECT DISTINCT ?name " + 
				" WHERE " + 
				"{" + 
				"?x <http://www.example.com/group07/hasEnded> \"false\"^^<http://www.w3.org/2001/XMLSchema#boolean> ." + 
				"?x <http://www.example.com/group07/organization> ?z." + 
				"?z <http://www.w3.org/2006/vcard/ns#organization-name> ?name" + 
				"}"; 
	}
	
	/*
	 * Looking for researchers that works in the organization
	 */
	
	public static String getResearchersOrganization(String Organization) {
		
		return "PREFIX foaf: <http://xmlns.com/foaf/0.1/>"
				+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"
				+ "PREFIX ns: <http://www.w3.org/2006/vcard/ns#>"
				+ "PREFIX sch: <http://schema.org/>"
				+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>"
				+ "SELECT DISTINCT ?x ?p ?o " + 
				"WHERE" + 
				"{" + 
				"  ?s ns:organization-name '"+Organization+"'." + 
				"  ?x <http://schema.org/memberOf> ?s." + 
				"  ?x ?p ?o" + 
				"}";
	}
	
}

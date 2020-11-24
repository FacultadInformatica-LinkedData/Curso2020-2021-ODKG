package com.example.demo.Service;
import java.io.*;


import org.apache.jena.rdf.model.*;
import org.springframework.stereotype.Service;

import com.example.demo.model.Queries;

import org.apache.jena.query.*;

@Service
public class H2020Service {

	String filename;
	InputStream file;
	Model model;
	Queries query;
	
	String namespace = "http://192.168.0.24:9999/blazegraph/namespace/h2020/sparql";
	
	public H2020Service() {
	}
	  
	/*
	 * Show all contents
	 */
	public String showAll() throws FileNotFoundException{
		QueryExecution qexec = null;
		try {
			Query query1 = QueryFactory.create(Queries.showAll());
			qexec = QueryExecutionFactory.sparqlService(namespace, query1);
			
			ResultSet results = qexec.execSelect();
			//if no results then return  empty string
	        if(!results.hasNext())
	        	return "";
	        ByteArrayOutputStream outputStream=new ByteArrayOutputStream();
	        ResultSetFormatter.outputAsJSON(outputStream, results);  
	        return outputStream.toString();
		} catch (Exception e) {
			e.printStackTrace();
	    }finally {
	        qexec.close();
	    }
	    return "Error";
	}
	  
	public String showAllResearchers() throws FileNotFoundException{
		QueryExecution qexec = null;
		try {
			Query query1 = QueryFactory.create(Queries.showAllResearchers());
			qexec = QueryExecutionFactory.sparqlService(namespace, query1);
			
			ResultSet results = qexec.execSelect();
			//if no results then return  empty string
	        if(!results.hasNext())
	        	return "";
	        ByteArrayOutputStream outputStream=new ByteArrayOutputStream();
	        ResultSetFormatter.outputAsJSON(outputStream, results);  
	        return outputStream.toString();
		} catch (Exception e) {
			e.printStackTrace();
	    }finally {
	        qexec.close();
	    }
	    return "Error";
	}  
	  
	public String showAllOrganizations() throws FileNotFoundException{
		QueryExecution qexec = null;
		try {
			Query query1 = QueryFactory.create(Queries.showAllOrganizations());
			qexec = QueryExecutionFactory.sparqlService(namespace, query1);
			
			ResultSet results = qexec.execSelect();
			//if no results then return  empty string
	        if(!results.hasNext())
	        	return "";
	        ByteArrayOutputStream outputStream=new ByteArrayOutputStream();
	        ResultSetFormatter.outputAsJSON(outputStream, results);  
	        return outputStream.toString();
		} catch (Exception e) {
			e.printStackTrace();
	    }finally {
	        qexec.close();
	    }
	    return "Error";
	}

	public String showAllProjects() throws FileNotFoundException{
		QueryExecution qexec = null;
		try {
			Query query1 = QueryFactory.create(Queries.showAllProjects());
			qexec = QueryExecutionFactory.sparqlService(namespace, query1);
			
			ResultSet results = qexec.execSelect();
			//if no results then return  empty string
	        if(!results.hasNext())
	        	return "";
	        ByteArrayOutputStream outputStream=new ByteArrayOutputStream();
	        ResultSetFormatter.outputAsJSON(outputStream, results);  
	        return outputStream.toString();
		} catch (Exception e) {
			e.printStackTrace();
	    }finally {
	        qexec.close();
	    }
	    return "Error";
	}

	public String showAllParticipations() throws FileNotFoundException{
		QueryExecution qexec = null;
		try {
			Query query1 = QueryFactory.create(Queries.showAllParticipations());
			qexec = QueryExecutionFactory.sparqlService(namespace, query1);
			
			ResultSet results = qexec.execSelect();
			//if no results then return  empty string
	        if(!results.hasNext())
	        	return "";
	        ByteArrayOutputStream outputStream=new ByteArrayOutputStream();
	        ResultSetFormatter.outputAsJSON(outputStream, results);  
	        return outputStream.toString();
		} catch (Exception e) {
			e.printStackTrace();
	    }finally {
	        qexec.close();
	    }
	    return "Error";
	}

	/*
	 * Show the organizations based on the country
	 */
	public String getOrganizations(String Country) throws FileNotFoundException{
		QueryExecution qexec = null;
		try {
			Query query1 = QueryFactory.create(Queries.getOrganizations( Country));
			qexec = QueryExecutionFactory.sparqlService(namespace, query1);
		
			ResultSet results = qexec.execSelect();
			//if no results then return  empty string
	        if(!results.hasNext())
	        	return "";
	        ByteArrayOutputStream outputStream=new ByteArrayOutputStream();
	        ResultSetFormatter.outputAsJSON(outputStream, results);  
	        return outputStream.toString();
		} catch (Exception e) {
			e.printStackTrace();
	    }finally {
	        qexec.close();
	    }
	    return "Error";
	}
	
	/*
	 * Show the organizations based on the name
	 */
	public String getOrganizationsByName(String Name) throws FileNotFoundException{
		QueryExecution qexec = null;
		try {
			Query query1 = QueryFactory.create(Queries.getOrganizationsByName(Name));
			qexec = QueryExecutionFactory.sparqlService(namespace, query1);
		
			ResultSet results = qexec.execSelect();
			//if no results then return  empty string
	        if(!results.hasNext())
	        	return "";
	        ByteArrayOutputStream outputStream=new ByteArrayOutputStream();
	        ResultSetFormatter.outputAsJSON(outputStream, results);  
	        return outputStream.toString();
		} catch (Exception e) {
			e.printStackTrace();
	    }finally {
	        qexec.close();
	    }
	    return "Error";
	}
	
	/*
	 * Show the researchers based on the name
	 */
	public String getResearchersByName(String Name) throws FileNotFoundException{
		QueryExecution qexec = null;
		try {
			Query query1 = QueryFactory.create(Queries.getResearchersByName(Name));
			qexec = QueryExecutionFactory.sparqlService(namespace, query1);
		
			ResultSet results = qexec.execSelect();
			//if no results then return  empty string
	        if(!results.hasNext())
	        	return "";
	        ByteArrayOutputStream outputStream=new ByteArrayOutputStream();
	        ResultSetFormatter.outputAsJSON(outputStream, results);  
	        return outputStream.toString();
		} catch (Exception e) {
			e.printStackTrace();
	    }finally {
	        qexec.close();
	    }
	    return "Error";
	}
	
	/*
	 * Show the projects based on the title
	 */
	public String getProjectsByTitle(String Title) throws FileNotFoundException{
		QueryExecution qexec = null;
		try {
			Query query1 = QueryFactory.create(Queries.getProjectsByTitle(Title));
			qexec = QueryExecutionFactory.sparqlService(namespace, query1);
		
			ResultSet results = qexec.execSelect();
			//if no results then return  empty string
	        if(!results.hasNext())
	        	return "";
	        ByteArrayOutputStream outputStream=new ByteArrayOutputStream();
	        ResultSetFormatter.outputAsJSON(outputStream, results);  
	        return outputStream.toString();
		} catch (Exception e) {
			e.printStackTrace();
	    }finally {
	        qexec.close();
	    }
	    return "Error";
	}

	/*
	 * Contribution of each project 
	 */
	public String getProjectContribution(String Contribution)throws FileNotFoundException {
		QueryExecution qexec = null;
		try {
			Query query1 = QueryFactory.create(Queries.getProjectContribution(Contribution));
			qexec = QueryExecutionFactory.sparqlService(namespace, query1);
		
			ResultSet results = qexec.execSelect();
			//if no results then return  empty string
	        if(!results.hasNext())
	        	return "";
	        ByteArrayOutputStream outputStream=new ByteArrayOutputStream();
	        ResultSetFormatter.outputAsJSON(outputStream, results);  
	        return outputStream.toString();
		} catch (Exception e) {
			e.printStackTrace();
	    }finally {
	        qexec.close();
	    }
	    return "Error";
	}

	/*
	 * Looking for projects with a given status
	 */
	public String getStateProject(String state)throws FileNotFoundException {
		QueryExecution qexec = null;
		try {
			Query query1 = QueryFactory.create(Queries.getStateProject(state));
			qexec = QueryExecutionFactory.sparqlService(namespace, query1);
		
			ResultSet results = qexec.execSelect();
			//if no results then return  empty string
	        if(!results.hasNext())
	        	return "";
	        ByteArrayOutputStream outputStream=new ByteArrayOutputStream();
	        ResultSetFormatter.outputAsJSON(outputStream, results);  
	        return outputStream.toString();
		} catch (Exception e) {
			e.printStackTrace();
	    }finally {
	        qexec.close();
	    }
	    return "Error";
	}
	
	/*
	 * Looking for researchers that works in the organization
	 */
	public String getResearchersOrganization(String Organization)throws FileNotFoundException {
		QueryExecution qexec = null;
		try {
			Query query1 = QueryFactory.create(Queries.getResearchersOrganization(Organization));
			qexec = QueryExecutionFactory.sparqlService(namespace, query1);
		
			ResultSet results = qexec.execSelect();
			//if no results then return  empty string
	        if(!results.hasNext())
	        	return "";
	        ByteArrayOutputStream outputStream=new ByteArrayOutputStream();
	        ResultSetFormatter.outputAsJSON(outputStream, results);  
	        return outputStream.toString();
		} catch (Exception e) {
			e.printStackTrace();
	    }finally {
	        qexec.close();
	    }
	    return "Error";
	}

	private String execution(String queryString){
		//execution
		Query query = QueryFactory.create(queryString);
		QueryExecution qexec = QueryExecutionFactory.create(query, model) ;
		ResultSet results = qexec.execSelect() ;
		// if no results then return  empty string
		if(!results.hasNext())
			return "";
	
		// write to a ByteArrayOutputStream
		ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
		ResultSetFormatter.outputAsJSON(outputStream, results);

		// and turn that into a String
		String json = new String(outputStream.toByteArray());
		return json;
	}
}

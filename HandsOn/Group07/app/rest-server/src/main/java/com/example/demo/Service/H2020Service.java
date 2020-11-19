package com.example.demo.Service;
import java.io.*;

import org.apache.jena.rdf.model.*;
import org.apache.jena.util.FileManager;
import org.springframework.stereotype.Service;

import com.example.demo.model.Queries;

import org.apache.jena.query.*;
@Service
public class H2020Service {

	 String filename;
	    InputStream file;
	    Model model;
	    Queries query;
	  public H2020Service() {
		  /*
		  filename = "dataset.rdf";
	        // Use the FileManager to find the input file
	         file = FileManager.get().open(filename);
	         
	         if (file == null)
	             throw new IllegalArgumentException("File: "+filename+" not found");*/
	  }
	  
	   /*
	    * Show all contents
		*/
	  public String showAll() throws FileNotFoundException{
	        model =  ModelFactory.createDefaultModel();
	        model.read(new FileReader("C:\\Users\\delfi\\Documents\\MCD\\ODKG\\newhandson\\servicio\\h2020-version3\\src\\main\\resources\\dataset.rdf"),"",null);
	        String queryString =Queries.showAll();
	        return execution(queryString);
	    }
	  
	  public String showAllResearchers() throws FileNotFoundException{
	        model =  ModelFactory.createDefaultModel();
	        model.read(new FileReader("C:\\Users\\delfi\\Documents\\MCD\\ODKG\\newhandson\\servicio\\h2020-version3\\src\\main\\resources\\dataset.rdf"), "", null);
	        String queryString = Queries.showAllResearchers();
	        return execution(queryString);
	    }
	  
	  
	  public String showAllOrganizations() throws FileNotFoundException{
	        model =  ModelFactory.createDefaultModel();
	        model.read(new FileReader("C:\\Users\\delfi\\Documents\\MCD\\ODKG\\newhandson\\servicio\\h2020-version3\\src\\main\\resources\\dataset.rdf"), "", null);
	        String queryString = Queries.showAllOrganizations();
	        return execution(queryString);
	    }
	  
	  public String showAllProjects() throws FileNotFoundException{
	        model =  ModelFactory.createDefaultModel();
	        model.read(new FileReader("C:\\Users\\delfi\\Documents\\MCD\\ODKG\\newhandson\\servicio\\h2020-version3\\src\\main\\resources\\dataset.rdf"), "", null);
	        String queryString = Queries.showAllProjects();
	        return execution(queryString);
	    }
	  
	  public String showAllParticipations() throws FileNotFoundException{
	        model =  ModelFactory.createDefaultModel();
	        model.read(new FileReader("C:\\Users\\delfi\\Documents\\MCD\\ODKG\\newhandson\\servicio\\h2020-version3\\src\\main\\resources\\dataset.rdf"), "", null);
	        String queryString = Queries.showAllParticipations();
	        return execution(queryString);
	    }
	    /*
		 * Show the organizations based on the country
		 */
	  public String getOrganizations(String Country) throws FileNotFoundException{
	        model =  ModelFactory.createDefaultModel();
	        model.read(new FileReader("C:\\Users\\delfi\\Documents\\MCD\\ODKG\\newhandson\\servicio\\h2020-version3\\src\\main\\resources\\dataset.rdf"), "", null);
	        String queryString =Queries.getOrganizations(Country);
	        return execution(queryString);
	    }
	  
	    /*
		 * Contribuction of each project 
		 */
	  public String getProjectContribuction(String Contribuction)throws FileNotFoundException {
		    model =  ModelFactory.createDefaultModel();
	        model.read(new FileReader("C:\\Users\\delfi\\Documents\\MCD\\ODKG\\newhandson\\servicio\\h2020-version3\\src\\main\\resources\\dataset.rdf"),"",null);
	        String queryString =Queries.getProjectContribuction(Contribuction);
	        return execution(queryString); 
		}
	     
	    /*
		 * Looking for reserchers that works in the organization
		 */
		public String getResercherOrganization(String Organization)throws FileNotFoundException {
			model =  ModelFactory.createDefaultModel();
	        model.read(new FileReader("C:\\Users\\delfi\\Documents\\MCD\\ODKG\\newhandson\\servicio\\h2020-version3\\src\\main\\resources\\dataset.rdf"),"",null);
	        String queryString =Queries.getResercherOrganization(Organization);
	        return execution(queryString); 
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

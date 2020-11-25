package com.example.demo.control;

import org.springframework.web.bind.annotation.*;

import com.example.demo.Service.H2020Service;

import org.springframework.http.ResponseEntity;
import org.springframework.http.MediaType;


import java.io.FileNotFoundException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
@RestController
public class H2020Control {

	@Autowired
	H2020Service service;
	
	/*
	 * Show all contents
	 */
	@CrossOrigin
	@GetMapping("/all")
	public ResponseEntity<String>  showAll() throws FileNotFoundException {
		String json="";
        json = service.showAll();
        if(json.isEmpty()){
        	return new ResponseEntity<>("No Information Found", HttpStatus.NOT_FOUND);
        }
        return new ResponseEntity<>(json,HttpStatus.ACCEPTED);
    }
	
	@CrossOrigin
	@GetMapping("/researchers")
	public ResponseEntity<String>  getResearchers() throws FileNotFoundException {
		String json="";
        json = service.showAllResearchers();
        if(json.isEmpty()){
        	return new ResponseEntity<>("No Information Found", HttpStatus.NOT_FOUND);
        }
        return new ResponseEntity<>(json,HttpStatus.ACCEPTED);
    }
	
	@CrossOrigin
	@GetMapping("/organizations")
	public ResponseEntity<String>  getOrganizations() throws FileNotFoundException {
		String json="";
        json = service.showAllOrganizations();
        if(json.isEmpty()){
        	return new ResponseEntity<>("No Information Found", HttpStatus.NOT_FOUND);
        }
        return new ResponseEntity<>(json,HttpStatus.ACCEPTED);
    }
	
	@CrossOrigin
	@GetMapping("/projects")
	public ResponseEntity<String>  getProjects() throws FileNotFoundException {
		String json="";
        json = service.showAllProjects();
        if(json.isEmpty()){
            return new ResponseEntity<>("No Information Found", HttpStatus.NOT_FOUND);
        }
        return new ResponseEntity<>(json,HttpStatus.ACCEPTED);
	}
	
	@CrossOrigin
	@GetMapping("/participations")
	public ResponseEntity<String>  getParticipations() throws FileNotFoundException {
		String json="";
        json = service.showAllParticipations();
        if(json.isEmpty()){
            return new ResponseEntity<>("No Information Found", HttpStatus.NOT_FOUND);
        }
        return new ResponseEntity<>(json,HttpStatus.ACCEPTED);
    }
	
	/*
	 * Show the organizations based on the country
	 */
	 @CrossOrigin
	 @RequestMapping(value = "/organizations/{Country}", method = RequestMethod.GET, produces = MediaType.APPLICATION_JSON_VALUE)
	 public ResponseEntity<String> getOrganizationsByCountry(@PathVariable String Country )throws FileNotFoundException{
		 String json="";
	        
	     json = service.getOrganizations(Country);
	     if(json.isEmpty()){
	    	 return new ResponseEntity<>("No Organizations Found", HttpStatus.NOT_FOUND);
	     }
	     return new ResponseEntity<>(json, HttpStatus.ACCEPTED);
	 }
	 
	 /*
	 * Show the organizations based on the name
	 */
	 @CrossOrigin
	 @RequestMapping(value = "/organizations/name/{Name}", method = RequestMethod.GET, produces = MediaType.APPLICATION_JSON_VALUE)
	 public ResponseEntity<String> getOrganizationsByName(@PathVariable String Name )throws FileNotFoundException{
		 String json="";
	        
	     json = service.getOrganizationsByName(Name);
	     if(json.isEmpty()){
	    	 return new ResponseEntity<>("No Organizations Found", HttpStatus.NOT_FOUND);
	     }
	     return new ResponseEntity<>(json, HttpStatus.ACCEPTED);
	 }
	 
	 /*
	 * Show the researchers based on the name
	 */
	 @CrossOrigin
	 @RequestMapping(value = "/researchers/name/{Name}", method = RequestMethod.GET, produces = MediaType.APPLICATION_JSON_VALUE)
	 public ResponseEntity<String> getResearchersByName(@PathVariable String Name )throws FileNotFoundException{
		 String json="";
	        
	     json = service.getResearchersByName(Name);
	     if(json.isEmpty()){
	    	 return new ResponseEntity<>("No Organizations Found", HttpStatus.NOT_FOUND);
	     }
	     return new ResponseEntity<>(json, HttpStatus.ACCEPTED);
	 }
	 
	 /*
	 * Show the projects based on the title
	 */
	 @CrossOrigin
	 @RequestMapping(value = "/projects/title/{Title}", method = RequestMethod.GET, produces = MediaType.APPLICATION_JSON_VALUE)
	 public ResponseEntity<String> getProjectsByTitle(@PathVariable String Title)throws FileNotFoundException{
		 String json="";
	        
	     json = service.getProjectsByTitle(Title);
	     if(json.isEmpty()){
	    	 return new ResponseEntity<>("No Organizations Found", HttpStatus.NOT_FOUND);
	     }
	     return new ResponseEntity<>(json, HttpStatus.ACCEPTED);
	 }
    
	 /*
	  * Contribution of each project 
	  */
	 @CrossOrigin
	 @RequestMapping(value = "/projects/{Contribution}", method = RequestMethod.GET, produces = MediaType.APPLICATION_JSON_VALUE)
	 public ResponseEntity<String> getProjectContribution(@PathVariable String Contribution )throws FileNotFoundException{
		 String json="";
	        
		 json = service.getProjectContribution(Contribution);
		 if(json.isEmpty()){
			 return new ResponseEntity<>("No Project Found", HttpStatus.NOT_FOUND);
		 }
		 return new ResponseEntity<>(json, HttpStatus.ACCEPTED);
	 }
	 
	/*
	 * Status of each project 
	 */
//	 @CrossOrigin
//	 @RequestMapping(value = "/projects/{state}", method = RequestMethod.GET, produces = MediaType.APPLICATION_JSON_VALUE)
//	 public ResponseEntity<String> getStateProject(@PathVariable String state )throws FileNotFoundException{
//		 String json="";
//		 json = service.getStateProject(state);
//		 if(json.isEmpty()){
//			 return new ResponseEntity<>("No Project Found", HttpStatus.NOT_FOUND);
//		 }
//		 return new ResponseEntity<>(json, HttpStatus.ACCEPTED);
//	 }
	 
	 /*
	  * Looking for researchers that works in the organization
	  */
	  @CrossOrigin
	  @RequestMapping(value = "/researchers/{Organization}", method = RequestMethod.GET, produces = MediaType.APPLICATION_JSON_VALUE)
	  public ResponseEntity<String> getResearchersOrganization(@PathVariable String Organization )throws FileNotFoundException{
		  String json="";
		  json = service.getResearchersOrganization( Organization);
		  if(json.isEmpty()){
			  return new ResponseEntity<>("No Resercher Found By Organization", HttpStatus.NOT_FOUND);
		  }
		  return new ResponseEntity<>(json, HttpStatus.ACCEPTED);
	  }
	
}
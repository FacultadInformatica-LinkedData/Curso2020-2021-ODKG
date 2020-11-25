### Running the REST server

First run blazegraph, upload the database.rdf file and generate a namespace called h2020.

To run blazegraph:

    java -server -Xmx4g -jar blazegraph.jar

Then download the Service description file, copy the generated URI for the resource and replace it on H2020Service.java, on the field called "namespace".

After connecting with the database, run the server as a Spring Application.
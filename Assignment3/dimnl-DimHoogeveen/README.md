# ODKG - Assignment 3 

1. Get all the properties that can be applied to instances of the Politician class (<http://dbpedia.org/ontology/Politician>)

```SPARQL
PREFIX ex: <http://dbpedia.org/ontology/>

SELECT DISTINCT ?properties
WHERE
{
?x a/rdfs:subClassOf* ex:Politician .
?x ?properties ?y
}
LIMIT 100
```

- [Query result](https://es.dbpedia.org/sparql?default-graph-uri=&query=PREFIX+ex%3A+%3Chttp%3A%2F%2Fdbpedia.org%2Fontology%2F%3E%0D%0A%0D%0ASELECT+DISTINCT+%3Fproperties%0D%0AWHERE%0D%0A%7B%0D%0A%3Fx+a%2Frdfs%3AsubClassOf*+ex%3APolitician+.%0D%0A%3Fx+%3Fproperties+%3Fy%0D%0A%7D%0D%0ALIMIT+100&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)

2. Get all the properties, except rdf:type, that can be applied to instances of the Politician class


```SPARQL
PREFIX ex: <http://dbpedia.org/ontology/>

SELECT DISTINCT ?properties
WHERE
{
?x a/rdfs:subClassOf* ex:Politician .
?x ?properties ?y

FILTER( ?properties != rdf:type )
}
LIMIT 100
```

 - [Query result]( https://es.dbpedia.org/sparql?default-graph-uri=&query=PREFIX+ex%3A+%3Chttp%3A%2F%2Fdbpedia.org%2Fontology%2F%3E%0D%0A%0D%0ASELECT+DISTINCT+%3Fproperties%0D%0AWHERE%0D%0A%7B%0D%0A%3Fx+a%2Frdfs%3AsubClassOf*+ex%3APolitician+.%0D%0A%3Fx+%3Fproperties+%3Fy%0D%0A%0D%0AFILTER%28+%3Fproperties+%21%3D+rdf%3Atype+%29%0D%0A%7D%0D%0ALIMIT+100&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)

3. Which different values exist for the properties, except for rdf:type, applicable to the instances of Politician?


```SPARQL
PREFIX ex: <http://dbpedia.org/ontology/>

SELECT DISTINCT ?values
WHERE
{
?x a/rdfs:subClassOf* ex:Politician .
?x ?properties ?values

FILTER( ?properties != rdf:type )
}
LIMIT 100
```

- [Query result](https://es.dbpedia.org/sparql?default-graph-uri=&query=PREFIX+ex%3A+%3Chttp%3A%2F%2Fdbpedia.org%2Fontology%2F%3E%0D%0A%0D%0ASELECT+DISTINCT+%3Fvalues%0D%0AWHERE%0D%0A%7B%0D%0A%3Fx+a%2Frdfs%3AsubClassOf*+ex%3APolitician+.%0D%0A%3Fx+%3Fproperties+%3Fvalues%0D%0A%0D%0AFILTER%28+%3Fproperties+%21%3D+rdf%3Atype+%29%0D%0A%7D%0D%0ALIMIT+100&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)

4. For each of these applicable properties, except for rdf:type, which  different values do they take globally for all those instances?


```SPARQL
PREFIX ex: <http://dbpedia.org/ontology/>

SELECT DISTINCT ?properties ?values
WHERE
{
?x a/rdfs:subClassOf* ex:Politician .
?x ?properties ?values

FILTER( ?properties != rdf:type )
}
LIMIT 100
```

- [Query result](https://es.dbpedia.org/sparql?default-graph-uri=&query=PREFIX+ex%3A+%3Chttp%3A%2F%2Fdbpedia.org%2Fontology%2F%3E%0D%0A%0D%0ASELECT+DISTINCT+%3Fproperties+%3Fvalues%0D%0AWHERE%0D%0A%7B%0D%0A%3Fx+a%2Frdfs%3AsubClassOf*+ex%3APolitician+.%0D%0A%3Fx+%3Fproperties+%3Fvalues%0D%0A%0D%0AFILTER%28+%3Fproperties+%21%3D+rdf%3Atype+%29%0D%0A%7D%0D%0ALIMIT+100&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)

5. For each of these applicable properties, except for rdf:type, how many  distinct values do they take globally for all those instances?


```SPARQL
PREFIX ex: <http://dbpedia.org/ontology/>

SELECT ?properties COUNT(?values)
WHERE
{
?x a/rdfs:subClassOf* ex:Politician .
?x ?properties ?values

FILTER( ?properties != rdf:type )
}
LIMIT 100
```

- [Query result](https://es.dbpedia.org/sparql?default-graph-uri=&query=PREFIX+ex%3A+%3Chttp%3A%2F%2Fdbpedia.org%2Fontology%2F%3E%0D%0A%0D%0ASELECT+%3Fproperties+COUNT%28%3Fvalues%29%0D%0AWHERE%0D%0A%7B%0D%0A%3Fx+a%2Frdfs%3AsubClassOf*+ex%3APolitician+.%0D%0A%3Fx+%3Fproperties+%3Fvalues%0D%0A%0D%0AFILTER%28+%3Fproperties+%21%3D+rdf%3Atype+%29%0D%0A%7D%0D%0ALIMIT+100&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)
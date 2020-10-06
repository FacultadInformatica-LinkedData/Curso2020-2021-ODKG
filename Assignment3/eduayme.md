# Assignment 3
- Author: Eduard Aymerich

###################################################################
1. Get all the properties that can be applied to instances of
the Politician class (<http://dbpedia.org/ontology/Politician>)

```SPARQL
PREFIX ex: <http://dbpedia.org/ontology/>

SELECT DISTINCT ?p
WHERE
{
  ?x a/rdfs:subClassOf* ex:Politician.
  ?x ?p ?y
}
LIMIT 100
```

**[Result](https://es.dbpedia.org/sparql?default-graph-uri=&query=PREFIX+ex%3A+%3Chttp%3A%2F%2Fdbpedia.org%2Fontology%2F%3E%0D%0A%0D%0ASELECT+DISTINCT+%3Fp%0D%0AWHERE%0D%0A%7B%0D%0A++%3Fx+a%2Frdfs%3AsubClassOf*+ex%3APolitician.%0D%0A++%3Fx+%3Fp+%3Fy%0D%0A%7D%0D%0ALIMIT+100&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)**


###################################################################
2. Get all the properties, except rdf:type, that can be applied
to instances of the Politician class

```SPARQL
PREFIX ex: <http://dbpedia.org/ontology/>

SELECT DISTINCT ?p
WHERE
{
  ?x a/rdfs:subClassOf* ex:Politician.
  ?x ?p ?y
  FILTER(?p != rdf:type)
}
LIMIT 100
```

**[Result](https://es.dbpedia.org/sparql?default-graph-uri=&query=PREFIX+ex%3A+%3Chttp%3A%2F%2Fdbpedia.org%2Fontology%2F%3E%0D%0A%0D%0ASELECT+DISTINCT+%3Fp%0D%0AWHERE%0D%0A%7B%0D%0A++%3Fx+a%2Frdfs%3AsubClassOf*+ex%3APolitician.%0D%0A++%3Fx+%3Fp+%3Fy%0D%0A%0D%0A++FILTER%28%3Fp+%21%3D+rdf%3Atype%29%0D%0A%7D%0D%0ALIMIT+100&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)**


###################################################################
3. Which different values exist for the properties, except
rdf:type, of the instances of the Politician class?

```SPARQL
PREFIX ex: <http://dbpedia.org/ontology/>

SELECT DISTINCT ?v
WHERE
{
  ?x a/rdfs:subClassOf* ex:Politician.
  ?x ?p ?v
  FILTER(?p != rdf:type)
}
LIMIT 100
```

**[Result](https://es.dbpedia.org/sparql?default-graph-uri=&query=PREFIX+ex%3A+%3Chttp%3A%2F%2Fdbpedia.org%2Fontology%2F%3E%0D%0A%0D%0ASELECT+DISTINCT+%3Fv%0D%0AWHERE%0D%0A%7B%0D%0A++%3Fx+a%2Frdfs%3AsubClassOf*+ex%3APolitician.%0D%0A++%3Fx+%3Fp+%3Fv%0D%0A++FILTER%28%3Fp+%21%3D+rdf%3Atype%29%0D%0A%7D%0D%0ALIMIT+100&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)**


###################################################################
4. For each of the properties, except rdf:type, that can be
applied to instances of the Politician class, which different
values do they take in those instances?

```SPARQL
PREFIX ex: <http://dbpedia.org/ontology/>

SELECT DISTINCT ?p ?v
WHERE
{
  ?x a/rdfs:subClassOf* ex:Politician.
  ?x ?p ?v
  FILTER(?p != rdf:type)
}
LIMIT 100
```

**[Result](https://es.dbpedia.org/sparql?default-graph-uri=&query=PREFIX+ex%3A+%3Chttp%3A%2F%2Fdbpedia.org%2Fontology%2F%3E%0D%0A%0D%0ASELECT+DISTINCT+%3Fp+%3Fv%0D%0AWHERE%0D%0A%7B%0D%0A++%3Fx+a%2Frdfs%3AsubClassOf*+ex%3APolitician.%0D%0A++%3Fx+%3Fp+%3Fv%0D%0A++FILTER%28%3Fp+%21%3D+rdf%3Atype%29%0D%0A%7D%0D%0ALIMIT+100&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)**


###################################################################
5. For each of the properties, except rdf:type, that can be
applied to instances of the Politician class, how many
distinct values do they take in those instances?

```SPARQL
PREFIX ex: <http://dbpedia.org/ontology/>

SELECT DISTINCT ?p COUNT(?v)
WHERE
{
  ?x a/rdfs:subClassOf* ex:Politician.
  ?x ?p ?v
  FILTER(?p != rdf:type)
}
LIMIT 100
```

**[Result](https://es.dbpedia.org/sparql?default-graph-uri=&query=PREFIX+ex%3A+%3Chttp%3A%2F%2Fdbpedia.org%2Fontology%2F%3E%0D%0A%0D%0ASELECT+DISTINCT+%3Fp+COUNT%28%3Fv%29%0D%0AWHERE%0D%0A%7B%0D%0A++%3Fx+a%2Frdfs%3AsubClassOf*+ex%3APolitician.%0D%0A++%3Fx+%3Fp+%3Fv%0D%0A++FILTER%28%3Fp+%21%3D+rdf%3Atype%29%0D%0A%7D%0D%0ALIMIT+100&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)**

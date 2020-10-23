# Hands-on assignment 3 – Self assessment

## Checklist

**Every resource described in the CSV file:**

- [X] Has a unique identifier in a column (not an auto-increased integer)
- [X] Is related to a class in the ontology

**Every class in the ontology:**

- [X] Is related to a resource described in the CSV file

**Every column in the CSV file:**

- [X] Is trimmed
- [X] Is properly encoded (e.g., dates, booleans)
- [X] Is related to a property in the ontology

**Every property in the ontology:**

- [X] Is related to a column in the CSV file

## Comments on the self-assessment
_(If required)_
Added column id starting from value 1.
We tried to join several columns to form an unique identifier but there were rows with equal column values (each row with equal values represent parts of the same contract, it has the same link to plublication)
Group 10
    General
    Analysis
        - The analysis.html file does not contain the license of the dataset to be generated.
        - The resource naming strategy should use different paths for ontology resources and individuals.
        - It is not clear which benefits will be obtained from linking those data with other datasets.
    Ontology
        - Some of the classes have no properties (e.g., Seccion).
        - Instead of defining the union of Gastos and Ingresos, include a superclass of them (e.g., ApunteContable). Right now you have defined tieneCentro and you also have tieneIngresos and tieneGasto that should be inverse properties but cannot be.
        - Correct: tieneIngresos -> tieneIngreso.
    RDF generated
        - No RDF file has been delivered.
        - Some of the queries in the rdf directory are wrong.

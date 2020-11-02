Group 02
    General
    Analysis
        - You should not include together hash and slash in URIs (/#).
        - The resource naming strategy for individuals does not ensure uniqueness.
        - It is not clear which benefits will be obtained from linking those data with other datasets.
    Ontology
        - Identifiers are not numbers.
        - Why do you use gYear for years and string for months instead of gMonth?
        - Since you have represented contracts as a class, contract types should be better represented as subclasses of contract, instead of values. The same happens for the other types.
        - isDeal and isZeroCost are boolean, not strings.
        - Latitude and longitude are not strings.
    RDF generated
        - The URIs have to follow the resource naming strategy.
        - The RDF file does not use the class and property URIs defined in the ontology.
        - URIs are encoded as strings.
        - The RDF file does not contain individuals with labels.
        - The value of hasExpNumber are not numbers.
        - Empty values are inserted.
        - Review datatypes.
        - Check incorrect triples at the end of the file.

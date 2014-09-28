<h2>LD in Chronos LD architecture are defined using these namespaces:</h2>
- rdf (trying to avoid rdfs)
- skos (main usage)

Here's how divisions, subjects and terms are defined as taken from NASA-STI Subjects and Scopes.

**Divisions:**<br/>
divisions as defined in NASA-STI taxonomy

example:

    <!-- each division is a SKOS Concept -->
    
    <skos:Concept rdf:about="http://mydomain.com/divisions/engineering">
    
        <skos:definition> Includes engineering (general); communications and radar; electronics and electrical engineering;... </skos:definition>
    
        <skos:prefLabel xml:lang="en"> engineering </skos:prefLabel>
    
        <!-- URIs of narrower subjects contained in this division -->
        <skos:narrower rdf:resource="http://mydomain.com/subjects/instrumentation+and+photography#"/>
    
        <!-- URIs of synonyms resources from DBpedia, Freebase and Wikidata -->
        <skos:exactMatch rdf:resource="http://dbpedia.org/page/Engineering"/>
        <skos:exactMatch rdf:resource="http://rdf.freebase.com/ns/en.engineering"/>
    
    </skos:Concept>


**Subjects:**<br/>
subjects as defined in NASA-STI taxonomy

example:

    <!-- each subject is a SKOS Concept -->
    
    <skos:Concept rdf:about="http://mydomain.com/subjects/astronomy">
    
        <skos:definition>Includes observations of celestial bodies; astronomical instruments and techniques; radio, gamma-ray, x-ray, ultraviolet, and infrared astronomy; and astrometry.</skos:definition>
    
        <skos:prefLabel xml:lang="en"> astronomy </skos:prefLabel>
        <skos:altLabel xml:lang="en"> astronomical </skos:altLabel>
    
        <skos:editorialNote> Exhaustive Interest : Except for astrophysics, all facets of astronomy including radio and gamma-ray astronomy, observations of celestial bodies... </skos:editorialNote>
    
        <!-- URI of the division which the concept is the narrower term -->
        <skos:broader rdf:resource="http://mydomain.com/divisions/space+sciences#"/>
    
        <!-- URIs of synonyms resources (RDF) from DBpedia, Freebase and Wikidata -->
        <skos:exactMatch rdf:resource="http://dbpedia.org/page/Astronomy"/>
        <skos:exactMatch rdf:resource="https://www.wikidata.org/wiki/Q333"/>
        <skos:exactMatch rdf:resource="http://rdf.freebase.com/ns/en.astronomy"/>
    
        <!-- URIs of closely related resources (RDF) from DBpedia, Freebase and Wikidata -->
        <skos:closeMatch rdf:resource="http://rdf.freebase.com/ns/en.history_of_astronomy"/>
    
        <!-- URIs of other resources (non-RDF) related to the concept.
        For RDF format use skos:relatedMatch instead of skos:related -->
        <skos:related rdf:resource="https://www.freebase.com/m/0dc_v"/> <!-- astronomy -->
        <skos:related rdf:resource="https://www.freebase.com/m/03n1_"/> <!-- history of astronomy -->
    
    </skos:Concept>



**Terms:**<br/>
terms (keywords) as defined in NASA-STI taxonomy

example:

    <!-- each term is a SKOS Concept -->
    
    <skos:Concept rdf:about="http://mydomain.com/terms/infrared+telescopes">

        <skos:prefLabel xml:lang="en">infrared telescopes</skos:prefLabel>
        <skos:altLabel xml:lang="en">infrared telescope</skos:altLabel>

        <!-- no skos:scopeNote definition -->

        <!-- URI of the subject which the concept is the narrower term -->
        <skos:broader rdf:resource="http://mydomain.com/subjects/astronomy#"/>

        <!-- URIs of synonyms resources (RDF) from DBpedia, Freebase and Wikidata -->
        <skos:exactMatch rdf:resource="http://dbpedia.org/page/Infrared_telescope"/>
        <skos:exactMatch rdf:resource="http://rdf.freebase.com/ns/en.infrared_telescope"/>
        
        <!-- URIs of closely related resources (RDF) from DBpedia, Freebase and Wikidata -->
        <skos:closeMatch rdf:resource="http://rdf.freebase.com/ns/en.infrared"/>
        
        <!-- URIs of other resources (non-RDF) related to the concept.
        For RDF format use skos:relatedMatch instead of skos:related -->
        <skos:related rdf:resource="https://www.freebase.com/m/02qkxqz"/> <!-- infrared telescope -->
        <skos:related rdf:resource="https://www.freebase.com/m/0flvd"/> <!-- infrared astronomy -->
        <skos:related rdf:resource="https://www.freebase.com/m/03z8m"/> <!-- infrared spectroscopy -->

    </skos:Concept>


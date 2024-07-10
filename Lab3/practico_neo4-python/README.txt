ycdh6aTgFxfT9egXuqVoZM7x_YSaa04wBmIsen6JRXE
LOAD CSV WITH HEADERS FROM 'http://localhost:11001/project-2ffa1662-0b11-4da0-a228-2f7a729a71da/nodes.csv' AS line
CREATE (:PROTEIN {nodeId: line.nodeId, name:line.name, label:line.LABEL});


* import nodes and relationships. with neo4j user:

$ neo4j-admin import --nodes=nodes.csv --relationships=relations.csv


--------------

MATCH (pa:PATTERN)-[:HAS_CLUSTER]->(cl:CLUSTER) with pa, count(pa) as n return n

MATCH (pa:PATTERN)-[:HAS_CLUSTER]->(cl:CLUSTER) with pa, count(pa) as n where n>=9 return pa, n

MATCH (pa:PATTERN {name: '2C2H'})  
MATCH (pa)-[HAS_CLUSTER]->(cl:CLUSTER)
MATCH (cl)-[HAS_SITE]->(st:SITE)
return pa, cl, st



MATCH (p:PROTEIN) return count(*) as np

MATCH (pa:PATTERN)<-[:HAS_PATTERN]-(pr:PROTEIN) with pa, count(pa) as n where n=4 return pa, n


----------------------------------------------------------------------
proteins=4
* patterns with 100% of coverage.
MATCH (pa:PATTERN)<-[:HAS_PATTERN]-(pr:PROTEIN) with pa, count(pa) as n where n=4 
MATCH (pr)-[:HAS_PATTERN]->(PATTERN)
return pa, pr

* patterns with 50% of coverage.
MATCH (pa:PATTERN)<-[:HAS_PATTERN]-(pr:PROTEIN) with pa, count(pa) as n where n=2 
MATCH (pr)-[:HAS_PATTERN]->(PATTERN)
return pa, pr

----------------------------------------------------------------------

* borrar todos los nodos y relaciones:

MATCH (n) DETACH DELETE n


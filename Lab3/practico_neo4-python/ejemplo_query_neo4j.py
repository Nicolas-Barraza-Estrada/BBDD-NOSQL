#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://pypi.org/project/neo4j-driver/

pip install neo4j-driver

"""

from neo4j import GraphDatabase

def main(args):
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "123456"), encrypted=False)

    session = driver.session()
    
    person = session.run("MATCH (p:PROTEIN) return p").data()
    for row in person:
        print(row["p"]["name"])
    
    driver.close()
    return 0

"""
"""
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
    
    

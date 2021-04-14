#!/bin/bash

# Wait until Neo4j is up
while ! nc -z -w 2 neo4j 7687; do sleep 1; done;
# Run the tests
    pytest -vvv --cov-report term-missing --cov=estuary_updater tests/ && \
    flake8

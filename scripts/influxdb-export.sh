#!/bin/bash

curl -G 'http://localhost:8086/query?pretty=true' --data-urlencode "db=I1820" --data-urlencode "q=SELECT * FROM \"$1\"" > $1.json

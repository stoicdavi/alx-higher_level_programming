#!/bin/bash
# get request with some headers
curl -s -X GET "$1" -H "X-School-User-Id: 98"

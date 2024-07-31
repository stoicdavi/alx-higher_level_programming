#!/bin/bash
### sends Post request with variables to display body of response
curl "$@" -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"

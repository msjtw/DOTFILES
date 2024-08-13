#!/bin/sh

city=$1

curl -q "http://api.openweathermap.org/geo/1.0/direct?q=$city&limit=1&appid=7acaae7aee25aa7e5a5cabd98eb57132" | jq > city.json
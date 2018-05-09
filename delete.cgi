#!/usr/bin/python
import os, sys, json

userName = "Ronaldo"
splitString = os.environ['QUERY_STRING'].split('&')

index = splitString[0].split("=")
actIndex =  splitString[1].split("=")


with open('users.json', 'r') as data_file:
    data = json.load(data_file)

data_file.close()

for element in data:
    del data[index]["actionIndex"][actIndex]
    del data[index]["actions"][actIndex]
    del data[index]["descriptions"][actIndex]
    del data[index]["prioities"][actIndex]

with open('users.json', 'w') as data_file:
    json.dump(data, data_file)

print ("Content-Type: text/plain")     
print ("")

print ("")


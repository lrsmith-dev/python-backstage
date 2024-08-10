#!/usr/bin/env python3

#businessUnit, businessDivision, businessDepartment
companyHierarchy=[
    ("Engineering", "Software Engineering", "User Interface" ),
    ("Engineering", "Software Engineering", "Back end"),
    ("Engineering", "Software Engineering", "Security"),
    ("Engineering", "Site Reliability Engineering", "Observability" ),
    ("Engineering", "Site Reliability Engineering", "Networking" ),
    ("Engineering", "Site Reliability Engineering", "Databases"),
    ("Engineering", "Information Technology", "Helpdesk" ),
    ("Engineering", "Information Technology", "Back Office" ),
    ("Customer Support", "Professional Services", "APAC" ),
    ("Customer Support", "Professional Services", "AMER" ),
    ("Customer Support", "Technical Support", "First Level" ),
    ("Customer Support", "Technical Support", "Second Level" ),
    ("Security", "Enterprise", "Red team" ),
]

import pandas as pd
import random
import requests

# Get list of first names
firstNameTable = pd.read_html('https://www.ssa.gov/oact/babynames/decades/century.html')[0]
firstNames=list(firstNameTable['Males']['Name']) 
firstNames.append(list(firstNameTable['Females']['Name']))

# Get list of last names
lastNameTable = pd.read_html('https://www.thoughtco.com/most-common-us-surnames-1422656')[0]
lastNames=list(lastNameTable['Surname']) 


# Print out random list of users and their business <X>

max=25
print(f'"Business Unit", "Business Division", "Business Department", "Name", "Email"')

for i in range(0,max):
    name = random.choice(firstNames)+" "+random.choice(lastNames)
    email = name.lower().replace(" ",".") + "@my.org"

    line=', '.join(f'"{w}"' for w in random.choice(companyHierarchy)) 
    line += ', "{}", "{}"'.format(name,email)

    print(line)




# References
## Pandas - Multiindexing https://pandas.pydata.org/docs/user_guide/advanced.html
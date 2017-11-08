
import requests
from bs4 import BeautifulSoup
import re

elections = "http://historical.elections.virginia.gov/elections/"
elections += "search/year_from:1924/year_to:2016/"
elections += "office_id:1/stage:General"
resp = requests.get(elections)

soup = BeautifulSoup(resp.content, "html.parser")
e_id = soup.find_all("tr", "election_item")
ELECTION_ID = []

for t in e_id:
    year    = t.td.text
    year_id = t["id"][-5:] #get the last 5 characters (id)
    i       = [year, year_id]
    ELECTION_ID.append(i) #adding values to the list

with open("ELECTION_ID", "w") as ELECTION_ID_file:
    for line in ELECTION_ID:
        #format it like a list with space b/w values & line breaks
        ELECTION_ID_file.write(line[0] + " " + line[1] + " \n")
        print(line[0], line[1])

#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

page = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/"

for line in open("ELECTION_ID", "r"):
    array       = line.split(" ")
    year        = array[0]
    election_id = array[1]
    file_name   = year + ".csv"
    url         = page.format(election_id)

    with open(file_name, 'w') as output:
        output.write(requests.get(url).text)


import requests
from bs4 import BeautifulSoup
import re
ELECTION_ID = []

elections = "http://historical.elections.virginia.gov/elections/"
elections += "search/year_from:1924/year_to:2016/"
elections += "office_id:1/stage:General"
resp = requests.get(elections)
soup = BeautifulSoup(resp.content, "html.parser")

#decided to get href - did this before I saw "hints"
e_id = soup.select('a[href*="/elections/view/"]')
r = re.compile("view/(\d+)")

for a in e_id:
    ELECTION_ID.append(r.search(a['href']).group(1))
print (ELECTION_ID)

#finding the year
year = soup.find_all("td", class_="year first")

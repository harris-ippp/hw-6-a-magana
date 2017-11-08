#!/usr/bin/env python

import re
import pandas as pd
import numpy as np

#need to define all these variables outside of the for loop
#this will function as the foundation of the dataframe
header = pd.read_csv("1924.csv", nrows = 1).dropna(axis = 1)
d = header.iloc[0].to_dict()
df = pd.read_csv("1924.csv", index_col = 0, thousands = ",", skiprows = [1])
df.rename(inplace = True, columns = d) #renaming columns
df.dropna(inplace = True, axis = 1) #dropping unnecessary columns
df = df[["Democratic", "Republican", "Total Votes Cast"]] #only want these columns
df["Year"] = 1924

#created my own list, wasn't sure if you wanted me to use code from e1.py
all_years = ['1928', '1932', '1936', '1940', '1944',
             '1948', '1952', '1956', '1960', '1964',
             '1968', '1972', '1976', '1980', '1984',
             '1988', '1992', '1996', '2000', '2004',
             '2008', '2012', '2016']
#left out 1924 bc I already use it and it works as the foundation for looping through

for specific_year in all_years:
    filename = specific_year + ".csv"
    header = pd.read_csv(filename, nrows=1).dropna(axis=1)
    d = header.iloc[0].to_dict()
    formdf = pd.read_csv(filename, index_col = 0, thousands =",", skiprows = [1])
    formdf.rename(inplace = True, columns = d)
    formdf.dropna(inplace = True, axis = 1)
    formdf = formdf[["Democratic", "Republican", "Total Votes Cast"]]
    formdf["Year"] = int(specific_year)
    df = df.append(formdf)
    df["RepublicanShare"] = df["Republican"]/df["Total Votes Cast"]
#df at this point gives me the Republican shares in ALL counties

counties = ["Accomack County", "Albemarle County", "Alexandria City", "Alleghany County"]
#Using a forloop, go through each county to plot republican share of votes
for county in counties:
    countydf = df.loc[county]
    county_graph = countydf.plot(x = "Year",
                                 y = "RepublicanShare",
                                 legend = False,
                                 title = ("{} Vote Share").format(county))
    #getting proper pdf formatting
    pdf_name = re.sub("([A-Z])", "_\\1", county).lower().lstrip("_").replace(" ", "")
    county_graph.figure.savefig(("{}.pdf").format(pdf_name))

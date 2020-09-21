"""This is the python script for the webscapping. Use it to scrap the information from
http://www.guide2research.com/topconf/machine-learning in order to get the list of top conferences"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

from time import sleep
from random import randint


# Scrape the desired url, only one page

url = 'http://www.guide2research.com/topconf/machine-learning'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

context = soup.find("div", {"id": "ajax_content"})
tables = context.find_all("table")

# create en empty list to store the information
rows = []

for table in tables:
    # each row is the info about the conference
    row = table.find_all("tr")
    # get the h5 index, need to remove the newline. e.g., '\n240\n'
    h5_index = re.sub('\n', '', row[0].find_all("td")[1].get_text())
    # the name of the conference, remove the "newline"
    name = re.sub('\n', '', row[0].find_all("td")[3].get_text())
    # the website
    url = row[1].find_all("td")[0].find("a")["href"]
    
    rows.append([h5_index, name, url])



df=pd.DataFrame(rows,columns=['h5_index', 'Name','URL'])

df.to_csv('top_conference_ML_AI.csv',header=True)





import re
import datetime
import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Get Datetime for logging purposes
date = datetime.datetime.now()
date_time = date.strftime("%m/%d/%Y, %H:%M:%S")
print(date)

# Scrape the website for its full HTML contents
url = "https://www.eastmarcommonsorlando.com/floorplans/2bedroom/indigo/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# Find all th tags that contain the apartment number class
units = soup.find_all("th", {"class": "floorplan-detail__units__number"})
# Find all span tags that contain the apartment price class
prices = soup.find_all("td", {"class": "floorplan-detail__units__price"})

# Loop through apartments, format data into a human readable list
apartments = []
for unit in units:
    u = unit.findAll("span", string=re.compile("([0-9]+)|-{1}"))
    apt = ""
    for i in u:
       apt += i.string.strip()
    if apt != "":
        apartments.append(apt)
print(apartments)

# Loop through prices, format data into human readable list
aptPrices = []
for price in prices:
    p = price.findAll("span", string=re.compile("\$[0-9]+$"))
    for i in p:
        aptPrices.append(i.string)
print(aptPrices)

# Create list of duplicate datetimes for csv purposes
d = []
d = [date_time] * len(aptPrices)
print(d)

# Create csv, append results
with open('apartments.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerows(zip(apartments, aptPrices, d))

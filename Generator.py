__author__ = 'spoffy'

import http.client
import xml.etree.ElementTree as ET
from random import randint

conn = http.client.HTTPConnection("www.dailymail.co.uk")
conn.connect()
conn.request("GET", "/home/index.rss")
response = conn.getresponse()
response_data = response.read()

root = ET.fromstring(response_data)

titles = []

for child in root[0]:
    if child.tag == "item":
        for child2 in child:
            if child2.tag == "title":
                text = child2.text.rstrip().lstrip()
                titles.append(text)

conjunctives = ["used", ":", "could", " or ", " and ", " is "]
first_half = {}
second_half = {}

for conjunctive in conjunctives:
    first_half[conjunctive] = []
    second_half[conjunctive] = []

for title in titles:
    for conjunctive in conjunctives:
        halves = title.split(conjunctive)
        if len(halves) > 1:
            first_half[conjunctive].append(halves[0])
            second_half[conjunctive].append(halves[1])

for conjunctive in first_half:
    for phrase in first_half[conjunctive]:
        choice = second_half[conjunctive]
        for phrase2 in second_half[conjunctive]:
            print(phrase + conjunctive + phrase2)
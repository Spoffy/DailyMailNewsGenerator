__author__ = 'spoffy'

import http.client
import xml.etree.ElementTree as ET
from random import randint

conn = http.client.HTTPConnection("www.wordgenerator.net")
conn.connect()
conn.request("POST", "/application/p.php?id=nouns&type=50&spaceflag=false")
response = conn.getresponse()
random_nouns = response.read().decode(encoding="UTF-8").split(",")

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

conjunctives = [" by ", " of ", " for ", "?", "!", ".", "used to be", "has", "used", ":", "could", " or ", " and ", " is "]
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
    print("Xkcd:" + conjunctive)
    for phrase in first_half[conjunctive]:
        choice = second_half[conjunctive]
        for phrase2 in second_half[conjunctive]:
            print(phrase + conjunctive + phrase2)

for conjunctive in [" by ", " is "]:
    for phrase in first_half[conjunctive]:
        for phrase2 in random_nouns:
            print(phrase + conjunctive + "a " + phrase2)
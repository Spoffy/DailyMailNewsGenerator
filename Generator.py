__author__ = 'spoffy'

import http.client
import xml.etree.ElementTree as ET
from time import sleep
from random import choice
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

RANDOMS = []
for conjunctive in first_half:
    for phrase in first_half[conjunctive]:
        my_choice = second_half[conjunctive]
        for phrase2 in second_half[conjunctive]:
            RANDOMS.append(phrase + conjunctive + phrase2)

NAMES = [ "Duchess of Cambridge", "Brad Pitt", "Queen Elizabeth", "Google", "NSA", "Apple", "Obama", "Jennifer Lopez", "Royals", "Zac Efron", "Prince George" ]

ACTIONS = [ "spotted after", "is accompanied by", "shows off incredible", "to fund", "feels confident", "dazzles in sparkling dress," ]

OBJECTS = [ "Britain", "baby", "immigration", "pit bull", "hot body", "Nigeria", "teen mum", "underwear business", "royal family", "police officers", "glorious empire", "nostalgia" ]

PHRASE = [ "Get them out!", "There is deep love there", "My abs look a little different now", "Rule Brittania", "Poor and lazy", "They are not welcome", "Glorious empire!", "Now THATS a water cannon" ]

state = 0

def phrase_says_person():
    return "\"" + choice(PHRASE) + "\"" + " says " + choice(NAMES)

def make_title():
    if (randint(0, 4) == 1):
        return phrase_says_person()
    elif (randint(0, 4) == 1):
        return choice(RANDOMS)

    global state
    string_list = []
    for i in range(0, 1 + 2 * randint(1, 2)):
        if (state == 0):
            string_list.append(choice(NAMES))
            state = 1
        elif (state == 1):
            string_list.append(choice(ACTIONS))
            state = 2
        elif (state == 2):
            string_list.append(choice(OBJECTS))
            state = 1
    return " ".join(string_list)

while (True):
    print(make_title() + "\n")
    state = 0
    sleep(1)


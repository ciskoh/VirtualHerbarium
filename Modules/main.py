#! /usr/bin/env python3

# -*- coding: utf-8 -*-
"""main module calling all other operations to build a VirtualHerbarium"""

# ----------Settings
import wikipediaapi as wiki
import csv
import settings as st
import functions as fn
import classes as cl
from collections import OrderedDict
# import sys
# sys.path.append('/usr/local/lib/python3.6/dist-packages')
# print(" \n %s" % (sys.path))

# ---------Parameters
inputPath = '/home/matt/Dropbox/github/VirtualHerbarium/Tests/TestInputFile.csv'
# get input from csv file
inputDicList=fn.getInputAsDictionary(st.inputPath, nameCol=st.nameCol)
plantObjList=[ cl.Plant(i) for i in inputDicList]


#     lineCount = 0
#     # get list of plant names
plantNameList = list()
for row in csv_reader:
    plantNameList.append(row['PlantName'])
print(plantNameList)
breakpoint

# for each plant name
# just for testing
currentName = plantNameList[1]
print(currentName)
# get wikipedia page
wiki_wiki = wiki.Wikipedia('en')
page_py = wiki_wiki.page(currentName)
# select sections

sectionsTitle = [i.title for i in page_py.sections]

chosenTitle = "Uses"
chosenTitleIndex = sectionsTitle.index(chosenTitle)
sectionText = page_py.sections[chosenTitleIndex]

# extract relevant paragraph with scrappy

# get cabi page and save it
# extract relevant paragraph with scrappy

# get world flora and save it

# extract relevant paragraph with scrappy

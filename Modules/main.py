#! /usr/bin/env python3

# -*- coding: utf-8 -*-
"""main module calling all other operations to build a VirtualHerbarium"""

# ----------Settings
import csv
from utils import *
from collections import OrderedDict
from wikiScraping import *
# import sys
# sys.path.append('/usr/local/lib/python3.6/dist-packages')
# print(" \n %s" % (sys.path))

# ---------Parameters
inputPath = '/home/matt/Dropbox/github/VirtualHerbarium/Tests/TestInputFile.csv'
# get input from csv file
inputDicList=getInputAsDictionary(inputPath, colName=colName)
plantObjList=[ Plant(i) for i in inputDicList]
# [i.__str__() for i in plantObjList]

#     lineCount = 0
#     # get list of plant names


# just for testing
currentPlant = plantObjList[1]

# webscrapeWikipedia
currentPlantWiki=wikiTextContainer("wikipedia", currentPlant.name, wikiSectionTitles )
currentPlantWiki.webscrapeWikipedia()


# get wikipedia page
def checkBeforeScraping(wikiText):
    for i in ['journalName', 'plantName', 'sectionTitles']:
        assert(getattr(wikiText, i )), f"{i} is still missing, cannot scrape wikipedia"

checkBeforeScraping(wikiText)
i=wikiText.plantName

wiki_wiki = wiki.Wikipedia('en')
page_py = wiki_wiki.page(wikiText.plantName)
# select sections

sectionsTitle = [i.title for i in page_py.section]
a= page_py.sections[-3]
c=(a.text)
dir(page_py)

chosenTitle = "Uses"
chosenTitleIndex = sectionsTitle.index(chosenTitle)
sectionText = page_py.sections[chosenTitleIndex]

# extract relevant paragraph with scrappy

# get cabi page and save it
# extract relevant paragraph with scrappy

# get world flora and save it

# extract relevant paragraph with scrappy

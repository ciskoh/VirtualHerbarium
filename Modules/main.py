# !/usr/bin/env python3

# -*- coding: utf-8 -*-
"""main module calling all other operations to build a VirtualHerbarium"""
#----------Settings
import sys
sys.path.append('/usr/local/lib/python3.6/dist-packages')
print(sys.path)
import csv
import wikipediaapi as wiki
# ---------Parameters
inputPath = '/home/matt/Dropbox/github/VirtualHerbarium/Tests/TestInputFile.csv'
#get input from csv file
with open(inputPath) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    lineCount = 0
    # get list of plant names
    plantNameList=list()
    for row in csv_reader:
        plantNameList.append(row['PlantName'])
print(plantNameList)


#for each plant name
currentName=plantNameList[1]
print(currentName)
    # get wikipedia page and save it
wiki_wiki = wiki.Wikipedia('en')
page_py = wiki_wiki.page(currentName)
dir(page_py.__dict__)
sectionsTitle = [i.title for i in page_py.sections]
print(sectionsTitle)
print(page_py.sections[0].title)
    #extract relevant paragraph with scrappy

    #get cabi page and save it
    #extract relevant paragraph with scrappy

    #get world flora and save it

    #extract relevant paragraph with scrappy

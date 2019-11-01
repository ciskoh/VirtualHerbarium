"""this module holds the main settings, classes and functions \n is imported by all other modules"""
#! /usr/bin/env python3
import csv
import sys
from collections import OrderedDict
import datetime
import wikipediaapi as wiki

#------------------Settings

# General Settings
    # input (path to csv)
inputPath = '/home/matt/Dropbox/github/VirtualHerbarium/Tests/TestInputFile.csv'
    # column in input file holding plant names
colName = 'PlantName'
    # output folder path
outputPath="/tmp"

# wikipedia Settings
    # section titles to scrape
wikiSectionTitles = ["Summary", "Description", "Uses"]

attrList = ["journalName", "plantName", "sectionTitles"]
#------------------functions

def getInputAsDictionary(inputPath, colName=colName):
    """read csv file and output a standard dictionary performing some checks"""
    with open(inputPath) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        finalDic = list()
        #test if input is good
        for row in csv_reader:
            try:
                row[colName]
            except KeyError:
                print("no PlantName column in input file %s" % inputPath)
                return
            assert(row[colName] != ""), "missing p§lant name!"
            # transform output to standard dictionary
            normalDic=dict(OrderedDict(row))
            finalDic.append(normalDic)
        return(finalDic)

#------------------Classes
class Plant:
    """Class for plant objects to be filled with text from the web"""

    type = "plant"

    def __init__(self, nameOrDic=None):
        if type(nameOrDic) is dict:
            for k, v in nameOrDic.items():
                setattr(self, k, v)
            print("added attributes from dictionary: %s" % self.__dict__)
            key, value = next(iter(nameOrDic.items()))
            self.name = value
            # TODO: add checks to name Variable as property?
        elif type(nameOrDic) is str:
            self.name = nameOrDic
            # TODO: add checks to name Variable as property?
        else:
            self.name = "name not defined"

    def __str__(self):
        attrDict = str(self.__dict__)
        return f'plant object named {self.name} with the following attributes {attrDict}'


class TextContainer:
    """class holding text and data from each website"""

    def __init__(self, journalName=None, plantName=None, sections=None):
        self.date = datetime.datetime.now()
        self.journalName = journalName
        self.plantName = plantName
        if sections:
            self.sectionTitles = sections
            self.sectionContents = [
                str(i) + ": content not yet set!" for i in sections]
        else:
            self.sectionTitles = None
            self.sectionContents = None

    def __str__(self):
        attrDict = str(self.__dict__)
        return f'TextContainer object named {self.journalName} with the following attributes {attrDict}'

    def checkForMainAttr(self, attrList=attrList):
        """checks for main attributes before scraping webpage"""
        for i in attrList:
            assert(getattr(self, i)), f"{i} is still missing, cannot scrape wikipedia"



if __name__ == "__main__":
    print(getInputAsDictionary(inputPath, colName=colName))

    # class Plant tests
    print("test with object from str " + Plant('testClassPlant').__str__())
    tDic = {"rer": "balbla", "der": 2}
    print("test with object from dict " + Plant(tDic).__str__())
    print("test with no inputs " + Plant().__str__())
    # class TextContainer
    tSecs = ["aa", "bb", "cc"]
    test3 = TextContainer("wikipedia", "Lablab purpureus", tSecs)
    test3.__dict__
    plantName="dddurpureus"
    test3.webscrapeWikipedia()
    print(test3.wikiPage)
    self=test3

#! /usr/bin/env python3

# -*- coding: utf-8 -*-

""" Module to scrape World Flora online"""

# ------------------SETTINGS
from utils import Scraper
from utils import floraTitles
from utils import outputFold
from utils import pathToScrapySpider

import os

# ---------------CLASSES


class floraScraper(Scraper):
    """class holding input variables and retrieving
    results from World FLora Online using scrapy through command line"""

    pathToScrapySpider = pathToScrapySpider

    def test(self):
        print(self.name)

    def createScrapyCall(self):
        self.createOutputPath()
        stringStart = f'scrapy runspider {pathToScrapySpider} '
        string1 = f'-a plantName="{self.plantName}" '
        string2 = f'-a tempFileDump="{self.outputPath}" '
        string3 = f'-a titles="{floraTitles}"'

        spyderCall=stringStart+string1+string2+string3
        print(spyderCall)
        # os.system(spyderCall)

    def createOutputPath(self, baseFolder=outputFold):
        token = str(self.timeStamp)
        pn = self.plantName.replace(" ", "-")
        path = os.path.join(baseFolder, "VirtHerb" + token, pn)
        os.makedirs(path, mode=0o777, exist_ok=True)
        self.outputPath = os.path.join(path, "flora.xml")


# -------------FUNCTIONS--------------
# define string with names of plant

# call external command with scrapy string
#


# -------------CODE--------------


# run spyder

# collect response
if __name__ == "__main__":

    # test class name
    a = floraScraper(journalName="flora", plantName="Parthenium hysterophorus")
    b = a.timeStamp
    str(object=b)
    a.createOutputPath()
    a.createScrapyCall()
    # call spyder with command line

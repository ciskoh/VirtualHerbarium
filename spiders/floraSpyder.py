# -*- coding: utf-8 -*-

import scrapy
import os
import xml.etree.ElementTree as ET
# import settings.floraTitles as floraTitles


class FloraSpider(scrapy.Spider):
    name = 'flora'
    allowed_domains = ['www.worldfloraonline.org']
    BASE_URL = 'http://www.worldfloraonline.org'
    searchPrefix = 'search?query='
    outputStr = "nothing here"

    def __init__(self, plantName, tempFileDump, titles):
        self.plantName = plantName
        self.tempFileDump = tempFileDump
        self.titles = titles.split(", ")

    def start_requests(self):
        searchString = self.searchPrefix + "+".join(self.plantName.split())
        self.searchUrl = os.path.join(self.BASE_URL, searchString)
        yield scrapy.Request(url=self.searchUrl, callback=self.parse)

    def parse(self, response):
        """search worldfloraonline and look for an entry with
        plant name and accepted status"""
        a = response.css('tr')
        if a == None:
            self.printToFile("Something went wrong!! Response is empty", "w+")
        else:
            self.outputStr = "***"
            check=0
            for i in a:

                status = i.css('div span::text').get()
                name = i.css('a::attr(title)').get()
                link = str(i.css('a::attr(href)').get()).split(";")[0]

                if str(status).lower() == "accepted name" and name.lower() == self.plantName.lower():
                    check=1
                    # for printing as xml
                    newURl=self.BASE_URL+link
                    top = ET.Element('plant', {'name' : self.plantName, 'link': self.BASE_URL+link})
                    self.outputXML= top
                    ET.ElementTree(element=top).write(self.tempFileDump)
                    yield scrapy.Request(url=self.BASE_URL+link, callback=self.parse2)
            if not check:
                self.printToFile(f'Something went wrong!!\n no plant named {self.plantName}', "w+")

    def parse2(self, response):
        """access the actual plant page and prints the paragraph in
        the tempFileDump"""
        outputStr2 = '\n'
        for sectionTitle in self.titles:
            # get desired sections
            #desired number of getLongestParagraphs
            parNum=3
            xpath = f'//*[(@id = "{sectionTitle}")]'
            outputList = response.xpath(xpath).css('div p::text').getall()
            sortedList= sorted(outputList, key=len)
            try:
                shortList= sortedList[-parNum:-1]
            except TypeError:
                shortList=sortedList

            # translate 2 xml
            section= ET.SubElement(self.outputXML, 'section', {'name': sectionTitle})
            outputPars = shortList
            for i in outputPars:
                ET.SubElement(section, 'paragraph', {'text': i})
        #print to file
        ET.ElementTree(element=self.outputXML).write(self.tempFileDump)


    def printToFile(self, string, accessMode="a"):  # access a for append, w+ for writing
        """prints to desired file xml or txt"""
        filename = self.tempFileDump
        with open(filename, accessMode) as f:
            # this downloads the good css tag, still need to extract links
            f.write(string)
        self.log('Saved file ')

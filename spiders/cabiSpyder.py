# -*- coding: utf-8 -*-

import scrapy
import os
import xml.etree.ElementTree as ET
# import settings.floraTitles as floraTitles


class cabiSpider(scrapy.Spider):
    name = 'cabi'
    allowed_domains = ['https://www.cabi.org']
    BASE_URL = 'https://www.cabi.org/isc/'
    searchPrefix = 'search/index?q='
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
        """search cabi invasuve species compendium and look for an entry with
        correct plant name and accepted status"""
        a = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "links", " " ))]').css('a')
        # self.printToFile("\n".join(a))
        for i in a:
            link = i.css('a::attr(href)').get()
            name = i.css('a::text').get()
            cleanName = name.strip()
            if self.plantName in cleanName and "datasheet" in link:
                # cleanName=cleanName+"  YES!!!"            # cleanName = " ".join(cleanName)
                self.printToFile(cleanName + "\n")
                url=self.BASE_URL+link
                self.printToFile(url)
                yield scrapy.Request(url=self.BASE_URL+link, callback=self.parse2)

    def parse2(self, response):
        """access the actual plant page and prints the paragraph in
        the tempFileDump"""
        outputStr2 = '\n'
        for sectionTitle in self.titles:
            # get desired sections
            # desired number of getLongestParagraphs
            parNum = 3
            xpath = f'//*[(@id = "{sectionTitle}")]'
            outputList = response.xpath(xpath).css('div p::text').getall()
            sortedList = sorted(outputList, key=len)
            try:
                shortList = sortedList[-parNum:-1]
            except TypeError:
                shortList = sortedList

            # translate 2 xml
            section = ET.SubElement(self.outputXML, 'section', {
                                    'name': sectionTitle})
            outputPars = shortList
            for i in outputPars:
                ET.SubElement(section, 'paragraph', {'text': i})
        # print to file
        ET.ElementTree(element=self.outputXML).write(self.tempFileDump)

    def printToFile(self, string, accessMode="a"):  # access a for append, w+ for writing
        """prints to desired file xml or txt"""
        filename = self.tempFileDump
        with open(filename, accessMode) as f:
            # this downloads the good css tag, still need to extract links
            f.write(string)
        self.log('Saved file ')

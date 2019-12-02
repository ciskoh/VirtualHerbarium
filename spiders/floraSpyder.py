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
            printToFile("Something went wrong!!", "w+")
        else:
            self.outputStr = "***"
            for i in a:

                status = i.css('div span::text').get()
                name = i.css('a::attr(title)').get()
                link = str(i.css('a::attr(href)').get()).split(";")[0]

                if str(status).lower() == "accepted name" and name.lower() == self.plantName.lower():

                    # for printing as xml
                    newURl=self.BASE_URL+link
                    top = ET.Element('plant', {'name' : self.plantName, 'link': self.BASE_URL+link})
                    self.outputXML= top
                    ET.ElementTree(element=top).write(self.tempFileDump)

                #     FOR PRINTING TO TXT FILE

                #     self.outputStr = self.outputStr + \
                #         f'\ntest: {str(status).lower() == "accepted name"} {name.lower() == self.plantName.lower()},'
                #     self.outputStr = self.outputStr + \
                #         f'\nname : {name}, \nlink : {str(link).split(";")[0]},'
                #     self.outputStr = self.outputStr + f'\nstatus : {status},'
                #     self.outputStr = self.outputStr + '\n***\n' + f'{self.BASE_URL}' + f'{link}'

                    # self.printToFile(self.outputStr, "w+")
                    yield scrapy.Request(url=self.BASE_URL+link, callback=self.parse2)

    def parse2(self, response):
        """access the actual plant page and prints the paragraph in
        the tempFileDump"""
        outputStr2 = '\n'
        for title in self.titles:
            section= ET.SubElement(self.outputXML, 'section', {'name': title})
            xpath = f'//*[(@id = "{title}")]'
            outputList = response.xpath(xpath).css('div p::text').getall()
            sortedList= outputList.sort(key=len)
            # try:
            #     shortList= sortedList.slice(-3,-1)
            # except TypeError:
            #     shortList=sortedList

            for i in sortedList:
                ET.SubElement(section, 'paragraph', {'text': i})
        ET.ElementTree(element=self.outputXML).write(self.tempFileDump)
        # c = b.css('div p')
        # general info: 'p.justified'
        # synonims "h2::text"
        # Bibliography "h2::text"
            # outputStr2 = outputStr2 + '\n'.join(outputList[-3:-1])

        #self.printToFile(outputStr2)

        # obj= i.css()
        # for site in sites:
        #     title = site.select('a/text()').extract()
        #     link = site.select('a/@href').extract()

    def printToFile(self, string, accessMode="a"):  # access a for append, w+ for writing
        """prints to desired file xml or txt"""
        filename = self.tempFileDump
        with open(filename, accessMode) as f:
            # this downloads the good css tag, still need to extract links
            f.write(string)
        self.log('Saved file ')

    # def createXml(self, tag, string="None", parent="None"):
    #     """create xml file and prints it to file calling printToFile"""
    #     elem, accessMode = ET.Element(tag), "w+"
    #     # if parent == "None":
    #     #     elem, accessMode = ET.Element(tag), "w+"
    #     # else:
    #     #     elem = ET.SubElement(parent, tag)
    #     #     elem.text = string
    #     #     accessMode = 'a'
    #
    #     xml_str = ET.tostring(elem, encoding='unicode')
    #     self.printToFile(xml_str, accessMode)

        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
        # yield {
        #     'title': quote.css('table.table a::attr(title)').getAll()[0:4],
        #     'link': quote.css('table.table a::attr(href)').getAll()[0:4],
        #      }
        # print(response)
        #     filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)

        # with this Xpath
        # test=response.css("table.table a::attr(href)").get()
        #

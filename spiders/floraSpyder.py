# -*- coding: utf-8 -*-

import scrapy
import os


class FloraSpider(scrapy.Spider):
    name = 'flora'
    allowed_domains = ['www.worldfloraonline.org']
    BASE_URL = 'http://www.worldfloraonline.org/'
    searchPrefix='search?query='

    TempFileDump="./floraDump.txt"

    def __init__(self, plantName):
     self.plantName = plantName


    def start_requests(self):
        searchString=self.searchPrefix+"+".join(self.plantName.split())
        self.searchUrl=os.path.join(self.BASE_URL, searchString )
        yield scrapy.Request(url=self.searchUrl, callback=self.parse)

    def parse(self, response):
        """search worldfloraonline and look for an entry with
        plant name and accepted status"""
        a = response.css('tr')
        if a == None:
            obj="Something went wrong!!"
        else:
            outputStr="***"
            for i in a:

                status=i.css('div span::text').get()
                name=i.css('a::attr(title)').get()
                link=str(i.css('a::attr(href)').get()).split(";")[0]
                if str(status).lower() == "accepted name" and name.lower() == self.plantName.lower():
                    outputStr=outputStr+f'\ntest: {str(status).lower() == "accepted name"} {name.lower() == self.plantName.lower()},'
                    outputStr=outputStr+f'\nname : {name}, \nlink : {str(link).split(";")[0]},'
                    outputStr=outputStr+f'\nstatus : {status},'
                    outputStr=outputStr+'\n***\n'
                    self.printToFile(outputStr)
                    # yield scrapy.Request(url=os.path.join(self.BASE_URL, link), callback=self.parse2)

    def parse2(self, response):
        pass

                # obj= i.css()
        # for site in sites:
        #     title = site.select('a/text()').extract()
        #     link = site.select('a/@href').extract()

    def printToFile(self, string):
        filename = self.TempFileDump
        with open(filename, 'w') as f:
            f.write(string) # this downloads the good css tag, still need to extrcat links
        self.log('Saved file ')


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

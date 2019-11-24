# -*- coding: utf-8 -*-

import scrapy



class FloraSpider(scrapy.Spider):
    name = 'flora'
    allowed_domains = ['www.worldfloraonline.org']
    start_urls = ['http://www.worldfloraonline.org/search?query=parthenium+hysterophorus']

    def parse(self, response):
        for response.css("table.table a")
            yield {
                'title': quote.css('table.table a::attr(title)').getAll()[0:4],
                'link': quote.css('table.table a::attr(href)').getAll()[0:4],
                 }


        # with this Xpath
        # test=response.css("table.table a::attr(href)").get()
        #

# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        self.log("I just run the url **********" + response.url)
        urls = response.css('div.quote > span > a::attr(href)').extract()
        for url in urls:
           url = response.urljoin(url)
           yield scrapy.Request(url = url , callback = self.details)
            
          #follow pagination
        next_page_url = response.css('li.next > a::attr(href)').extract_first()
        print(next_page_url)
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url = next_page_url , callback = self.parse)

            
    def details(self, response):
        yield{
                'name' : response.css('h3.author-title::text').extract_first()
        }
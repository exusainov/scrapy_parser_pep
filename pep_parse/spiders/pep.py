import re

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/', ]

    def parse(self, response):
        numerical_index = response.xpath('//section[@id="numerical-index"]')
        tr_tags = numerical_index.css('tbody tr')
        for tr_tag in tr_tags:
            pep_link = tr_tag.css('td a::attr(href)').get()
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        page_title = str(
            response.xpath('//h1[@class="page-title"]/text()').get())
        pattern = r'(?P<number>\d+) – (?P<name>.*)'
        text_pars = re.search(pattern, page_title)
        number = text_pars.group('number')
        name = text_pars.group('name')
        status = response.css(
            'dt:contains("Status")').xpath('//abbr/text()').get()
        data = {
            'number': number,
            'name': name,
            'status': status
        }
        yield PepParseItem(data)

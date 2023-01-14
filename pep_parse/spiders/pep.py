import scrapy


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['http://peps.python.org/']

    def parse(self, response):
        pass
        numerical_index = response.xpath('//section[@id="numerical-index"]')
        tr_tags = numerical_index.css('tbody tr')
        for tr_tag in tr_tags:
            pep_link = tr_tag.css('td a::attr(href)').get() 
            yield response.follow(pep_link, callback=self.parse_author)
        # clas = response.xpath('//section[@id="numerical-index"]')   берем таблицу со всеми pep
        # clas.css('tr a::attr(href)').getall()
        #  tr = clas.css('tbody tr')
        #  tr[0].css('td a::attr(href)').get() брать одну ссылку по циклу для того чтобы дальше обработать
    def parse_pep(self, response):
        pass

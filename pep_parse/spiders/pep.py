import re
import scrapy

from ..items import PepParseItem


REGEX_PEP = r'(?P<number>\d+)\W+(?P<name>.+)'
URL = 'peps.python.org'


class PepSpider(scrapy.Spider):
    name = "pep"
    # allowed_domains = [URL]
    # start_urls = [f'https://{URL}/']
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://peps.python.org/']    

    def parse(self, response):
        peps = response.css('#numerical-index tr a::attr(href)').getall()
        for pep_link in peps:
            yield response.follow(pep_link, callback=self.pep_parse)

    def pep_parse(self, response):
        title_formatted = re.search(
            REGEX_PEP, response.css('h1.page-title::text').get()
        )
        data = {
            'number': title_formatted.group('number'),
            'name': title_formatted.group('name'),
            'status': response.css('dt:contains("Status")+dd abbr::text').get()
        }
        yield PepParseItem(data)

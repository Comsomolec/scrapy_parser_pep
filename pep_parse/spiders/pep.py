import re
import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import DOMAIN


REGEX_PEP = r'(?P<number>\d+)\W+(?P<name>.+)'


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = [DOMAIN]
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        for pep_link in response.css(
            '#numerical-index tr a::attr(href)'
        ).getall():
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        title_formatted = re.search(
            REGEX_PEP, response.css('h1.page-title::text').get()
        )
        yield PepParseItem(
            dict(
                number=title_formatted.group('number'),
                name=title_formatted.group('name'),
                status=response.css(
                    'dt:contains("Status")+dd abbr::text'
                ).get()
            )
        )

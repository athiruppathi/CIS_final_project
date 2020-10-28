import scrapy


class MonsterSpider(scrapy.Spider):
    name = 'monster'
    allowed_domains = ['https://www.monster.com/jobs/search/?q=computer-information-systems&intcid=skr_navigation_nhpso_searchMain']
    start_urls = ['http://https://www.monster.com/jobs/search/?q=computer-information-systems&intcid=skr_navigation_nhpso_searchMain/']

    def parse(self, response):
        pass

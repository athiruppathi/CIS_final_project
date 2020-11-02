import scrapy


class MonsterSpider(scrapy.Spider):
    name = 'monster'
    start_urls = ['https://www.monster.com/jobs/search/?q=computer-information-systems&intcid=skr_navigation_nhpso_searchMain']

    def parse(self, response):
        entry = response.css('header')
        links = entry.xpath('.//h2/a/@href').extract()
        titles = entry.xpath('.//h2/a/text()').extract()
        yield{'titles':titles, 'links':links}

# need to clean up titles list
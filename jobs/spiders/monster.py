import scrapy
from ..items import JobsItem


class MonsterSpider(scrapy.Spider):
    name = 'monster'
    start_urls = ['https://www.monster.com/jobs/search/?q=computer-information-systems&intcid=skr_navigation_nhpso_searchMain']

    custom_settings = {
        'FEED_FORMAT':'csv',
        'FEED_URI':'monster_data.csv'
    }


    def parse(self, response):

        items = JobsItem()

        entry = response.css('header')
        links = entry.xpath('.//h2/a/@href').extract()
        titles = entry.xpath('.//h2/a/text()').extract()

        items['monster_titles'] = titles
        items['monster_links'] = links
        yield items

        
import scrapy
from urllib.parse import urljoin
#from urlparse import urljoin 
from ..items import JobsItem


class IndeedSpider(scrapy.Spider):
    name = 'indeed'
    start_urls = ['https://www.indeed.com/q-computer-information-systems-jobs.html']

    custom_settings = {
        'FEED_FORMAT':'csv',
        'FEED_URI':'indeed_data.csv'

    }

    def parse(self, response):

        items = JobsItem()

        entry = response.css('.jobsearch-SerpJobCard')
        titles = entry.xpath('.//h2/a/@title').extract()
        links = entry.xpath('.//h2/a/@href').extract()
        absolute_url_list = []
        for link in links:
            #yield response.follow(link, callback=self.parse)
            absolute_url = response.follow(link, callback=self.parse)
            absolute_url_list.append(absolute_url)

        items['indeed_titles'] = titles
        items['indeed_links'] = absolute_url_list
        yield items
        #yield {'titles':titles, 'links':absolute_url_list}


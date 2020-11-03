import scrapy
from urllib.parse import urljoin
#from urlparse import urljoin 


class IndeedSpider(scrapy.Spider):
    name = 'indeed'
    start_urls = ['https://www.indeed.com/q-computer-information-systems-jobs.html']

    def parse(self, response):
        entry = response.css('.jobsearch-SerpJobCard')
        titles = entry.xpath('.//h2/a/@title').extract()
        links = entry.xpath('.//h2/a/@href').extract()
        absolute_url_list = []
        for link in links:
            #yield response.follow(link, callback=self.parse)
            absolute_url = response.follow(link, callback=self.parse)
            absolute_url_list.append(absolute_url)

        yield {'titles':titles, 'links':absolute_url_list}

# how is the yielded information stored? 
# use main.py file to import and pre-process data from the spiders
# format the scraped data into the tkinter GUI 

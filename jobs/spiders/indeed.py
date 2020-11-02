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
        absolute_links = []
        for link in links:
            #absolute_url = urljoin('https://www.indeed.com/q-computer-information-systems-jobs.html',link)
            #yield {'links': response.follow(link, callback=self.parse)}
            absolute_links = (yield response.follow(link, callback=self.parse)).append()
        yield {'titles':titles,'links':absolute_links}

# figure out how to put absolute links in the same dictionary as titles
# how is the yielded information stored? 
# use main.py file to import and pre-process data from the spiders
# format the scraped data into the tkinter GUI 

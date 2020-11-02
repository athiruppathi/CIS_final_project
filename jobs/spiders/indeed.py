import scrapy


class IndeedSpider(scrapy.Spider):
    name = 'indeed'
    #allowed_domains = ['https://www.indeed.com/q-computer-information-systems-jobs.html']
    #start_urls = ['http://https://www.indeed.com/q-computer-information-systems-jobs.html/']
    start_urls = ['https://www.indeed.com/q-computer-information-systems-jobs.html']

    def parse(self, response):
        entry = response.css('.jobsearch-SerpJobCard')
        titles = entry.xpath('.//h2/a/@title').extract()
        links = entry.xpath('.//h2/a/@href').extract()

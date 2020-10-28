import scrapy


class LinkedinSpider(scrapy.Spider):
    name = 'linkedin'
    allowed_domains = ['https://www.linkedin.com/jobs/search?keywords=Computer%20information%20systems&location=&geoId=&trk=homepage-jobseeker_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0']
    start_urls = ['http://https://www.linkedin.com/jobs/search?keywords=Computer%20information%20systems&location=&geoId=&trk=homepage-jobseeker_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0/']

    def parse(self, response):
        pass

import scrapy


class LinkedinSpider(scrapy.Spider):
    name = 'linkedin'
    start_urls = ['https://www.linkedin.com/jobs/search?keywords=computer"%20"information"%20"systems&location=&geoId=&trk=homepage-jobseeker_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0']

    def parse(self, response):
        title_class = response.css('.result-card__contents')
        titles = title_class.xpath('.//h3/text()').extract()
        links_class = response.css('.result-card__full-card-link')
        links = links_class.xpath('//@href')[:25].extract()
        yield{'titles':titles,'links':links}

#returns 25 entries of each 
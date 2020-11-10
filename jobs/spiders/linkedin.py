import scrapy
from ..items import JobsItem


class LinkedinSpider(scrapy.Spider):
    name = 'linkedin'
    start_urls = ['https://www.linkedin.com/jobs/search?keywords=computer"%20"information"%20"systems&location=&geoId=&trk=homepage-jobseeker_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0']

    custom_settings = {
        'FEED_FORMAT':'csv',
        'FEED_URI':'linkedin_data.csv'
    }

    def parse(self, response):

        items = JobsItem()

        titles = response.xpath('//*[@class="result-card__contents job-result-card__contents"]/h3/text()').extract()
        links = response.xpath('//*[@class="result-card__contents job-result-card__contents"]/h4/a/@href').extract()
        
        items['linkedin_titles'] = titles
        items['linkedin_links'] = links
        yield items
        
        #yield {'titles':titles,'links':links}

#returns 25 entries of each 
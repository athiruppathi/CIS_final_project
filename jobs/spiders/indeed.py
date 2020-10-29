import scrapy


class IndeedSpider(scrapy.Spider):
    name = 'indeed'
    allowed_domains = ['https://www.indeed.com/q-computer-information-systems-jobs.html']
    start_urls = ['http://https://www.indeed.com/q-computer-information-systems-jobs.html/']

    def parse(self, response):
        #entry = response.css('[data-tn-component="organicJob"]')
        entry = response.css('.jobsearch-SerpJobCard')
        for attribute in entry: 
            titles = entry.xpath('.//h2/a/@title').extract()
            links = entry.xpath('.//h2/a/@href').extract()
            for link in links: 
                absolute_url = response.urljoin(link)
                #yield Request(absolute_url, callback=self, parse)

#To do: 
# figure out URLs, how to use response.urljoin 
# learn purpose of yield  
# learn xpath regex 
# how can I get title and URL from this file to main.py
# vs code linting is what makes colors change 
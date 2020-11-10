# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsItem(scrapy.Item):
    # define the fields for your item here like:
    #global indeed_titles
    indeed_titles = scrapy.Field()
    indeed_links = scrapy.Field()
    linkedin_titles = scrapy.Field()
    linkedin_links = scrapy.Field()
    monster_titles = scrapy.Field()
    monster_links = scrapy.Field()

    # def __init__(self):
    #     self.indeed_titles = indeed_titles
    #     self.indeed_links = indeed_links
    #     self.linkedin_titles = linkedin_titles
    #     self.monster_titles = monster_titles
    #     self.monster_links = monster_links

    # def get_indeed(self)
    #     return indeed_titles, indeed_links

        

#print(indeed_titles)
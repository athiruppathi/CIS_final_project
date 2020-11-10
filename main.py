import tkinter as tk 
from tkinter import ttk
from jobs.spiders import indeed
from jobs.spiders import linkedin
from jobs.spiders import monster 
import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd 

# Create Tkinter root window
root = tk.Tk()
root.title('Job Board Aggregator')
root.geometry('700x900')
canvas = tk.Canvas(root)
canvas.pack()


# Title and Description
label = tk.Label(canvas,text='CIS Job Board', font=(None, 25), height=2)
label.grid(row=0, column=0, columnspan=6)

label2 = tk.Label(canvas, text='See results from the top Computer Information System jobs from the most popular job boards \n \
    (Indeed, Linkedin, and Monster)')
label2.grid(row=1, column=0)


# Run Spiders
process = CrawlerProcess()
process.crawl(indeed.IndeedSpider) 
process.crawl(linkedin.LinkedinSpider)
process.crawl(monster.MonsterSpider)
process.start()

# Import and Clean Data 
pd.read_csv()












root.mainloop()



import tkinter as tk 
from tkinter import ttk
from jobs.spiders import indeed
from jobs.spiders import linkedin
from jobs.spiders import monster 
import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd 
import os

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
current_directory = os.getcwd()
partialPathIndeed = '\indeed_data.csv'
partialPathLinkedin = '\linkedin_data.csv'
partialPathMonster = '\monster_data.csv'

indeedPath = current_directory + partialPathIndeed
linkedinPath = current_directory + partialPathLinkedin
monsterPath = current_directory + partialPathMonster

indeed_sdata = pd.read_csv(indeedPath)
linkedin_sdata = pd.read_csv(linkedinPath)
monster_sdata = pd.read_csv(monsterPath)


#Indeed 

link_string1 = indeed_sdata.iloc[0,0]
link_string1 = link_string1[1:-2]
link_list1 = link_string1.split(",")

indeed_links_list = []
for i in link_list1:
    i = i[6:-2]
    indeed_links_list.append(i)
    
del indeed_links_list[0]
del indeed_links_list[14] # removes bad URL 


titles_string1 = indeed_sdata.iloc[0,1]
indeed_titles_list = titles_string1.split(",")

del indeed_titles_list[0]


indeed_df = pd.DataFrame({'titles':indeed_titles_list,'links':indeed_links_list}) #indeed dataframe


#Linkedin
linkedin_sdata.drop(['indeed_links','indeed_titles','monster_links','monster_titles'], axis=1, inplace=True)
linkedin_sdata.drop([1,2,3,4], axis=0, inplace=True)
linkedin_sdata.reset_index(inplace=True)
linkedin_sdata.drop(['index'], axis=1, inplace=True)

linksA = linkedin_sdata.iloc[0,0]
linkedin_links_list = linksA.split(",")

titlesA = linkedin_sdata.iloc[0,1]
linkedin_titles_list = titlesA.split(',')

linkedin_df = pd.DataFrame({'titles':linkedin_titles_list, 'link':linkedin_links_list}) #linkedin dataframe


#Monster
monster_links_string = monster_sdata.iloc[0,4]
monster_links_list = monster_links_string.split(",")

monster_titles_string = monster_sdata.iloc[0,5]
monster_titles_list = monster_titles_string.split(",")

for i in monster_titles_list:  # account for possibility of city,state format splititng at the comma 
    if len(i) < 7:
        indexValue = monster_titles_list.index(i)
        monster_titles_list.pop(indexValue)

    
monster_df = pd.DataFrame({'titles':monster_titles_list,'links':monster_links_list})  # monster dataframe


# Make entries in the GUI that dispaly job entries from dataframes







root.mainloop()

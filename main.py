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
#pd.read_csv()
indeed_sdata = pd.read_csv(r"C:\Users\arjun\OneDrive\Desktop\jobs\indeed_data.csv")
linkedin_sdata = pd.read_csv(r"C:\Users\arjun\OneDrive\Desktop\jobs\linkedin_data.csv")
monster_sdata = pd.read_csv(r"C:\Users\arjun\OneDrive\Desktop\jobs\monster_data.csv")

#Indeed 
indeed_sdata.drop(columns=['linkedin_links','linkedin_titles','monster_links','monster_titles'], axis=1, inplace=True) #remove extra columns
indeed_sdata.drop([1], inplace=True) #remove extra row
indeed_sdata.reset_index(inplace=True)  #reset the index
indeed_sdata.drop(['index'], axis=1, inplace=True) #remove the old index column


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
linkedin_sdata.drop([1,3,5,6,7,9,10], inplace=True)
linkedin_sdata.reset_index(inplace=True)
linkedin_sdata.drop(['index'], axis=1, inplace=True)

linksA = linkedin_sdata.iloc[0,0]
linksB = linkedin_sdata.iloc[1,0]
linksC = linkedin_sdata.iloc[2,0]
linksD = linkedin_sdata.iloc[3,0]

linkedin_links_list = linksA + ',' + linksB + ',' + linksC + ',' + linksD
linkedin_links_list = linkedin_links_list.split(",")

titlesA = linkedin_sdata.iloc[0,1]
titlesB = linkedin_sdata.iloc[1,1]
titlesC = linkedin_sdata.iloc[2,1]
titlesD = linkedin_sdata.iloc[3,1]

linkedin_titles_list = titlesA + ',' + titlesB + ',' + titlesC + ',' + titlesD
linkedin_titles_list = linkedin_titles_list.split(",")

del linkedin_titles_list[97:-1]

linkedin_df = pd.DataFrame({'titles':linkedin_titles_list, 'link':linkedin_links_list}) #linkedin dataframe


#Monster
monster_sdata.drop(['indeed_links','indeed_titles','linkedin_links','linkedin_titles'], axis=1, inplace=True)

monster_links_string = monster_sdata.iloc[0,0]
monster_links_list = monster_links_string.split(",")

monster_titles_string = monster_sdata.iloc[0,1]
monster_titles_list = monster_titles_string.split(",")

monster_df = pd.DataFrame({'titles':monster_titles_list,'links':monster_links_list})  # monster dataframe








root.mainloop()

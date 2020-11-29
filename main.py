import tkinter as tk 
from tkinter import ttk
from jobs.spiders import indeed
from jobs.spiders import linkedin
from jobs.spiders import monster 
import re
from scrapy.crawler import CrawlerProcess
import pandas as pd 
import os
import webbrowser

# Create Tkinter root window and headers
root = tk.Tk()
root.title('Job Board Aggregator')
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f'550x{height}')

label = tk.Label(root,text='CIS Job Board', font=(None, 18), height=2)
label.pack()
label2 = tk.Label(root, text='See the top Computer Information System jobs from the most popular job boards \n \
    (Indeed, Linkedin, and Monster)')
label2.pack()


# Run Spiders
process = CrawlerProcess()
process.crawl(indeed.IndeedSpider) 
process.crawl(linkedin.LinkedinSpider)
process.crawl(monster.MonsterSpider)
process.start()

# Import Data 
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


#Indeed Data Cleaning
indeed_links = indeed_sdata.iloc[0,0]
indeed_titles = indeed_sdata.iloc[0,1]

indeed_links = indeed_links[:-2]
indeed_links_list = indeed_links.split('>,')
iLinksList = []
for i in indeed_links_list:
    i = i[6:-1]
    iLinksList.append(i)

p = re.compile('\S, ')
iTitlesString = p.sub('-',indeed_titles)
iTitlesList = iTitlesString.split(',')  # use regex patten to replace comma with "-", then split at ","
        

indeed_df = pd.DataFrame({'titles':iTitlesList,'links':iLinksList}) #indeed dataframe

#Linkedin Data Cleaning
linksA = linkedin_sdata.iloc[0,2]
linkedin_links_list = linksA.split(",")

titlesA = linkedin_sdata.iloc[0,3]
linkedin_titles_list = titlesA.split(',')


linkedin_titles_list = linkedin_titles_list[:5]
linkedin_links_list = linkedin_links_list[:5]

linkedin_df = pd.DataFrame({'titles':linkedin_titles_list, 'links':linkedin_links_list}) #linkedin dataframe


#Monster Data Cleaning
monster_links_string = monster_sdata.iloc[0,4]
monster_links_list = monster_links_string.split(",")

monster_titles_string = monster_sdata.iloc[0,5]
mTitlesList = re.split("\s,",monster_titles_string) 

monster_df = pd.DataFrame({'titles':mTitlesList,'links':monster_links_list})  # monster dataframe


# Combine Dataframes and convert into dictionary 
complete_df = pd.concat([indeed_df,monster_df,linkedin_df], axis=0)
complete_df.reset_index(inplace=True)
complete_df.drop(['index'], axis=1, inplace=True) #join all datafraemes into one

complete_df['tuples'] = complete_df[['titles', 'links']].apply(tuple, axis=1) # create a column of tuples with title and links
complete_dict = {}
for x, y in complete_df['tuples']:
    complete_dict[x] = y    #create dictionary from the tuple column


# Create buttons and click command
def clickURL(title):
    link = complete_dict.get(title)
    webbrowser.open(link,new=0)

for title in complete_dict:
    tbutton = tk.Button(root, text=title, bg='gray', command=lambda x=title: clickURL(x))
    tbutton.pack()


# Delete dataframes for the next time user runs program
os.remove(indeedPath)
os.remove(linkedinPath)
os.remove(monsterPath)

root.mainloop()
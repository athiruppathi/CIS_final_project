import tkinter as tk 
from tkinter import ttk
from jobs.spiders import indeed
from jobs.spiders import linkedin
from jobs.spiders import monster 
import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd 
import os
import webbrowser

# Create Tkinter root window
root = tk.Tk()
root.title('Job Board Aggregator')
#root.geometry('700x900')

# Create scrollabe widgit 
container = ttk.Frame(root)
canvas = tk.Canvas(container, width=600, height=700)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas, width=600, height=700)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", width=600, height=700)
canvas.configure(yscrollcommand=scrollbar.set)

#scrollable_frame.place(x=0, y=0, anchor="nw", width=385, height=460)

# Create Title and Description
label = tk.Label(scrollable_frame,text='CIS Job Board', font=(None, 18), height=2)
label.pack()
label2 = tk.Label(scrollable_frame, text='See results from the top Computer Information System jobs from the most popular job boards \n \
    (Indeed, Linkedin, and Monster)')
label2.pack()


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
    
del indeed_links_list[0]  # delete ad on first entry
#del indeed_links_list[14] # removes bad URL 


titles_string1 = indeed_sdata.iloc[0,1]
indeed_titles_list = titles_string1.split(",")

del indeed_titles_list[0] #delete ad on the first entry

for z in indeed_titles_list:  # account for possibility of city,state format splitting at the comma 
    if len(z) < 11:
        indexValue1 = indeed_titles_list.index(z)
        indeed_titles_list.pop(indexValue1)

titlesLen = len(indeed_titles_list)
linksLen = len(indeed_links_list)

if titlesLen > linksLen:     # makes sure lists are the same size
    diff = titlesLen - linksLen
    for i in range(diff):
        indeed_titles_list.pop(i)
elif linksLen > titlesLen:
    diff2 = linksLen - titlesLen
    for i in range(diff2):
        indeed_links_list.pop(i)

indeed_df = pd.DataFrame({'titles':indeed_titles_list,'links':indeed_links_list}) #indeed dataframe


#Linkedin
linksA = linkedin_sdata.iloc[0,2]
linkedin_links_list = linksA.split(",")

titlesA = linkedin_sdata.iloc[0,3]
linkedin_titles_list = titlesA.split(',')

for y in linkedin_titles_list:  # account for possibility of city,state format splitting at the comma 
    if len(y) < 11:
        indexValue2 = linkedin_titles_list.index(y)
        linkedin_titles_list.pop(indexValue2)

linkedin_titles_list = linkedin_titles_list[:5]
linkedin_links_list = linkedin_links_list[:5]

linkedin_df = pd.DataFrame({'titles':linkedin_titles_list, 'links':linkedin_links_list}) #linkedin dataframe



#Monster
monster_links_string = monster_sdata.iloc[0,4]
monster_links_list = monster_links_string.split(",")

monster_titles_string = monster_sdata.iloc[0,5]
monster_titles_list = monster_titles_string.split(",")

for i in monster_titles_list:  # account for possibility of city,state format splitting at the comma 
    if len(i) < 11:
        indexValue3 = monster_titles_list.index(i)
        monster_titles_list.pop(indexValue3)

monster_titles_list_clean = []
for t in monster_titles_list:  #remove new lines from titles
    t = t[:-2]
    monster_titles_list_clean.append(t)

mTitleLen = len(monster_titles_list_clean)
mLinksLen = len(monster_links_list)

if mTitleLen > mLinksLen: # makes sure lists are the same size
    diff5 = mTitleLen - mLinksLen
    for i in range(diff5):
        monster_titles_list_clean.pop(i)
#elif mLinksLen > mTitleLen:
#    diff6 = mLinksLen - mTitleLen
#    for i in range(diff6):
#        monster_links_list.pop(i)

    
monster_df = pd.DataFrame({'titles':monster_titles_list_clean,'links':monster_links_list})  # monster dataframe


# Make entries in the GUI that shows job entries from dataframes
   #join all dataframes of data
complete_df = pd.concat([indeed_df,monster_df,linkedin_df], axis=0)
complete_df.reset_index(inplace=True)
complete_df.drop(['index'], axis=1, inplace=True) #join all datafraemes into one

# create a column of tuples with title and links
complete_df['tuples'] = complete_df[['titles', 'links']].apply(tuple, axis=1)
complete_dict = {}
for x, y in complete_df['tuples']:
    complete_dict[x] = y    #create dictionary from the tuple column

# Create buttons and click command
def clickURL(title):
    link = complete_dict.get(title)
    webbrowser.open(link,new=0)

for title in complete_dict:
    tbutton = tk.Button(scrollable_frame, text=title, bg='gray', command=lambda x=title: clickURL(x))
    tbutton.pack()

container.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Delete dataframes for the next time user runs program

os.remove(indeedPath)
os.remove(linkedinPath)
os.remove(monsterPath)

root.mainloop()
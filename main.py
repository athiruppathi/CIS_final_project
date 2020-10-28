import tkinter as tk 
from tkinter import ttk


root = tk.Tk()
root.title('Job Board Aggregator')
root.geometry('700x900')
canvas = tk.Canvas(root)
canvas.pack()



# Title and Search Bar
label = tk.Label(canvas,text='CIS Job Board', font=(None, 25), height=2)
label.grid(row=0, column=0, columnspan=6)

label2 = tk.Label(canvas, text='Search for a job title, and see results from the most popular job board sites \n \
    (Indeed, Linkedin, Glassdoor, and Monster)')
label2.grid(row=1, column=0)


entry = tk.Entry(canvas, width=50, borderwidth=5)
entry.grid(row=2, column=0, columnspan=6)
entryString = entry.get()




def search_Click():
    #jobSearch = entry.get()
    pass



searchButton = tk.Button(canvas, text='Search', command=search_Click)
searchButton.grid(row=2,column=1)



root.mainloop()



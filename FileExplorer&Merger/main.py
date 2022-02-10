from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from fileMerger.merger import *

import logging as lg
lg.basicConfig(filename='main.log', level=lg.INFO, format='%(asctime)s %(levelname)s %(message)s')

def show_files():
    try:
        text['state']='normal'
        fileList=getFiles(entry.get())
        for i in fileList:
            text.insert(END, i+'\n')
        text['state']='disabled'
        messagebox.showinfo("Notification", f"{len(fileList)} Files Found ")
        lg.info(f"{len(fileList)} Files Found ")

    except Exception as e:
        lg.error('error occured during file explore', e)
        return e

def merge():
    try:
        ext=fileExtension.get()
        if ext=='.pdf':
           msg=mergePDF(entry.get(), fileName.get())
           messagebox.showinfo("Notification", msg)
           lg.info(msg)
        elif ext=='.docx':
            msg=mergeDOC(entry.get(), fileName.get())
            messagebox.showinfo("Notification", msg)
            lg.info(msg)
        elif ext=='.txt':
            msg=mergeTXT(entry.get(), fileName.get())
            messagebox.showinfo("Notification", msg)
            lg.info(msg)

    except Exception as e:
        lg.error("error occured during file merge!", e)
        return e

root=Tk()
root.title("File explorer")
root.geometry("1000x700")

Label(text="File Explorer", font="bold").grid(row=0, column=1)

Label(root, text="Enter a file path here", font="bold").grid(row=1, column=0, padx=30, pady=30)
entry=Entry(root,width=100)
entry.grid(row=1, column=1, pady=30)
search_button=Button(text="Search", font="bold", command=show_files).grid(row=1, column=2, padx=20, pady=30)

text=Text(root, state='disabled')
text.place(x=100, y=150, width=800, height=400)
scroll=Scrollbar(root, orient='vertical', command=text.yview)
scroll.place(x=900, y=150, height=400)
text['yscrollcommand']=scroll.set

Label(root, text='Filename', font='bold').place(x=350, y=580)
fileName=Entry(root)
fileName.place(x=450, y=580, width=200)

Label(root, text="Choose a file extension to merge", font="bold").place(x=200, y=610)
#dropdown
n=StringVar()
fileExtension= ttk.Combobox(root, values=['.pdf', '.txt', '.docx'], width=20, textvariable=n)
fileExtension.place(x=450, y=610)
merge_button=Button(text="Merge", font="bold", command=merge)
merge_button.place(x=650, y=610)
root.mainloop()
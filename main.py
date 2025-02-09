#data entry == Add,delete,Modify
#date
#status ==Done,Not started,in progress
#

#fix the data insert problem --v
# date issue --v
# add a dropdown menu to the status column 
# find a way to save the tasks using files 

import tkinter as tk
from tkinter import ttk
from datetime import datetime

class TodoList(tk.Frame):
    def __init__(self,parent):
        tk.Frame.__init__(self,parent)
        self.parent = parent
        self.start_UI()
    
    def start_UI(self):
        self.parent.title("ToDO APP")
        self.parent.grid_rowconfigure(0,weight=1)
        self.parent.grid_columnconfigure(0,weight=1)
        self.parent.config(background="Lavender")  

        self.task_entry = tk.Label(self.parent, text ="Name of the task")
        self.task = tk.Entry(self.parent)
        self.task_entry.grid(row=0,column=0,sticky=tk.W)
        self.task.grid(row=0,column=1)


        self.status_entry = tk.Label(self.parent, text ="Status")
        self.options = ["Done","Not done","In progress"]
        self.combo = ttk.Combobox(self.parent,values=self.options,state="readonly")
        self.combo.grid(row=2,column=1,sticky=tk.W)
        self.combo.bind("<<ComboboxSelected>>",self.start_UI)
        self.status_entry.grid(row=2,column=0,sticky=tk.W)
        

        self.insert_task = tk.Button(self.parent, text="Insert", command=self.insert_data)
        self.insert_task.grid(row=3,column=1,sticky=tk.W)
        self.exit_button = tk.Button(self.parent,text="Exit",command=self.parent.quit)
        self.exit_button.grid(row=0,column=3)

        self.tree = ttk.Treeview(self.parent, columns=('Task','Date','Status'),show="headings")
        self.tree.heading('Task',text="Name of the task")
        self.tree.heading('Date',text="Date Added")
        self.tree.heading('Status',text="Status")
        self.tree.column("Task",stretch=tk.YES)
        self.tree.column("Date",stretch=tk.YES)
        self.tree.column("Status",stretch=tk.YES)
        self.tree.grid(row=4,column=0,columnspan=3,sticky='nsew')
        self.treeview = self.tree
       
    
    def insert_data(self):
       task_name = self.task.get()
       task_date = datetime.now().strftime("%d-%m-%Y")
       task_status = self.combo.get()
       self.treeview.insert('','end',text = task_name,values=(task_name,task_date,task_status))
    
def main():
        root = tk.Tk()
        app = TodoList(root)
        root.mainloop()
    
if __name__ == "__main__":
        main()
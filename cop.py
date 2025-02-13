# 
# root = tk.Tk()
# root.title("Data Table Example")

# columns = ('Name_of_the_task',date,'status')

# tree = ttk.Treeview(root, columns=columns,show='headings')

# tree.heading ('Name_of_the_task', text = "Name of The Task")
# tree.heading (date, text = date)
# tree.heading ('status', text = "Status")
# tree.grid(row=4, column=4, sticky='nsew')

# tree.insert('','end',text=" "+str(i),values=)


# root.mainloop()

# try:
#     import Tkinter
#     import ttk
# except ImportError:  # Python 3
#     import tkinter as Tkinter
#     import tkinter.ttk as ttk


# class Begueradj(Tkinter.Frame):
#     '''
#     classdocs
#     '''
#     def __init__(self, parent):
#         '''
#         Constructor
#         '''
#         Tkinter.Frame.__init__(self, parent)
#         self.parent=parent
#         self.initialize_user_interface()

#     def initialize_user_interface(self):
#         """Draw a user interface allowing the user to type
#         items and insert them into the treeview
#         """
#         self.parent.title("Canvas Test")
#         self.parent.grid_rowconfigure(0, weight=1)
#         self.parent.grid_columnconfigure(0, weight=1)
#         self.parent.config(background="lavender")

#         # Define the different GUI widgets
#         self.dose_label = Tkinter.Label(self.parent, text="Dose:")
#         self.dose_entry = Tkinter.Entry(self.parent)
#         self.dose_label.grid(row=0, column=0, sticky=Tkinter.W)
#         self.dose_entry.grid(row=0, column=1)

#         self.modified_label = Tkinter.Label(self.parent,
#                                             text="Date Modified:")
#         self.modified_entry = Tkinter.Entry(self.parent)
#         self.modified_label.grid(row=1, column=0, sticky=Tkinter.W)
#         self.modified_entry.grid(row=1, column=1)

#         self.submit_button = Tkinter.Button(self.parent, text="Insert",
#                                             command=self.insert_data)
#         self.submit_button.grid(row=2, column=1, sticky=Tkinter.W)
#         self.exit_button = Tkinter.Button(self.parent, text="Exit",
#                                           command=self.parent.quit)
#         self.exit_button.grid(row=0, column=3)

#         # Set the treeview
#         self.tree = ttk.Treeview(self.parent,
#                                  columns=('Dose', 'Modification date'))
#         self.tree.heading('#0', text='Item')
#         self.tree.heading('#1', text='Dose')
#         self.tree.heading('#2', text='Modification Date')
#         self.tree.column('#1', stretch=Tkinter.YES)
#         self.tree.column('#2', stretch=Tkinter.YES)
#         self.tree.column('#0', stretch=Tkinter.YES)
#         self.tree.grid(row=4, columnspan=4, sticky='nsew')
#         self.treeview = self.tree
#         # Initialize the counter
#         self.i = 0

#     def insert_data(self):
#         """
#         Insertion method.
#         """
#         self.treeview.insert('', 'end', text="Item_"+str(self.i),
#                              values=(self.dose_entry.get() + " mg",
#                                      self.modified_entry.get()))
#         # Increment counter
#         self.i = self.i + 1


# def main():
#     root=Tkinter.Tk()
#     d=Begueradj(root)
#     root.mainloop()

# if __name__=="__main__":
#     main()

import tkinter as tk
from tkinter import ttk

class MyApp:
    def __init__(self, parent):
        self.parent = parent
        self.status_entry = tk.Label(self.parent, text="Status")
        self.options = ["Done", "Not done", "In progress"]
        self.combo = ttk.Combobox(self.parent, values=self.options, state="readonly")
        
        # Corrected event binding
        self.combo.bind("<<ComboboxSelected>>", self.on_select)
        
        self.stat = tk.Entry(self.parent)  # Corrected parent
        
        self.status_entry.grid(row=2, column=0, sticky=tk.W)
        self.combo.grid(row=2, column=1)  # Added missing grid() for combo
        self.stat.grid(row=3, column=1)  # Moved to the next row for better layout

    def on_select(self, event):
        selected_value = self.combo.get()
        self.stat.delete(0, tk.END)
        self.stat.insert(0, selected_value)  # Show selected value in entry field

root = tk.Tk()
root.title("Dropdown Example")
app = MyApp(root)
root.mainloop()

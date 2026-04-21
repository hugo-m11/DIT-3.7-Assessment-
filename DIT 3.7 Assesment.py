from tkinter import*

class SimpleGUI:
    def __init__(self, parent):
        
        self.name_var = StringVar()
        
        self.name_label = Label(parent, text="Name")
        self.name_label.pack()
        self.name_entry = Entry(parent, textvariable=self.name_var)
        self.name_entry.pack()



if __name__ == "__main__":
    root = Tk()
    gui = SimpleGUI(root)
    root.title("TAKEAWAY ORDERING SYSTEM")
    root.mainloop()




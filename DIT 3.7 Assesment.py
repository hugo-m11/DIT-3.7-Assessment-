from tkinter import*

class Menu_items:
#class that makes the menu items 
    def __init__(self, menu_item_name, price):
        self.menu_item_name = menu_item_name
        self.price = price
#function that allows to pass objects as strings 
    def __str__(self):
        return f"{self.menu_item_name} - ${self.price}"

class SimpleGUI:
    def __init__(self, parent):

#stores menu items as an attribute
        self.menu_items = [Menu_items("Burger", 17),
                      Menu_items("Cabbage and Lettuce", 18),
                      Menu_items("Chicken Tikka Mo Salah", 22),
                      Menu_items("50g of Rump Steak", 26),
                      Menu_items("Pesto Pasta", 27),
                      Menu_items("HUGE burger", 34),
                      Menu_items("Lobster agnolotti", 43)]   
        
#stores the varible selected from the dropdown list 
        self.list_val = StringVar()
        self.list_val.set(str(self.menu_items[0]))


        self.name_variable = StringVar()
        self.name_label = Label(parent, text="Name")
        self.name_label.pack()
        self.name_entry = Entry(parent, textvariable=self.name_variable)
        self.name_entry.pack()


#creates the dropdown list 
        self.option = OptionMenu(parent, self.list_val, *self.menu_items)
        self.option.pack() 
#button that runs the get selected item functio
        self.button = Button(parent, text="Get Selection", command=self.get_selectet_item)
        self.button.pack()

#checks to see if selected item is the same as the object created in the str function
    def get_selectet_item(self):
        selected_menu_item = self.list_val.get()

#loops through the list of menu_items to find matching object
        for item in self.menu_items:
            if str(item) == selected_menu_item:
                print(item.menu_item_name, item.price)

    

if __name__ == "__main__":



    root = Tk()
    gui = SimpleGUI(root)
    root.title("TAKEAWAY ORDERING SYSTEM")
    root.mainloop()




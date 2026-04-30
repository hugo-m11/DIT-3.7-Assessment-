from tkinter import*
from tkinter import messagebox
from tkinter.scrolledtext import*


class MenuItems:
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
        self.menu_items = [MenuItems("Burger", 17),
                           MenuItems("Cabbage and Lettuce", 18),
                           MenuItems("Chicken Tikka Mo Salah", 22),
                           MenuItems("50g of Rump Steak", 26),
                           MenuItems("Pesto Pasta", 27),
                           MenuItems("HUGE burger", 34),
                           MenuItems("Lobster agnolotti", 43)]    
        
#stores the varible selected from the dropdown list 
        self.list_val = StringVar()
        self.list_val.set(str(self.menu_items[0]))

#Where the user enters their name 
        self.name_variable = StringVar()
        self.name_label = Label(parent, text="Name")
        self.name_label.grid()
        self.name_entry = Entry(parent, textvariable=self.name_variable)
        self.name_entry.grid()


#creates the dropdown list 
        self.option = OptionMenu(parent, self.list_val, *self.menu_items)
        self.option.grid() 
#button that runs the get selected item functio
        self.button = Button(parent, text="Add Selection to order", command=self.get_selectet_item)
        self.button.grid()      
    

        self.display_user_order = ScrolledText(parent, width = 30, height = 10, state = 'disabled', wrap = 'word')
        self.display_user_order.grid(row = 6, columnspan = 2)

#checks to see if selected item is the same as the object created in the str function
    def get_selectet_item(self):

        user_order = []
        selected_menu_item = self.list_val.get()
        if self.name_entry.get() == "":
            messagebox.showerror("", "Please add an order name")
            return 
        user_order.append(selected_menu_item)
        
        self.display_user_order.configure(state = 'normal')
        
        for user in user_order:
            self.display_user_order.insert(END, str(user) + "\n")
            self.display_user_order.configure(state = 'disabled')


#loops through the list of menu_items to find matching object
        for item in self.menu_items:
            if str(item) == selected_menu_item:
                print(item.menu_item_name, item.price)
    
    def price_of_order():
        pass


if __name__ == "__main__":

    root = Tk()
    gui = SimpleGUI(root)
    root.geometry("238x250+200+200")
    root.title("TAKEAWAY ORDERING SYSTEM")
    root.mainloop()




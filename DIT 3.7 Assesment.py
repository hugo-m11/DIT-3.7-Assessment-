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
        return f"{self.menu_item_name} | ${self.price}"

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

# where the user enters their name 
        self.name_variable = StringVar()
        self.name_label = Label(parent, text="Name")
        self.name_label.grid()
        self.name_entry = Entry(parent, textvariable=self.name_variable)
        self.name_entry.grid()

#list where orders are stored
        self.user_order = []

# creates the dropdown list 
        self.option = OptionMenu(parent, self.list_val, *self.menu_items)
        self.option.grid() 
# button that runs the get selected item functio
        self.button = Button(parent, text="Add Selection to order", command=self.get_selectet_item)
        self.button.grid()      
    
# sets up the scroll window where the orders will be displayed 
        self.display_user_order = ScrolledText(parent, width = 30, height = 10, state = 'disabled', wrap = 'word')
        self.display_user_order.grid(row = 6, columnspan = 2)

# button where the user can get the total price of their order 
        self.get_price_of_order = Button(parent, text="Get Price", command=self.get_price)
        self.get_price_of_order.grid()

        self.actually_confirm_order = Button(parent, text="confirm order", command=self.confirm_order)
        self.actually_confirm_order.grid()

# checks to see if selected item is the same as the object created in the str function
    def get_selectet_item(self):

# gets the currently selected dropdown value (as a string)
        selected_menu_item = self.list_val.get()

# checks to see if the user inputted a name, if not a messagebox pops up     
        if self.name_entry.get() == "":
            messagebox.showerror("", "Please add an order name")
            return 
# adds the selected menu item to the overall list        
        self.user_order.append(selected_menu_item)
        
# unlocks the text box, inputs all ordered items into it, and locks it again in order to ensure the user can't edit it       
        self.display_user_order.configure(state = 'normal')
        self.display_user_order.insert(END, selected_menu_item + "\n")
        self.display_user_order.configure(state = 'disabled')

# loops through the list of menu_items to find matching object and prints
        for item in self.menu_items:
            if str(item) == selected_menu_item:
                print(item.menu_item_name, item.price)

# gets the price of the order
    def get_price(self):
        total_of_order = 0
        for order in self.user_order:
            for item in self.menu_items:
                if str(item) == order:
                    total_of_order += item.price
                    messagebox.showinfo("Total Price", f"Total Price of Order: ${total_of_order}")

# function for confirming order
    def confirm_order(self):

# allows the scroll text to be edited 
        self.display_user_order.configure(state='normal')
# adds a break in between orders 
        self.display_user_order.insert(END, "---------------------\n")
      
# shows a message thanking the user 
        messagebox.showinfo("", "Thank you for your order")

# clears the entry widget
        self.name_entry.delete(0, END)
        self.user_order.clear()
# locks the scroll text window 
        self.display_user_order.configure(state='disabled')

# mainloop
if __name__ == "__main__":

    root = Tk()
    gui = SimpleGUI(root)
    # sets window size
    root.geometry("238x300+200+200")
    # adds a window title
    root.title("TAKEAWAY ORDERING SYSTEM")
    # runs the mainloop
    root.mainloop()
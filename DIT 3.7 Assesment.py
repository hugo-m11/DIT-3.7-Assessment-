from tkinter import*

class Menu_items:
    #class that makes the menu items 
    def __init__(self, menu_item_name, price):
        self.menu_item_name = menu_item_name
        self.price = price

    def __str__(self):
        return f"{self.menu_item_name} - ${self.price}"

class SimpleGUI:
    def __init__(self, parent):

        #drop down list of food items 
        self.menu_items = [Menu_items("Burger", 17),
                      Menu_items("Cabbage and Lettuce", 18),
                      Menu_items("Chicken Tikka Mo Salah", 22),
                      Menu_items("50g of Rump Steak", 26),
                      Menu_items("Pesto Pasta", 27),
                      Menu_items("HUGE burger", 34),
                      Menu_items("Lobster agnolotti", 43)]   
        
         #label to enter order name
        self.list_val = StringVar()
        self.list_val.set(str(self.menu_items[0]))
        

        self.option = OptionMenu(parent, self.list_val, *self.menu_items)
        self.option.pack() 
        

        self.list_val = StringVar()
        self.list_val.set(self.menu_items[0])
        




if __name__ == "__main__":



    root = Tk()
    gui = SimpleGUI(root)
    root.title("TAKEAWAY ORDERING SYSTEM")
    root.mainloop()




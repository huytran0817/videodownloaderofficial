from tkinter import (Tk, ttk, Label, Frame, Button,
    Checkbutton, Radiobutton, IntVar, HORIZONTAL)

class  SimpleGUI(Tk):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.title("Food Order Form")
        self.minsize(300, 200)  # width, height
        self.geometry("400x350+50+50")
        self.setupWindow()

    def setupWindow(self):
        """ Set up the widgets."""
        title = Label(self, text="Food Order Form",
            font=('Helvetica', 20), bd=10)
        title.pack()

        line = ttk.Separator(self, orient=HORIZONTAL)
        line.pack(fill='x')

        order_label = Label(self, text="What would you like to order?", bd=10)
        order_label.pack(anchor='w')

        foods_list = ["Sandwich", "Salad", "Soup", "Pizza"]
        self.foods_dict = {}

        # Populate the dictionary with checkbutton widgets
        for  i, food_item in  enumerate(foods_list):

            # Set the text for each checkbutton
            self.foods_dict[food_item] = Checkbutton(self, text=food_item)

            # Create a new instance of IntVar() for each checkbutton
            self.foods_dict[food_item].var = IntVar()

            # Set the variable parameter of the checkbutton
            self.foods_dict[food_item]['variable'] = self.foods_dict[food_item].var

            # Arrange the checkbutton in the window
            self.foods_dict[food_item].pack(anchor='w')

        payment_label = Label(self, text="How do you want to pay?", bd=10)
        payment_label.pack(anchor='w')

        # Create integer variable
        self.var = IntVar()
        self.var.set(0)  # Use set() initialize the variable
        self.payment_methods = ["PayPal", "Credit Card", "Other"]

        for  i, method in  enumerate(self.payment_methods):
            self.pymt_method = Radiobutton(self, text=method, variable=self.var, value=i)
            self.pymt_method.pack(anchor='w')

        # Use ttk to add styling to button
        style = ttk.Style()
        style.configure('TButton', bg='skyblue', fg='white')

        # Create button that will call the method to display text and
        # close the program
        next_button = ttk.Button(self, text="Next", command=self.printResults)
        next_button.pack()

    def printResults(self):
        """Print the results of the checkboxes and radio buttons."""
        for  cb in  self.foods_dict.values():
            if  cb.var.get():
                print('Item selected: {}'.format(cb['text']))

        index = self.var.get()
        print("Payment method: {}".format(self.payment_methods[index]))
        self.quit()

if  __name__  ==  "__main__":
    app = SimpleGUI()
    app.mainloop()
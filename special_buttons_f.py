import tkinter



#...................................
class Special_Buttons(tkinter.Frame):

    def __init__(self,parent):

        self.parent = parent
        tkinter.Frame.__init__(self,parent,name="frame_Special_Buttons" ,height=30 , background='royal blue')

        # Add buttons here
        self.button1 = tkinter.Button(self, text="button1")
        self.button1.grid(row = 0, column = 0, pady=2, padx=2)

        self.button2 = tkinter.Button(self, text="button2")
        self.button2.grid(row = 0, column = 1, pady=2, padx=2)

        self.button3 = tkinter.Button(self, text="button3")
        self.button3.grid(row = 0, column = 2, pady=2, padx=2)

        self.custom_string = tkinter.Label(self, text="Custom String: ")
        self.custom_string.grid(row=0, column=3,pady=2, padx=2,sticky='e')
    
        self.custom_string_entry = tkinter.Entry(self, width=25)
        self.custom_string_entry.grid(row=0, column=4, padx=2, pady=2,sticky='we')


        
########## End of class Special_Buttons() ###################

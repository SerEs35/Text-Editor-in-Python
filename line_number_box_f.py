import tkinter

#...................................
class Line_Number_Box(tkinter.Frame):

    def __init__(self, parent):
        
        self.parent = parent
        
        tkinter.Frame.__init__(self,parent,
                               name="frame_Line_Number",
                               width=50,
                               background= 'light green')

        self.line_number = tkinter.Canvas(self, name="line_number", background= 'Wheat',width=50 , highlightthickness=0)
        self.line_number.pack(side='left', fill='y', expand=0)
        
########## End of class Line_Number_Box() ###################

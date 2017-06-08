import tkinter

#...................................
class Parameter_Box(tkinter.Frame):

    def __init__(self, parent):
        
        self.parent = parent
        tkinter.Frame.__init__(self,parent,
                               name="frame_Parameter_Box",
                               width=150,
                               background= 'light blue')

        
########## End of class Parameter_Box() ###################

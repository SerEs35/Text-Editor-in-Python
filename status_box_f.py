import tkinter

#...................................
class Status_Box(tkinter.Frame):

    def __init__(self, parent):
        
        self.parent = parent
        
        tkinter.Frame.__init__(self,parent,name="frame_Status_Bar" )

        self.cursor_info = tkinter.Label(self, text="Line: 1 | Column: 1" , background ='grey', foreground='white')
        self.cursor_info .pack(fill=None, expand = 0, side='right', anchor='se')
        

########## End of class Status_Box() ###################

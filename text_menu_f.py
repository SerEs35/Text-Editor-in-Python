import tkinter


#...................................
class Text_Menu(tkinter.Menu):

    #Constuctor
    def __init__(self, parent):
        tkinter.Menu.__init__(self,parent)
        
        self.parent = parent     #This is a reference to Core

        self.show_line_number = tkinter.BooleanVar()
        self.show_line_number.set(True)
        
        #********File Menu********
        self.file_menu = tkinter.Menu(self, tearoff=0)       #child File menu
        self.add_cascade(label='File',menu=self.file_menu)   #apply a cascaded list, linked to file_menu as parent

        self.file_menu.add_command(label="New File" , accelerator = 'Ctrl+N', command = self.parent.new_file)
        self.file_menu.add_command(label="Open File", accelerator = 'Ctrl+O', command = self.parent.open_file)
        self.file_menu.add_command(label="Save File", accelerator = 'Ctrl+S', command = self.parent.save)
        self.file_menu.add_command(label="Save As", accelerator = 'Ctrl+Shift+S', command = self.parent.save_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quit", accelerator = 'Alt+F4', command = self.parent.close_app)

        #********Edit Menu********
        self.edit_menu = tkinter.Menu(self, tearoff=0)       #child Edit menu
        self.add_cascade(label='Edit',menu=self.edit_menu)
        
        self.edit_menu.add_command(label="Undo", accelerator = 'Ctrl+Z', command = self.parent.undo)
        self.edit_menu.add_command(label="Redo", accelerator = 'Ctrl+Y', command = self.parent.redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", accelerator = 'Ctrl+X', command = self.parent.cut)
        self.edit_menu.add_command(label="Copy", accelerator = 'Ctrl+C', command = self.parent.copy)
        self.edit_menu.add_command(label="Paste", accelerator = 'Ctrl+V', command = self.parent.paste)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Select All", accelerator = 'Ctrl+A', command = self.parent.select_all)
        self.edit_menu.add_command(label="Find", accelerator = 'Ctrl+F', command = self.parent.find)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Comment Line")
        self.edit_menu.add_command(label="Uncomment Line")
        self.edit_menu.add_separator()        
        self.edit_menu.add_command(label="Insert Custom String")
        self.edit_menu.add_command(label="Remove Custom String")                            


        #********Options Menu********
        self.options_menu = tkinter.Menu(self, tearoff=0)
        self.add_cascade(label='Options',menu=self.options_menu)

        self.options_menu.add_checkbutton(label="Show Line Number",
                                          variable = self.show_line_number ,
                                          command = self.parent.on_content_changed)
        
        #********About Menu********
        self.about_menu = tkinter.Menu(self, tearoff=0)       #child About menu
        self.add_cascade(label='About',menu=self.about_menu)
        
        self.about_menu.add_command(label="About My Window")
        #***************************************************
                
########## End of class Text_Menu() ###################
        

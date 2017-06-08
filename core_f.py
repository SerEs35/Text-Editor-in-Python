#Text Editor
#Author: Sergio Espinal, 2017

#===========================================================
# Frame: "Core"                                       
#   |-----------------------------------------------------|
#   | Frame: "Menu"                                       |
#   | |-------------------------------------------------| |
#   | |  Menu: menu                                     | |
#   | |-------------------------------------------------| |
#   |-----------------------------------------------------|
#   | Frame: "Buttons"                                    |
#   | |-------------------------------------------------| |
#   | | Button: button_X                                | |
#   | |-------------------------------------------------| |
#   |--------------------|--------------------------------|
#   |Frame: "Component"  |Frame: "Text Area"              | 
#   | |----------------| | |--------|--------|----------| |
#   | |List Box: Param | | |Canvas: |Text:   |ScrollBar:| |
#   | |                | | |Line N  |text box|scroll bar| |
#   | |----------------| | |--------|--------|----------| |
#   |--------------------|--------------------------------|
#   | Frame: "Status Area"                                |
#   | |-------------------------------------------------| |
#   | |  Label: status                                  | |
#   | |-------------------------------------------------| |
#   |-----------------------------------------------------|
#
#===========================================================

#load libraries
#-------------
import tkinter             
import tkinter.filedialog
import os

#import find_window
#import parameter_box
#import special_buttons
#import text_box
#import text_menu
#import line_number_box
#import status_box

from find_window_f import Find_Window
from parameter_box_f import Parameter_Box
from special_buttons_f import Special_Buttons
from text_box_f import Text_Box
from text_menu_f import Text_Menu
from line_number_box_f import Line_Number_Box
from status_box_f import Status_Box

#-----------------------------------
#........Classes....................

class Core(tkinter.Tk):

    #Constructor for unique instance of Core
    def __init__(self):
        
        #Create the Top Window
        tkinter.Tk.__init__(self)
        self.geometry("480x320+300+100")
        self.PROGRAM_NAME = "My Text Edit"
        #self.title(self.PROGRAM_NAME)
        self.title('{} - {}'.format("Untitled.cir",self.PROGRAM_NAME))
        
        self.file_name = None    #empty variable for file handling
        self.input_file_name = None
        self.is_find_running = tkinter.BooleanVar()
        self.is_find_running = False

        
        #...........Setup Grid Weights.................
        self.grid_rowconfigure(0, weight=0)    #y
        self.grid_rowconfigure(1, weight=1)    #y
        self.grid_rowconfigure(2, weight=0)    #y   minsize = 18
        self.grid_columnconfigure(0, weight=0) #x   if weight = 0, they do not get wider
        self.grid_columnconfigure(1, weight=0) #x
        self.grid_columnconfigure(2, weight=1) #x
        #..............................................
        
        #Menu Object
        self.menu_bar = Text_Menu(self)
        self.configure(menu = self.menu_bar)

        #Special Buttons
        self.special_btns = Special_Buttons(self)
        self.special_btns.grid(row = 0, column=0 , columnspan=3,sticky ='we')
        
        #Parameter Object
        self.parameter_area = Parameter_Box(self)
        self.parameter_area.grid(row = 1, column=0 , sticky ='ns')

        #Line Number Object
        self.line_number = Line_Number_Box(self)
        self.line_number.grid(row = 1, column=1 , sticky ='nsw')

        #Text Box + Scroll Bar Object
        self.text_box = Text_Box(self)
        self.text_box.grid(row = 1, column=2, sticky ='nswe')

        #Status Bar Object
        self.status_bar = Status_Box(self)
        self.status_bar.grid(row = 2, column=0 , columnspan=3,sticky ='we')

        #Find Window Object
        #self.find_obj = Find_Window(self)
        self.find_obj = None

        #Bindings for Text and Scrollbar Widgets
        #-----------------------------------------------------------------------------

        self.text_box.content_text.bindtags(('mousew','Text','.frame_Text_Box.content_text','.','all'))
        
        self.text_box.content_text.bind('<Any-KeyPress>', self.on_content_changed)
        self.text_box.content_text.bind('<Configure>', self.on_window_resizing)
        self.text_box.content_text.bind_class('mousew','<MouseWheel>',self.my_yscroll)

        self.text_box.content_text.bind('<Control-a>', self.select_all)
        self.text_box.content_text.bind('<Control-A>', self.select_all)

        self.text_box.content_text.bind('<Control-f>', self.find)
        self.text_box.content_text.bind('<Control-F>', self.find)

        self.text_box.content_text.bind('<Button-3>', self.text_box.popup)
        self.text_box.content_text.bind('<Button-1>', self.update_cursor_info)

        # The following allows to move the scrollbar from text widget
        self.text_box.content_text.configure(yscrollcommand = self.text_box.scroll_bar.set)

        #The following allows to move text from scrollbar
        self.text_box.scroll_bar.configure(command=self.my_yview)

        #Binding for Canvas-----------------
        self.line_number.line_number.bind('<MouseWheel>',self.my_yscroll)

        #----------------------------------------------------

        def close_main_window():
            #TODO: Check if document has been modified, proceed to ask to save
            # We will use the following function for now...
            if self.text_box.content_text.edit_modified():
                self.save_as() 
            
            #Dereferencing members:
            #self.dereference_members()

            #delete window
            self.destroy()
        #----------------------------------------------------
            
        #override the close function with a callback
        self.protocol('WM_DELETE_WINDOW', close_main_window)
      
    #++++++++++++++++++++++++++++++++++++++++++++++++++
    def dereference_members(self):

        print("inside dereference")
        pprint.pprint(gc.get_referents(self))
        
        self.file_name = None
        self.input_file_name = None
        self.is_find_running = None
            
        self.menu_bar = None
        self.special_btns = None
        self.parameter_area = None
        self.line_number = None
        self.text_box = None
        self.status_bar = None
        self.find_obj = None
        
    #++++++++++++++++++++++++++++++++++++++++++++++++++
       
    def close_app(self):

        #TODO: Check if document has been modified, proceed to ask to save
        # We will use the following function for now...
        if self.text_box.content_text.edit_modified():
            self.save_as()       
       
        #self.dereference_members()
        self.destroy()
    #----------------------------------------------------
    def __enter__(self):
        return self
    #----------------------------------------------------
    def __exit__(self, type, value, traceback):
        if type is not None:
            print("Error on exit with statement")
            pass
        print("Core Terminated")
        
    #----------------------------------------------------
        
    #=========== Menu Functions ==============
    #.....File commands.....
     
    def open_file(self,event=None):
        self.input_file_name = tkinter.filedialog.askopenfilename(defaultextension="*.*",
                                                                  filetypes=[("SPICE Circuit Description File","*.cir"),
                                                                             ("All Files", "*.*"),
                                                                             ("Text Documents","*.txt")])

        if self.input_file_name:
            self.file_name = self.input_file_name
            self.title('{} - {}'.format(os.path.realpath(self.file_name),self.PROGRAM_NAME)) #resolves symbolic links "\...\"
            #root.title('{} - {}'.format(os.path.dirname(os.path.abspath(file_name)),PROGRAM_NAME))
  
            #use os.path.join() for path manipulation
               
            self.text_box.content_text.delete('1.0', 'end')
    
            with open(self.file_name) as _file:
                self.text_box.content_text.insert('1.0', _file.read())

        self.on_content_changed()
        #content_text.focus_set()

    #.....................
    def save(self,event=None):

        if not self.file_name:
            self.save_as()
        else:
            self.write_to_file(self.file_name)
        return "break"
    
    #.....................
    def save_as(self,event=None):
        self.input_file_name = tkinter.filedialog.asksaveasfilename(defaultextension="*.*",
                                                           filetypes=[("SPICE Circuit Description File","*.cir"),
                                                                      ("All Files", "*.*"),
                                                                      ("Text Documents","*.txt")])
        if self.input_file_name:

            self.file_name = self.input_file_name
            self.write_to_file(self.file_name)
            self.title('{} - {}'.format(os.path.realpath(self.file_name),self.PROGRAM_NAME))
 
        return "break"
                
    #.....................
    def write_to_file(self,file_name):
        try:
            content = self.text_box.content_text.get('1.0', 'end')
            with open(file_name, 'w') as the_file:
                the_file.write(content)
        except IOError:
            pass        
        # pass for now but must show some warning
        
    #.....................
    def new_file(self,event=None):
        self.title('{} - {}'.format("Untitled.cir",self.PROGRAM_NAME))

        self.file_name = None
        self.text_box.content_text.delete('1.0','end')

        self.on_content_changed()
        
    #.....................
    #...Edit Menu commands.....   
    def undo(self):
        self.text_box.content_text.event_generate("<<Undo>>")   #Needs some tweaking
        self.on_content_changed()
        
    #.....................
    def redo(self):
        self.text_box.content_text.event_generate("<<Redo>>")   #Needs some tweaking
        self.on_content_changed()
        return "break"
    
    #.....................
    def cut(self):
        self.text_box.content_text.event_generate("<<Cut>>")
        self.on_content_changed()
        
    #.....................
    def copy(self):
        self.text_box.content_text.event_generate("<<Copy>>")
        
    #.....................
    def paste(self):
        self.text_box.content_text.event_generate("<<Paste>>")
        self.on_content_changed()

    #.....................
    def select_all(self,event=None):
        self.text_box.content_text.tag_add('sel', '1.0', 'end')
        return "break"
    
    #.....................
    #Find...
    def find(self,event=None):    
    #TODO: Find a way to delete the class

        if self.is_find_running is False:
            
            self.is_find_running = True
            self.find_obj = Find_Window(self)
            #self.find_obj.create_window()

    #/////////////////////////////////////////////
    #....Other Functions....

    #.......................        
    def on_content_changed(self,event=None):

        self.update_cursor_info()
        
        if self.menu_bar.show_line_number.get() is True:
            
            self.text_box.content_text.update_idletasks()
            self.update_line_numbers()
            
        else:
            self.line_number.line_number.delete('all')
            
    #.....................
    def check_line_number(self):
        return "break" 
        self.on_content_changed()
    
    #.....................    
    def on_window_resizing(self,event=None):
        self.on_content_changed()
        return "break"
    
    #.....................
    def update_cursor_info(self,event=None):

        line, col = self.text_box.content_text.index('insert').split('.')
        position = "Line: {} | Column: {}".format(str(line),str(col))
        self.status_bar.cursor_info.configure(text = position)
    
    #.....................    
    def update_line_numbers(self,event = None):
          
        #set the scrollregion dynamically:
        self.line_number.line_number.configure(scrollregion=(0,0,
                                                             self.text_box.content_text.winfo_width(),
                                                             self.text_box.content_text.winfo_height()
                                                             ))
        #clear the canvas
        self.line_number.line_number.delete('all')

        i = self.text_box.content_text.index("1.0")
        dline = self.text_box.content_text.dlineinfo(i)

        while dline is None:
            #Move index i to next line
            i = self.text_box.content_text.index("%s+1line" % i)
            dline = self.text_box.content_text.dlineinfo(i)
           
        while dline is not None:
            #determine the absolute position of the line at text box
            y = dline[1]    
            coord = 4,y  #  x,y coord for writing the index on the canvas
        
            #Draw 'linenum[0]' at 'y' coordinate on Canvas            
            linenum = str(i).split(".")
            self.line_number.line_number.create_text(coord,anchor="nw", text=linenum[0])
        
            #Check for comments
            start_pos = i

            if self.text_box.content_text.get(start_pos) == '*':
            #Apply tags:
                self.text_box.content_text.tag_add('*', start_pos, str(start_pos)+' lineend')
            #    self.text_box.content_text.tag_config(symbol, foreground='green2')
            else:
            #Remove tags:
            #    self.text_box.content_text.tag_config(symbol, background= None)      
                self.text_box.content_text.tag_remove('*', start_pos, str(start_pos)+' lineend')

            #Move index i to next line   
            i = self.text_box.content_text.index("%s+1line" % i)
            dline = self.text_box.content_text.dlineinfo(i)
    
        #self.line_number.line_number.update_idletasks()
    #.....................
        
    # This is for using one scrollbar for two text widgets
    def my_yview(self,*args):

        self.text_box.content_text.yview(*args)
        self.on_content_changed()   
        return "break"
    #............................
    def my_yscroll(self,event):

        self.text_box.content_text.yview_scroll(-1*(int(event.delta/120)),'units')
        self.on_content_changed()    
        return "break" 
    #............................

    
########## End of class Core() ###################
    

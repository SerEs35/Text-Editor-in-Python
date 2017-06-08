import tkinter

#...................................
class Text_Box(tkinter.Frame):
    #constructor: create them in a frame
    def __init__(self, parent):

        self.parent = parent
        self.mouse_index = None
        tkinter.Frame.__init__(self,parent,name="frame_Text_Box")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.content_text = tkinter.Text(self, undo=True, wrap='word',
                                         state = 'normal',name = "content_text")
        
        self.content_text.grid(row = 0, column= 0, sticky = 'nsew')
        
        self.scroll_bar = tkinter.Scrollbar(self, orient='vertical', name= "scroll_bar")
        self.scroll_bar.grid(row = 0, column= 1, sticky = 'ns')


        #Right-Click Popup
        #----------------------------------------------
        self.mouse_menu_popup = tkinter.Menu(self,tearoff=0)
        
        self.mouse_menu_popup.add_command(label="Insert Custom String",command = lambda: self.insert_string(True))
        self.mouse_menu_popup.add_command(label="Remove Custom String",command = lambda: self.remove_string(True))
        
        self.mouse_menu_popup.add_separator()
        
        self.mouse_menu_popup.add_command(label="Comment line: '*'", command = lambda : self.comment_line(True))
        self.mouse_menu_popup.add_command(label="Uncomment line ", command = lambda : self.uncomment_line(True))
        
        
        #Tags
        #----------------------------------------------
        self.content_text.tag_config('*', foreground = 'green3')
        self.content_text.tag_config('s', foreground = 'red3')
        self.content_text.tag_config('match', background='yellow')
        self.content_text.tag_config('match_next', background='OliveDrab1')
        self.content_text.tag_config('match_prev', background='OliveDrab1')
        
    #.......................................
    def popup(self,event):
        print("popup event:"+str(event))
        
        #save index location:
        self.mouse_index = self.content_text.index('current')

        print("Pop up, Right CLK:" + self.mouse_index)
        self.mouse_menu_popup.post(event.x_root, event.y_root)

    #.......................................
    def insert_string(self,right_clk):
        #Insert the string at line entry:

        #if right_clk is True:
        #    start_pos = self.mouse_index  #Get mouse-line cursor index
        #else:
        #    start_pos = self.content_text.index('insert')  #Get the keyboard cursor position            

        start_pos = self.content_text.index('insert')  #Get the keyboard cursor position
        
        text = self.parent.special_btns.custom_string_entry.get()
        end_pos = '{}+{}c'.format(start_pos, len(text))
    
        self.content_text.insert(start_pos, text)
        self.parent.text_box.content_text.tag_add('s', start_pos, end_pos)
        
        #place line feed cursor here        
        self.parent.text_box.content_text.mark_set('insert',end_pos)
        self.parent.on_content_changed()
        
    #.......................................        
    def remove_string(self,right_clk):
        #Insert the string at line entry:
        
        #Save cursor position
        line, col = self.content_text.index('insert').split('.')
        
        if right_clk is True:
    
            #start_pos = self.content_text.index('current linestart')  #Get mouse-row cursor index
            start_pos = self.content_text.index(self.mouse_index+'linestart')
        else:
            start_pos = self.content_text.index('insert linestart')  #Get the keyboard cursor row's position

        #Search for the string in the line, and remove 'comment' tagged chars in line:
        #Check if there is really a tagged text, else tuple returns one value: 0
        
        head_tail = self.content_text.tag_nextrange('s', start_pos)  #it is a type tuple class
        
        if len(head_tail) is not 0:            
            self.content_text.delete(head_tail[0], head_tail[1])

            self.content_text.mark_set('insert','{}.{}'.format(line,col))
            self.parent.on_content_changed()
        
    #.......................................        
    def comment_line(self,right_clk):
        #Insert '*' at the beginning of line 'L':

        #Save cursor position
        line, col = self.content_text.index('insert').split('.')
        
        if right_clk is True:

            #start_pos = self.content_text.index('current linestart')  #Get mouse-line cursor index
            start_pos = self.content_text.index(self.mouse_index+'linestart')

        else:
            start_pos = '{}.0'.format(line)  #We just need the row            
            
        symbol = '*'
        end_pos = '{}+{}c'.format(start_pos, len(symbol))
        
        self.content_text.insert(start_pos, symbol)

        #restore cursor position       
        self.content_text.mark_set('insert','{}.{}'.format(line,col))
        self.parent.on_content_changed()

    #.......................................        
    def uncomment_line(self,right_clk):
        #Remove '*' at line entry, if any:

        #Save cursor position
        line, col = self.content_text.index('insert').split('.')

        if right_clk is True:

            #start_pos = self.content_text.index('current linestart')  #Get mouse-line cursor index
            start_pos = self.content_text.index(self.mouse_index+'linestart')

        else:
            start_pos = '{}.0'.format(line)  #We just need the row            
           
        symbol = '*'
        end_pos = '{}+{}c'.format(start_pos, len(symbol))
        
        #check if at line.0 the character is '*'
        if self.content_text.get(start_pos) == symbol:
            self.content_text.delete(start_pos,end_pos)

            #restore cursor position
            self.content_text.mark_set('insert','{}.{}'.format(line,col))        
            self.parent.on_content_changed()

########## End of class Text_Box() ###################

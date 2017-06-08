#Class Find_Window
#---------------------------------
import tkinter             

#---------------------------------


class Find_Window(tkinter.Toplevel):

    def __init__(self,parent):

        #Variable members:
        self.parent = parent   
        self.is_case_sensitive = tkinter.IntVar() # could be bool too

    #def create_window(self,parent):
    #def create_window(self):
        
        #Create the Top Window
        tkinter.Toplevel.__init__(self, name = "toplevel_find_obj")
        
        self.title('Find Text')
        self.transient(self.parent)
        self.resizable(False, False)
    
        #position the widget when it pops up
        self.wm_geometry("+%d+%d" % (self.parent.winfo_rootx()+10,
                                     self.parent.winfo_rooty()+10))

        #place the elements on the widget
        self.find_label = tkinter.Label(self, text="Find:")
        self.find_label.grid(row=0, column=0,sticky='e')
    
        self.find_entry = tkinter.Entry(self, width=25)
        self.find_entry.grid(row=0, column=1, padx=2, pady=2,sticky='we')
        self.find_entry.focus_set()

        self.find_checkbtn = tkinter.Checkbutton(self, text='Ignore Case',variable=self.is_case_sensitive)
        self.find_checkbtn.grid(row=1,column=1, sticky='w', padx=2, pady=2)

        self.result_label = tkinter.Label(self, text=None)
        self.result_label.grid(row=2,column=1, sticky='w', padx=2, pady=2)
    
        #---------------------------------------------------
        #find all...
        self.find_all_button = tkinter.Button(self, text="Find All",
                                              command =lambda: self.find_all_output(self.find_entry.get()))
    
        self.find_all_button.grid(row=0, column=2, sticky='ew', padx=2, pady=2)
    
        #---------------------------------------------------
        #previous if any...
        self.find_previous_button =tkinter.Button(self, text="Previous",
                                                  command =lambda: self.find_previous(self.find_entry.get()))
        
        self.find_previous_button.grid(row=1, column=2, sticky='ew', padx=2, pady=2)
    
        #next if any...
        self.find_next_button =tkinter.Button(self, text="Next",
                                              command =lambda: self.find_next(self.find_entry.get()))
        
        self.find_next_button.grid(row=2, column=2, sticky='ew', padx=2, pady=2)    

        #----------------------------------------------------

        def close_search_window():
            #clear tag
            #content_text.tag_remove('match', '1.0', 'end')
            self.parent.text_box.content_text.tag_delete('match','match_next','match_previous')

            #reset the flag
            self.parent.is_find_running = False

            #Dereferencing members:
           
            #for widget in self.winfo_children():            
                #widget = None
                #widget.destroy()

            self.find_label = None
            self.find_entry = None
            self.find_checkbtn = None
            self.result_label = None
            self.find_all_button = None
            self.find_previous_button = None
            self.find_next_button = None
            
            self.is_case_sensitive = None
            self.parent = None

            #delete window
            self.destroy()
        #----------------------------------------------------
            
        #override the close function with a callback
        self.protocol('WM_DELETE_WINDOW', close_search_window)
    
        #---------------------------------------------------
    #.....................        

    #.....................
    def find_all_output(self,text_to_search):

        #clear tag
        self.parent.text_box.content_text.tag_remove('match', '1.0', 'end')
        matches_found = 0

        if text_to_search:
                
            start_pos = '1.0'
        
            while True:
            #Search forward
                start_pos = self.parent.text_box.content_text.search(text_to_search,
                                                                  start_pos,
                                                                  nocase = self.is_case_sensitive,
                                                                  stopindex='end')
                if not start_pos:
                    break
                #tag all occurrences
                #set end index
                end_pos = '{}+{}c'.format(start_pos, len(text_to_search)) 
               
                self.parent.text_box.content_text.tag_add('match', start_pos, end_pos)
                matches_found += 1

                #move start index forward
                start_pos = end_pos
        
                self.focus_set()
                self.result_label.configure(text='{} matches found'.format(matches_found))

    #.....................

    def clear_tags_marks(self):
        self.parent.text_box.content_text.tag_delete('sel','match','match_next','match_prev')
        self.parent.text_box.content_text.tag_remove('sel', '1.0', 'end')

    #.....................                    

    def find_next(self,text_to_search):

        #Clear all tags and marks
        self.clear_tags_marks()
    
        start_pos = self.parent.text_box.content_text.search(text_to_search,
                                                      self.parent.text_box.content_text.index('insert'),
                                                      nocase = self.is_case_sensitive,
                                                      stopindex='end')
        if start_pos:

            end_pos = '{}+{}c'.format(start_pos, len(text_to_search))
        
            self.highlight_match(start_pos,end_pos,"next")
        
            #place insert cursor here        
            self.parent.text_box.content_text.mark_set('insert',end_pos)  #here use the end_pos for next

    #.....................    
    def find_previous(self,text_to_search):
    
        #TODO: validate if cursor is at 1.0 or at the END
    
        self.clear_tags_marks()
    
        start_pos = self.parent.text_box.content_text.search(text_to_search,
                                                      self.parent.text_box.content_text.index('insert'),
                                                      backwards= True,
                                                      nocase = self.is_case_sensitive,
                                                      stopindex='1.0')
        if start_pos:

            end_pos = '{}+{}c'.format(start_pos, len(text_to_search))
        
            self.highlight_match(start_pos,end_pos,"prev")

            #place insert cursor here
            self.parent.text_box.content_text.mark_set('insert',start_pos)  #here use the start_pos for previous

    #.....................
    def highlight_match(self,start_pos,end_pos,direction):

        #jump to line
        self.parent.text_box.content_text.see(start_pos)
        #select text
        self.parent.text_box.content_text.tag_add('sel', start_pos, end_pos)

        #highlight with a color
        text = "match_"+direction
        self.parent.text_box.content_text.tag_add(text, start_pos, end_pos)

    #.....................

########## End of class Find_Window() ################### 

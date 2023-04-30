import os,sys,subprocess

#===================handle_functions====================#
try:
    from handle_functions import *
except: 
    print("Cannot import required handle_functions!")
    debug__(getframeinfo(currentframe()))
    sys.exit()

#===================handle_functions====================#
try:
    from tab_scrape import *
    from tab_info import *
except: 
    print("Cannot import required tab_scrape!")
    debug__(getframeinfo(currentframe()))
    sys.exit()

#=================tkinter======================#
try:
    from tkinter import Tk,ttk,messagebox,IntVar,StringVar
except: 
    print("Cannot import required Tkinter!")
    debug__(getframeinfo(currentframe()))
    sys.exit()


class WebScrape(Tk):
    def __init__(self):
        super().__init__()
        
        """init window basic info"""
        width = 1024
        height = 640
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        #create screen align string to set appearance at center of current window
        align_str = '%dx%d+%d+%d' % (width,height,(screen_width-width)/2,(screen_height-height)/2)
        self.geometry(align_str)
        self.resizable(False,False)

        #set title
        self.title(f"Web scrape")


        # call tab GUI
        tabs_control = ttk.Notebook(self)
        threaded(tabs_control.add(tab_scrape(tabs_control),text="scraping",padding=5))
        threaded(tabs_control.add(tab_info(tabs_control),text="info",padding=5))
        # tab_scrape(tabs_control)
        # tab_info(tabs_control)
        tabs_control.pack(expand=1,fill="both",padx=3,pady=3)


if __name__=="__main__":

    init_vars()
    
    main_gui = WebScrape()
    main_gui.mainloop()

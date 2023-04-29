#===================handle_functions====================#
try:
    from handle_functions import *
except: 
    debug__(getframeinfo(currentframe()))
    print("Cannot import required handle_functions!")
    sys.exit()

#=================tkinter======================#
try:
    from tkinter import Tk,ttk,messagebox,IntVar,StringVar
except: 
    print("Cannot import required Tkinter!")
    sys.exit()


class tab_scrape(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.GUI_tab_scrape()
    
    def GUI_tab_scrape(self):

        # create frame for tab
        self.frame_above = ttk.Frame(self,height=80)
        self.frame_under = ttk.Frame(self,height=80)

        #item for frame_above
        self.label_link = ttk.Label(self.frame_above,text="Web Link",foreground='#00796b')
        self.entry_link = ttk.Entry(self.frame_above)

        self.label_link.pack(side="left",fill="x",padx=(40,10),pady=(10,3))
        self.entry_link.pack(side="left",fill="x",padx=(40,100),pady=(10,3),expand=1)

        #item for frame_under
        self.label_keywords = ttk.Label(self.frame_under,text="Keywords",foreground='#f9a825')
        self.entry_keywords = ttk.Entry(self.frame_under)

        self.label_keywords.pack(side="left",fill="x",padx=(40,10),pady=(10,3))
        self.entry_keywords.pack(side="left",fill="x",padx=(40,100),pady=(10,3),expand=1)

        #packing frames
        self.frame_above.pack(fill="both",anchor="center")
        self.frame_under.pack(fill="both",anchor="center")

        self.btn_scrape = ttk.Button(self,text="Scraping",command=self.scrape)
        self.btn_scrape.pack(padx=(800,100),pady=(10,3),expand=0)

    def scrape(self):
        try:
            link = str(self.entry_link.get()).strip()
            keywords = str(self.entry_keywords.get()).strip()
        except:
            debug__(getframeinfo(currentframe()))
            return

        if ((link!='') and (keywords !='')):
            if (";" in keywords):
                keywords = keywords.split(";")
            self.label_link['foreground'] = "#000000"
            self.label_keywords['foreground'] = "#000000"


        self.label_link['foreground'] = "#00796b"
        self.label_keywords['foreground'] = "#f9a825"
#===================handle_functions====================#
try:
    from handle_functions import *
except: 
    debug__(getframeinfo(currentframe()))
    print("Cannot import required handle_functions!")
    sys.exit()

#=================tkinter======================#
try:
    from tkinter import Tk,ttk,messagebox,IntVar,StringVar,Text
except: 
    print("Cannot import required Tkinter!")
    sys.exit()


class tab_scrape(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.GUI_tab_scrape()
    
    def GUI_tab_scrape(self):

        self.check_vars = IntVar()
        self.username = StringVar()
        self.password = StringVar()

        # create frame for tab
        self.frame_link = ttk.Frame(self,height=40)
        self.frame_keywords = ttk.Frame(self,height=40)
        self.frame_authen = ttk.Frame(self,height=40)

        self.label_link = ttk.Label(self.frame_link,text="Web Link",foreground='#00796b')
        self.entry_link = ttk.Entry(self.frame_link)
        self.label_link.pack(side = "left",fill="x",padx=(40,10),pady=(10,3))
        self.entry_link.pack(side = "left",fill="x",padx=(40,100),pady=(10,3),expand=1)

        self.label_keywords = ttk.Label(self.frame_keywords,text="Keywords",foreground='#f9a825')
        self.entry_keywords = ttk.Entry(self.frame_keywords)
        self.label_keywords.pack(side = "left",fill="x",padx=(40,10),pady=(10,3))
        self.entry_keywords.pack(side = "left",fill="x",padx=(40,100),pady=(10,3),expand=1)
        

        #item for frame_under
        self.label_username = ttk.Label(self.frame_authen,text="User name")
        self.entry_username = ttk.Entry(self.frame_authen,state="disabled")
        self.label_password = ttk.Label(self.frame_authen,text="Password")
        self.entry_password = ttk.Entry(self.frame_authen,state="disabled")
        self.check_authen = ttk.Checkbutton(self.frame_authen,text="Authen",command=self.authen_click,variable=self.check_vars,takefocus = 0)

        self.label_username.pack(side="left",fill="x",padx=(40,10),pady=(10,3))
        self.entry_username.pack(side="left",fill="x",padx=(30,100),pady=(10,3))
        self.label_password.pack(side="left",fill="x",padx=(40,10),pady=(10,3))
        self.entry_password.pack(side="left",fill="x",padx=(30,100),pady=(10,3))
        self.check_authen.pack(side="left",fill="x",padx=(40,100),pady=(10,3))

        #packing frames
        self.frame_link.pack(fill="both",anchor="center")
        self.frame_keywords.pack(fill="both",anchor="center")
        self.frame_authen.pack(fill="both",anchor="center")

        self.btn_scrape = ttk.Button(self,text="Scraping",command=self.scrape)
        self.btn_scrape.pack(padx=(800,100),pady=(10,3),expand=0)

        self.txt_result = Text(self,background="#e0e0e0")
        self.txt_result.pack(fill="both",padx=(39,50),pady=(30,50),expand=0)


    def authen_click(self):
        if self.check_vars.get():
            self.entry_username["state"] = ("enabled")
            self.entry_password["state"] = ("enabled")
        else:
            self.entry_username["state"] = ("disabled")
            self.entry_password["state"] = ("disabled")


    def scrape(self):

        self.btn_scrape["state"] = "disabled"
        try:
            link = str(self.entry_link.get()).strip()
            keywords = str(self.entry_keywords.get()).strip()
        except:
            debug__(getframeinfo(currentframe()))
            return
        if self.check_vars:
            self.username = str(self.entry_username.get())
            self.password = str(self.entry_password.get())

        if ((link!='') and (keywords !='')):
            if (";" in keywords):
                keywords = keywords.split(";")
            self.label_link['foreground'] = "#000000"
            self.label_keywords['foreground'] = "#000000"

            if self.check_vars:
                find_contents(link,keywords,self.username,self.password)
            else:
                find_contents(link,keywords)



        self.label_link['foreground'] = "#00796b"
        self.label_keywords['foreground'] = "#f9a825"

        # self.txt_result.insert(1.0,link+"\n"+keywords+"\n","end")
        # self.txt_result.insert('end',self.username+"\n"+self.password+"\n","end")

        self.btn_scrape["state"] = "enabled"

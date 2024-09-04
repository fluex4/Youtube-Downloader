import io
import tkinter
import tkinter.messagebox
import customtkinter
from pytube import YouTube
from urllib.request import urlopen
from PIL import Image, ImageTk
import webbrowser




customtkinter.set_default_color_theme("dark-blue")  
customtkinter.set_appearance_mode("system")


class getVid(YouTube):
    def __init__(self,url):
        try:
            self.yt=YouTube(url=url)
        except Exception as e:
            tkinter.messagebox.showerror("Error",e)
class InnerFrame(customtkinter.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

    def update(self,url):

        self.url=url
        self.vid=getVid(url)

        self.vid_title=customtkinter.CTkLabel(self,text="",font=("Roboto", 13, "bold"),padx=40,pady=10)
        info = f"Title: "+ self.vid.yt.title +"\nChannel Name: "+ self.vid.yt.author +"\nViews :" + str(self.vid.yt.views)
        self.vid_title.configure(text=info)
        self.vid_title.place(x=20,y=50)

        


        self.redir=customtkinter.CTkButton(self,text="Open in Browser",command=self.open,width=40)
        self.redir.place(x=520,y=30)

        self.redir=customtkinter.CTkButton(self,text="Show Thumbnail",command=self.openthumb,width=40)
        self.redir.place(x=520,y=60)

        self.download_button=customtkinter.CTkButton(self,text="Download",command=self.download,width=40)
        self.download_button.place(x=520,y=90)

    def open(self):
        webbrowser.open_new(self.url)

    def openthumb(self):
        webbrowser.open_new(self.vid.yt.thumbnail_url)

    def download(self):
        # streams = self.vid.yt.streams.filter(progressive=True)
        video=self.vid.yt.streams.get_highest_resolution()
        video.download()


class InfoFrame(customtkinter.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

        title="Youtube Downloader"
        info="made by fluexxx"

        self.title=customtkinter.CTkLabel(self,text=title,font=("Roboto",30,"bold"),padx=40,pady=10)
        self.title.place(x=5,y=30)

        self.info=customtkinter.CTkLabel(self,text=info,font=("Roboto",15),padx=40,pady=10)
        self.info.place(x=8,y=70)

        self.github=customtkinter


class TopFrame(customtkinter.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

        self.search=customtkinter.CTkEntry(self,placeholder_text="Search",width=370)
        self.search.place(x=30,y=10)

        self.go=customtkinter.CTkButton(self,text="Search",width=40,command=self.go_btn).place(x=410,y=10)

        self.inner=InnerFrame(master=self,width=680,height=300) 

        self.inFr = InfoFrame(self,width=680,height=300)
        self.inFr.pack(padx=20,pady=(50,0))
        
        


    def go_btn(self):
        self.inFr.destroy()
        self.inner.pack(padx=20,pady=(50,0))
        self.inner.update(str(self.search.get()))


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("720x400")
        self.grid_rowconfigure(0, weight=1)  
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = TopFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


try:
    app = App()
    app.mainloop()
except Exception as e:
    tkinter.messagebox.showerror("Error Occoured",e)
# yt=YouTube('https://youtu.be/0WtRNGubWGA?si=gcbIGZyzKu7jwScC')
# print(yt.title)
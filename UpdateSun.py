from tkinter import *
from tkinter.ttk import Progressbar
import os, shutil
from zipfile import ZipFile
from urllib import request
from tqdm import tqdm
import time

class UpdateSun:
    def __init__(self):
        self.display= Tk()
        self.debug= 1
        self.display.geometry("500x500")
        self.display.title("Sunshine Instalador")
        self.display.config(bg="orange",padx="30px", pady="30px")
        self.label0= Label(self.display, text=f"Olá {os.getlogin()}", bg="orange", fg="white", font="Arial 21 bold")
        self.label0.pack(pady="20px")
        self.label= Label(self.display, text="Iniciando...", bg="orange", fg="white", font="Arial 19 bold")
        self.label.pack(pady="20px")
        self.progressbar= Progressbar(self.display, orient="horizontal", maximum="100", length=500, mode="determinate")
        self.progressbar.pack()
        time.sleep(1)
        self.pcent= Label(self.display, text="0%", bg="orange", fg="white", font="Arial 19 bold")
        self.pcent.pack(pady="20px")
        self.download()
        self.extract()
        self.removeDir()
        self.display.mainloop()
    def download(self):
        self.label["text"]= "Fazendo download..."
        while self.debug:
            x= request.urlretrieve("https://github.com/gstechcode/Sunshine/archive/refs/heads/aplicativo.zip",f"{os.environ['USERPROFILE']}/Downloads/Sunshine.zip", self.Ldownload) 
    def Ldownload(self, blocknum, blocksize, totalsize):
        self.display.update()
        if(totalsize == -1):
            self.debug= 1
            return 0
        pcent= (blocknum*blocksize/totalsize) * 100
        self.progressbar["value"]= pcent
        self.pcent["text"]= f"{int(pcent)}%"
        self.debug= 0
    def extract(self):
        self.label["text"]= "Extraindo arquivos..."
        self.progressbar["value"]= 0
        loading= []
        filetoextract = f"{os.environ['USERPROFILE']}/Downloads/Sunshine.zip"
        with ZipFile(filetoextract,"r") as zip_ref:
            for file in tqdm(iterable=zip_ref.namelist(), total=len(zip_ref.namelist()), disable= True):
                totalsize= len(zip_ref.namelist())
                loading.append(file)
                quantloading= len(loading)
                pcent=  (quantloading/totalsize) * 100
                zip_ref.extract(member=file, path=f"{os.environ['USERPROFILE']}/Downloads")
                self.progressbar["value"]= pcent
                self.pcent["text"]= f"{int(pcent)}%"
                self.display.update()
        os.rename(f"{os.environ['USERPROFILE']}/Downloads/Sunshine-aplicativo",f"{os.environ['USERPROFILE']}/Downloads/Sunshine")
        if(os.path.exists(os.environ["USERPROFILE"] + "/Sunshine")):
            shutil.rmtree(f"{os.environ['USERPROFILE']}/Sunshine")
        shutil.move(f"{os.environ['USERPROFILE']}/Downloads/Sunshine",f"{os.environ['USERPROFILE']}/Sunshine")
    def removeDir(self):
        self.display.update()
        self.progressbar["value"] = 0
        self.pcent["text"]= "0%"
        self.label["text"]= "Removendo arquivos resíduais..."
        os.remove(f"{os.environ['USERPROFILE']}/Downloads/Sunshine.zip")
        self.progressbar["value"] = 100
        self.pcent["text"]= "100%"
        self.display.update()
        self.display.destroy()

x= UpdateSun()
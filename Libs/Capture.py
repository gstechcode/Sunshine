from tkinter import *
from tkinter import messagebox
import sys
from Resources import Resolution as f
import pyautogui as p
import sys, shutil, os, json

class CaptureView(f.functions):
    def __init__(self,master):
        self.loadCoords()
        self.path= master["path"]
        super().__init__()
        self.master= master
        self.capture()
    def loadCoordsEst(self):
        arquivo= open(os.environ["USERPROFILE"] + "\\Sunshine\\coords.json","r")
        self.stCoords= json.loads(arquivo.readlines()[0])
        arquivo.close()
    def capture(self):
        while True:
            self.captFront()
            self.captBack()
            self.captLeft90()
            self.captLeft45()
            self.captRight90()
            self.captRight45()
            op= p.confirm(title="Deu tudo certo?", text="", buttons=["Sim","Não"])
            if(op == "Sim"):
                break
        if(self.master["sup"] != "0" or self.master["diagnostico"] == True):
            self.captOclSup("sup")
            self.captOclSup("sob")
            self.captOclSup("ipr")
        if(self.master["inf"] != "0" or self.master["diagnostico"] == True):
            self.captOclInf("inf")
            self.captOclInf("sob")
            self.captOclInf("ipr")
        p.confirm(title="Pronto para o estagiamento?", text="", buttons=["Pronto"])
        while 1:
            if(self.master["diagnostico"] == True):
                self.estCapt("SIM","Tabela")
            elif(self.master["sup"] == "0" and self.master["inf"] != "0"):
                self.estCapt("SIM","Inferior")
            elif(self.master["sup"] != "0" and self.master["inf"] == "0"):
                self.estCapt("SIM","Superior")
            elif(self.master["sup"] != "0" and self.master["inf"] != "0"):
                self.estCapt("SIM","Ambas")
            else:
                self.estCapt("SIM","Tabela")
            repeatEst= p.confirm(title="Quer repetir o estagiamento?", text="", buttons=["SIM","NAO"])
            if(repeatEst == "NAO"):
                break
            else:
                p.click(600,80)
        if(self.master["sup"] != "0" or self.master["diagnostico"] == True):
            shutil.copy(os.environ["USERPROFILE"] + "\\Sunshine\\Images\\tmp\\5.png", self.master["path"] + "\\05 - Sobreposicao " + self.master["setup"] + " Superior - " + self.master["paciente"] + ".png")
        if(self.master["inf"] != "0" or self.master["diagnostico"] == True):
            shutil.copy(os.environ["USERPROFILE"] + "\\Sunshine\\Images\\tmp\\6.png", self.master["path"] + "\\06 - Sobreposicao " + self.master["setup"] + " Inferior - " + self.master["paciente"] + ".png")


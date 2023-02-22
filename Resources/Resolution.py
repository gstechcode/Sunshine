from Resources import settings as s
import pyautogui as p
import time as t
from tkinter import *
import os, json
import win32api
import win32gui

class functions(s.settings):
    def __init__(self):
        self.loadCoords()
        super().__init__()
        p.PAUSE= 0.05
    def loadCoords(self):
        k= Tk()
        self.widthquad= k.winfo_screenwidth()
        self.heightquad= k.winfo_screenheight()
        k.destroy()
        arquivo = open(os.environ["USERPROFILE"] + "\\Sunshine\\coords.json", "r")
        self.coords= json.loads(arquivo.readlines()[0])
    def Sobrepos(self,btn):
        if(btn == "on"):
            p.click(self.coords["SobreposicaoON"])
        else:
            p.click(self.coords["SobreposicaoOFF"])
    def Transp(self,btn):
        t.sleep(1)
        if(btn == "on"):
            p.click(self.coords["TransparenciaON"])
        else:
            p.click(self.coords["TransparenciaOFF"])
    def IPR(self, btn):
        t.sleep(3)
        if(btn == "on"):
            p.PAUSE=1
            self.DownMenu()
            p.click(self.coords["IconeIPR"], clicks=1)
            p.click(self.coords["IPRONOFF"])
            self.Transp("on")
            self.Dist("on")
            p.PAUSE= 0.5
        else:
            p.PAUSE= 1
            p.click(self.coords["DISTOFF"])
            p.click(self.coords["IconeIPR2"], clicks=1)
            t.sleep(2)
            p.click(self.coords["IPRONOFF2"])
            p.PAUSE= 0.5
    def Dist(self,btn):
        if(btn == "off"):
            p.click(self.coords["IconeDIST"])
            p.click(self.coords["DISTOFF"])
        else:
            p.click(self.coords["IconeDIST"])
            p.click(self.coords["DISTON"])
    def DownMenu(self):
        p.click(self.coords["FINALMENU"], clicks=1)
    def Photo(self,text):
        p.click(self.coords["ICONEFOTO"])
        p.write(text)
        p.press(["tab","tab","tab"])
        p.press("enter")
    def SobreposPhoto(self,op):
        if(op == "sup"):
            p.alert(title="Atenção", text="Você tem 5 segundos para marcar sobreposição")
            t.sleep(5)
            self.Photo("Vista Oclusal Superior com Sobreposicao")
        else:
            p.alert(title="Atenção", text="Você tem 5 segundos para marcar sobreposição")
            t.sleep(5)
            self.Photo("Vista Oclusal Inferior com Sobreposicao")
    def question(self):
        x= p.confirm(title="Tem IPR?",text="",buttons=["SIM","NAO"])
        return x
    def IPRPhoto(self,op):
        p.PAUSE= 0.2
        if(op == "sup"):
            p.alert(title="Atenção", text="Marcou o IPR?")
            x= self.question()
            if(x == "SIM"):
                self.Photo("Vista Oclusal Superior com indicacao IPR")
            else:
                self.Photo("Vista Oclusal Superior sem indicacao IPR")
        else:
            p.alert(title="Atenção", text="Marcou o IPR?")
            x= self.question()
            if(x == "SIM"):
                self.Photo("Vista Oclusal Inferior com indicacao IPR")
            else:
                self.Photo("Vista Oclusal Inferior sem indicacao IPR")
    def Menu(self,btn):
        if(btn == "Otop"):
            p.click(self.coords["VOCLSUP"])
        elif(btn == "Oinf"):
            p.click(self.coords["VOCLINF"])
        elif(btn == "Right"):
            p.click(self.coords["VOCLRIGHT"])
        elif(btn == "Left"):
            p.click(self.coords["VOCLLEFT"])
        elif(btn == "Front"):
            p.click(self.coords["VOCLFRONT"])
        elif(btn == "Post"):
            p.click(self.coords["VOCLBACK"])
        
    def Mand(self,btn):
        if(btn == "off"):
            p.click(self.coords["MANDOFF"])
        else:
            p.click(self.coords["MANDON"])
    def Max(self,btn):
        if(btn == "off"):
            p.click(self.coords["MAXOFF"])
        else:
            p.click(self.coords["MAXON"])
    def Enquadrar(self, mid= False):
        initquad= self.coords["QUAD"]
        #x + 18,75% - 80%
        #y + 8% - 88%
        finalquad= [0,0]
        finalquad[0] = initquad[0] + int((self.widthquad * 61.25)/100)
        finalquad[1] = initquad[1] + int((self.heightquad * 80)/100)
        midcoordY= int(initquad[1] + ((finalquad[1] - initquad[1])/2))
        midcoordX= int(initquad[0] + ((finalquad[0] - initquad[0])/2))

        self.midcoord= [midcoordX,midcoordY]

        self.initquad= initquad
        self.finalquad= finalquad
        self.screenCoord= (self.initquad[0],self.initquad[1],self.finalquad[0] - self.initquad[0],self.finalquad[1] - self.initquad[1])

        aux= 0
        dc = win32gui.GetDC(0)
        while True:
            win32gui.MoveToEx(dc,initquad[0],initquad[1])
            win32gui.LineTo(dc,finalquad[0],initquad[1])

            win32gui.MoveToEx(dc,initquad[0],initquad[1])
            win32gui.LineTo(dc,initquad[0],finalquad[1])

            win32gui.MoveToEx(dc,initquad[0],finalquad[1])
            win32gui.LineTo(dc,finalquad[0],finalquad[1])

            win32gui.MoveToEx(dc,finalquad[0],initquad[1])
            win32gui.LineTo(dc,finalquad[0],finalquad[1])

            if(mid):
                win32gui.MoveToEx(dc,initquad[0],midcoordY)
                win32gui.LineTo(dc,finalquad[0],midcoordY)
            aux += 1
            print(aux)
            if(aux == 60):
                break
    def captFront(self):
        p.click(self.coords["ARCSOPEN"])
        p.alert(title="Atenção", text="Ajuste a posição inicial, alinhe com a linha desenhada na tela")

        self.Enquadrar(mid= True)

        t.sleep(3)
        self.Photo("Vista Oclusao Anterior")
        t.sleep(2)
        p.screenshot(region= self.screenCoord).save(os.environ["USERPROFILE"] + "\\Sunshine\\Images\\tmp\\7F.png")
        t.sleep(1)
        #captura essa foto
    def captBack(self):
        p.moveTo(self.midcoord)
        p.moveTo(self.midcoord)
        p.moveTo(self.midcoord)
        p.mouseDown(button="RIGHT")
        p.moveTo(self.midcoord[0] + 367,self.midcoord[1])
        p.mouseUp(button="LEFT")
        self.Photo("Vista Oclusao Posterior")
    def captLeft90(self):
        p.moveTo(self.midcoord[0],self.midcoord[1])
        p.mouseDown(button="RIGHT")
        p.moveTo(self.midcoord[0] - 189,self.midcoord[1])
        p.mouseUp(button="RIGHT")
        self.Photo("Vista Lateral Direita 90°")
    def captLeft45(self):
        p.moveTo(self.midcoord[0],self.midcoord[1])
        p.mouseDown(button="RIGHT")
        p.moveTo(self.midcoord[0] - 107,self.midcoord[1])
        p.mouseUp(button="RIGHT")
        self.Photo("Vista Lateral Direita 45°")
    def captRight90(self):
        p.moveTo(self.midcoord[0],self.midcoord[1])
        p.mouseDown(button="RIGHT")
        p.moveTo(self.midcoord[0] - 220,self.midcoord[1])
        p.mouseUp(button="RIGHT")
        self.Photo("Vista Lateral Esquerda 90°")
    def captRight45(self):
        p.moveTo(self.midcoord[0],self.midcoord[1])
        p.mouseDown(button="RIGHT")
        p.moveTo(self.midcoord[0] + 95,self.midcoord[1])
        p.mouseUp(button="RIGHT")
        self.Photo("Vista Lateral Esquerda 45°")
    def captOclSup(self,op):
        p.PAUSE= 0.2
        if(op == "sup"):
            self.Menu("Otop")
            self.Mand("off")
            p.alert(title="Atenção", text="Ajuste a posição superior")
            self.Enquadrar()
            t.sleep(4)
            self.Photo("Vista Oclusal Superior")
        elif(op == "sob"):
            self.Sobrepos("on")
            self.SobreposPhoto("sup") 
            self.Selfie("5")           
        else:
            self.Sobrepos("off")
            self.Transp("on")
            self.IPR("on")
            self.IPRPhoto("sup")
            self.Selfie("S")
            p.PAUSE= 1
            self.IPR("off")
    def Selfie(self, name):
        p.screenshot(region=self.screenCoord).save(os.environ["USERPROFILE"] + "\\Sunshine\\Images\\tmp\\" + name + ".png")
    def captOclInf(self,op):
        if(op == "inf"):
            t.sleep(2)
            self.Menu("Oinf")
            self.Max("off")
            self.Mand("on")
            p.alert(title="Atenção", text="Ajuste a posição inferior")
            self.Enquadrar()
            t.sleep(4)
            self.Photo("Vista Oclusal Inferior")
        elif(op == "sob"):
            self.Sobrepos("on")
            self.SobreposPhoto("inf")
            self.Selfie("6")
        else:
            self.Sobrepos("off")
            self.DownMenu()
            self.IPR("on")
            self.IPRPhoto("inf")
            self.Selfie("I")
            self.IPR("off")
        

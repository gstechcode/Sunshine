from tkinter import *
from tkinter import ttk, messagebox
import os, json
import win32api, win32gui
import pyautogui as p
import time as t

class Calibration(Tk):
    def __init__(self):
        super().__init__()
        self.title("Sunshine - Calibrador de Coordenadas")
        self.label1= Label(self, text="Selecione uma coordenada", font="Calibri 20", fg="white", bg="orange")
        self.label1.pack(pady="5px")
        self.iconbitmap(os.environ["USERPROFILE"] + "\\Sunshine\\Images\\Icon.ico")
        self.label1= Label(self, text="(Clique duas vezes)", font="Calibri 12", fg="white", bg="orange")
        self.label1.pack(pady="10px")
        style = ttk.Style()
        style.configure("mystyle.Treeview", bd=0, font=('Calibri', 11), justify="center")
        self.treeview= ttk.Treeview(self, columns= ["Coordenada","Valor"], show="headings", style="mystyle.Treeview")
        self.treeview.column("Coordenada",anchor= CENTER)
        self.treeview.heading("Coordenada",text= "Coordenada")
        self.treeview.column("Valor",anchor= CENTER)
        self.treeview.heading("Valor",text= "Valor")
        self.treeview.pack()
        self.treeview.bind("<Double-1>", self.updateCoord)
        self.readCoords()
        self.config(bg="orange", padx="30px", pady="30px")
        self.mainloop()
    def updateCoord(self, event):
        item= self.treeview.item(self.treeview.selection())["values"]
        messagebox.showinfo("Sunshine - Marcação de Coordenada Agendada", "Você terá 8 segundos para posicionar o ponteiro do mouse da coordenada desejada.")
        if(item[0] == "QUAD"):
            coords = self.refactorQuad()
            x= coords[0]
            y= coords[1]
        else:
            t.sleep(8)
            x,y= p.position().x, p.position().y
        messagebox.showinfo("Sucesso!","Coordenada capturada com sucesso!")
        option= messagebox.askyesno("Salvar mudanças?", "Você deseja adicionar essa nova coordenada?")
        if(option):
            print(item)
            self.coords[item[0]]= (x,y)
            self.saveChanges()
        else:
            pass
    def refactorQuad(self):
        k= Tk()
        width= k.winfo_screenwidth()
        height= k.winfo_screenheight()
        k.destroy()
        aux= 0
        dc = win32gui.GetDC(0)
        t.sleep(8)
        while True:
            initquad= [p.position().x,p.position().y]
            finalquad= [0,0]
            finalquad[0] = initquad[0] + int((width * 61.25)/100)
            finalquad[1] = initquad[1] + int((height * 80)/100)

            print(finalquad)

            win32gui.MoveToEx(dc,initquad[0],initquad[1])
            win32gui.LineTo(dc,finalquad[0],initquad[1])

            win32gui.MoveToEx(dc,initquad[0],initquad[1])
            win32gui.LineTo(dc,initquad[0],finalquad[1])

            win32gui.MoveToEx(dc,initquad[0],finalquad[1])
            win32gui.LineTo(dc,finalquad[0],finalquad[1])

            win32gui.MoveToEx(dc,finalquad[0],initquad[1])
            win32gui.LineTo(dc,finalquad[0],finalquad[1])

            self.update()
            
            aux += 100
            if(aux == 5000):
                x,y= p.position().x, p.position().y
                option = messagebox.askyesno("Sunshine - Quad", "Deseja usar este quadrado para as fotos?")
                if(not(option)):
                    aux= 0
                    t.sleep(8)
                else:
                    return [x,y]
    def saveChanges(self):
        arquivo= open(self.pcoords,"w")
        arquivo.write(json.dumps(self.coords))
        arquivo.close()
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        self.readCoords()
    def readCoords(self):
        self.pcoords= os.environ["USERPROFILE"] + "\\Sunshine\\coords.json"
        if(not(os.path.exists(self.pcoords))):
            arquivo= open(self.pcoords, "w")
            self.loadInitialJSON(arquivo)
            arquivo.close()
        arquivo= open(self.pcoords,"r")
        self.coords= json.loads(arquivo.readlines()[0])
        for i in self.coords:
            self.treeview.insert("",END,values= [i,self.coords[i]])
        arquivo.close()
    def loadInitialJSON(self, arquivo):
        coords= {}
        coords["SobreposicaoON"]= []
        coords["SobreposicaoOFF"]= []
        coords["TransparenciaON"]= []
        coords["TransparenciaOFF"]= []
        coords["IconeIPR"]= []
        coords["IconeDIST"]= []
        coords["IPRONOFF"]= []
        coords["DISTON"]= []
        coords["DISTOFF"]= []
        coords["FINALMENU"]= []
        coords["STARTMENU"] = []
        coords["ICONEFOTO"]= []
        coords["VOCLSUP"]= []
        coords["VOCLINF"]= []
        coords["VOCLRIGHT"]= []
        coords["VOCLLEFT"] = []
        coords["VOCLFRONT"] = []
        coords["VOCLBACK"] = []
        coords["MANDON"] = []
        coords["MANDOFF"] = []
        coords["MAXON"] = []
        coords["MAXOFF"] = []
        coords["QUAD"]= []
        coords["ARCSOPEN"]= []
        coords["BTNEST"]= []
        coords["BTNMOV"]= []
        coords["DOWNMENUEST"]= []
        coords["UPMENUEST"] = []
        coords["CLOSEEST"]= []
        coords["BLANK"] = []
        coords["STARTPOSITIONEST"]= []
        coords["ENDPOSITIONEST"]= []
        coords["STARTPOSITIONMOV"]= []
        coords["ENDPOSITIONMOV"]= []
        coords["IconeIPR2"] = []
        coords["IPRONOFF2"] = []
        arquivo.write(json.dumps(coords))
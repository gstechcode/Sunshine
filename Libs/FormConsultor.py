from PIL import Image, ImageFont, ImageDraw
import os, json, re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class FormConsultor:
    def __init__(self):
        self.width= 1000
        self.db= self.openDB()
        if(self.gerar()):
            self.loadConsultors()
            self.form()
        else:
            pass
    def gerar(self):
        sup= int(self.db["sup"])
        inf= int(self.db["inf"])
        if(self.db["supatt"] != ""):
            sup += 1
        if(self.db["infatt"] != ""):
            inf += 1

        if(self.db["diagnostico"]):
            return False
        if(sup > 12 and inf > 12):
            return True
        else:
            return False
    def form(self):
        self.display= tk.Tk()
        self.display.iconbitmap(os.environ["USERPROFILE"] + "\\Sunshine\\Images\\Icon.ico")
        menubar = tk.Menu(self.display, bg="orange")
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Configurar", command= self.configConsultors)
        menubar.add_cascade(label="Consultores", menu=filemenu)
        self.varCombo= tk.StringVar()
        self.varCombo.set("Selecione o consultor")
        self.display.title("Sunshine - Gerar Informativo")
        self.display.geometry("500x400")
        self.display.config(menu=menubar,bg="orange", padx="30px", pady="30px")
        self.label= tk.Label(self.display,text="Selecione o consultor", font="Arial 20 bold", fg="white", bg="orange")
        self.label.pack(pady="30px")
        self.combobox= ttk.Combobox(self.display,textvariable= self.varCombo, values= self.consultorsList, font="Arial 15", justify="center", state="readonly")
        self.combobox.pack()
        self.salvar= tk.Button(self.display, text="Pronto", bg="green", fg="white", relief="flat", font="arial 15", command= self.end)
        self.salvar.pack(pady="30px")
        self.display.mainloop()
    def end(self):
        self.db["Consultor"]= self.varCombo.get()
        self.db["ConsultorTel"]= self.getConsultor(self.varCombo.get())["Telefone"]
        self.rewriteDB(self.db)
        self.display.destroy()
    def getConsultor(self, txt):
        file= open(os.environ["USERPROFILE"] + "\\Sunshine\\consultors.json","r")
        selectedConsultor= json.loads(file.readlines()[0])
        file.close()
        return selectedConsultor[txt]
    
    def rewriteDB(self, txt):
        file= open(os.environ["USERPROFILE"] + "\\Sunshine\\Cache\\FormMain.cache","w")
        file.write(json.dumps(txt))
        file.close()

    def configConsultors(self):
        self.root= tk.Tk()
        self.root.iconbitmap(os.environ["USERPROFILE"] + "\\Sunshine\\Images\\Icon.ico")
        self.root.title("Configurações de Consultor")
        self.root.config(bg="orange", padx="30px", pady="30px")
        self.treeview= ttk.Treeview(self.root, columns= ["Nome","Telefone"], show="headings")
        self.treeview.heading("Nome", text="Nome")
        self.treeview.heading("Telefone", text="Telefone")
        self.listarConsultors()
        self.frame= tk.Frame(self.root, bg="orange")
        self.frame.pack(pady="5px")
        self.nome= tk.Entry(self.frame, justify= "center", font="Arial 12")
        self.nome.insert(0,"Nome do consultor")
        self.nome.pack(pady="10px")
        self.nome.bind("<FocusIn>", self.clearNome)
        self.telefone= tk.Entry(self.frame, justify= "center", font="Arial 12")
        self.telefone.insert(0,"Telefone do Consultor")
        self.telefone.pack(pady="5px")
        self.btn= tk.Button(self.root, text="Salvar", bg="green", fg="white", relief="flat", font="Arial 15", command= self.TreeSave)
        self.btn.pack(pady="5px")
        self.telefone.bind("<FocusIn>", self.clearTelefone)
        self.treeview.pack()
        self.treeview.bind('<<TreeviewSelect>>', self.consultorSelected)
        self.root.mainloop()
    def TreeSave(self):
        if(self.nome.get() in self.consultors):
            self.consultors[self.nome.get()]["Telefone"]= self.telefone.get()
            messagebox.showinfo("Consultor Atualizado!","Consultor foi atualizado com sucesso!")
        else:
            self.consultors[self.nome.get()] = {"Telefone": self.telefone.get()}
            messagebox.showinfo("Consultor Cadastrado!","Consultor foi cadastrado com sucesso!")
        arquivo= open(os.environ["USERPROFILE"] + "\\Sunshine\\consultors.json", "w")
        arquivo.write(json.dumps(self.consultors))
        arquivo.close()
        self.root.destroy()
        self.display.update()
        self.loadConsultors()
        self.combobox["values"]= self.consultorsList
        self.combobox.update()
    def clearNome(self, event):
        self.nome.delete(0,tk.END)
    def clearTelefone(self, event):
        self.telefone.delete(0,tk.END)
    def consultorSelected(self, event):
        tag= self.treeview.selection()
        item= self.treeview.item(tag)["values"]
        self.nome.delete(0,tk.END)
        self.nome.insert(0,item[0])
        self.telefone.delete(0,tk.END)
        self.telefone.insert(0,item[1])
    def listarConsultors(self):
        for i in self.consultors:
            self.treeview.insert("",tk.END,values= [i,self.consultors[i]["Telefone"]])
        self.root.update()    
    def loadConsultors(self):
        if(not(os.path.exists(os.environ["USERPROFILE"] + "\\Sunshine\\consultors.json"))):
            arquivo= open(os.environ["USERPROFILE"] + "\\Sunshine\\consultors.json", "w")
            arquivo.write("{}")
            arquivo.close()
        arquivo= open(os.environ["USERPROFILE"] + "\\Sunshine\\consultors.json", "r")
        try:
            consultors= arquivo.readlines()[0]
        except IndexError:
            arquivo= open(os.environ["USERPROFILE"] + "\\Sunshine\\consultors.json", "w")
            arquivo.write("{}")
            arquivo.close()
            consultors= arquivo.readlines()[0]
        arquivo.close()
        self.consultors= json.loads(consultors)
        self.consultorsList= []
        for i in self.consultors:
            self.consultorsList.append(i)

    def loadFont(self, font, size):
        font= ImageFont.truetype(os.environ["USERPROFILE"] + f"\\Sunshine\\Fonts\\{font}.ttf",size)
        return font

    def header(self):
        self.cRect((0,0,1000,300), (235,87,31))
        self.loadIMG(os.environ["USERPROFILE"] + "\\Sunshine\\Images\\Compass3D.png",-1.7,["c", 20])
        self.text("Aviso importante", 50, color=(255,255,255), font="Arial",whc= [0,220])
        self.loadConsultors()
        consultor= self.varCombo.get()
        telefone= self.consultors[consultor]["Telefone"]
        script= f"""< Prezado Dr.  {self.db["dentista"]} > \n\n \n\n Este é um caso de grandes movimentações ortodônticas a serem realizadas, movimentações essas que geram uma distorção no modelo na região cervical. Isso se explica porque a gengiva não acompanha as movimentações realizadas no dente virtualmente. \n\n \n\n Por conta disso, caso deseje solicitar a continuação do caso após o uso dos primeiros 12 pares de placas, pode ser que seja necessário a realização de um recorte cervical nas próximas placas ou até mesmo o envio de um novo escaneamento. Essa medida é benéfica para boa evolução do caso, pois quando o novo escaneamento é enviado, temos o correto posicionamento do periodonto com o dente, melhorando assim a previsibilidade. O recorte cervical também pode ser indicado pois ele remove a área de retentividade criada, melhora a adaptação e conforto ao paciente. Em algumas situações essa medida pode ser obrigatória e não somente benéfica. \n\n \n\n Gostaríamos de lembrá-lo que os escaneamentos de modelo em gesso são gratuitos e podem ser enviados a Compass 3D, porém as moldagens devem ser realizadas sem attachments. E caso opte pelo recorte cervical, a taxa cobrada pelo serviço deverá ser consultada com o consultor comercial da sua região < ({consultor} - {telefone}) >. \n\n \n\n < Qualquer dúvida, continuamos sempre à disposição! > \n\n \n\n < Atenciosamente, > \n\n < {self.db["ortodontista"]} > \n"""
        self.Paragraph(script, "Arial", 22)
    def Paragraph(self,txt, font, size, margins= 40):
        bold= 0
        finalText= ""
        _, _, w, h = self.cursor.textbbox((0, 0), "A", font=self.loadFont(font,size))
        heightText= h
        widthText= w
        currentHeight= 340
        currentWidth= margins
        contador= 0
        varText= ""
        textList= re.split(" ",txt)
        for i in textList:
            varText += i + " "
            _, _, w, h = self.cursor.textbbox((0, 0), varText, font=self.loadFont(font,size))
            breaked= w > self.width - (2*margins) - (widthText*8)
            #VERIFICAÇÃO DE BOLD
            if("<" in i):
                bold= 1
                finalText= finalText.replace("<","")
                font += "-Bold"
                currentWidth -= widthText
            elif(">" in i):
                font= font.replace("-Bold","")
            
            if("Este" in i or "Por" in i or "Gosta" in i):
                currentWidth -= 5

            if(i == "\n\n" or breaked):
                currentWidth= margins
                currentHeight += heightText + 10
                varText= ""
            _, _, w, h = self.cursor.textbbox((0, 0), i + " ", font=self.loadFont(font,size))
            self.text(i.replace("<","").replace(">","") + " ",size, color=(0,0,0), font= font, whc=[currentWidth,currentHeight])
            currentWidth += w
    def text(self, text, size, color, font="Arial",whc= None):
        _, _, w, h = self.cursor.textbbox((0, 0), text, font=self.loadFont(font,size))        
        widthtext= int((self.width-w)/2)
        heighttext= int((self.height-h)/2)
        if(whc != None):
            if(whc[0] != 0):
                widthtext= whc[0]
            if(whc[1] != 0):
                heighttext= whc[1]
        self.cursor.text((widthtext, heighttext), text, font=self.loadFont(font,size), fill= color)
    def cRect(self,coords,bg):
        self.cursor.rectangle(coords,fill=bg)
    def openDB(self):
        file= open(os.environ["USERPROFILE"] + "\\Sunshine\\Cache\\FormMain.cache","r")
        arq= file.readlines()[0]
        file.close()
        return json.loads(arq)
    def loadIMG(self,fp,scale,center):
        img= Image.open(fp)
        if(scale >= 1):
            img= img.resize((img.size[0]*scale,img.size[1]*scale))
        else:
            scale *= -1
            img= img.resize((int(img.size[0]/scale),int(img.size[1]/scale)))
            if("c" in center):
                self.img.paste(img,(int((self.width - img.size[0])/2),center[1]),mask=img)
            else:
                 self.img.paste(img,center[0],center[1],mask=img)
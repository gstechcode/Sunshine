#GERA RELATORIO 14 E REGISTRA ATT

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.utils import ImageReader
from reportlab.rl_config import defaultPageSize
import os
import json

class Report14(object):
    def __init__(self, db):
        self.masterpath= os.environ["USERPROFILE"] + "\\Sunshine"
        self.width= 596
        self.database= db
        self.translateVars()
        self.fim= 0
        self.util= [0,0]
        self.tablesp= 0
        self.enter= 0
        self.aux= 0
        self.qp= 0
        self.aux2= ""
        self.pagebreak= 0
        self.height= 842
        self.pdf= canvas.Canvas(self.path + f"/14 - Relatorio de Instrucoes {self.tsetup} - {self.paciente}.pdf", verbosity= 1, bottomup= 0)
        self.pdf.setPageSize((596,842))
        self.pdf.setTitle("Relatorio de Instrucoes {self.tsetup} - {self.paciente}")
        self.Header()
        self.body()
        self.pdf.save()
    def translateVars(self):
        self.tsetup= self.database["setup"]
        self.paciente= self.database["paciente"]
        self.dentista= self.database["dentista"]
        self.sup= self.database["sup"]
        self.inf= self.database["inf"]
        self.vest= self.database["vestibular"]
        self.lin= self.database["lingual"]
        self.ocl= self.database["oclusal"]
        self.pacote= self.database["pacote"]
        self.ortodont= self.database["ortodontista"]
        self.validade= self.database["prazo"]
        self.path= self.database["path"]
        self.comment= self.database["comentario"]
    def Center(self, ref):
        return (self.width - ref)/2
    def Header(self):
        self.pdf.setFillColorRGB(31/255,91/255,141/255)
        self.pdf.setStrokeColorRGB(31/255,91/255,141/255)
        self.pdf.rect(0,0,827,160, fill=1)
        img= ImageReader(self.masterpath + "\\Images\\OrthoAligner.png")
        self.pdf.scale(1,-1)
        imgw= 250
        self.pdf.drawImage(img,self.Center(imgw),-150, width= imgw, height= 200, mask='auto', preserveAspectRatio= True, anchor="c")
        self.pdf.scale(1,-1)
        self.pdf.setFillColorRGB(1,1,1)
        self.pdf.setFont("Helvetica",26)
        self.pdf.setStrokeColorRGB(0,0,0)
        self.pdf.drawCentredString(self.width/2,130,"Relat??rio de Setup Virtual")
    def write(self,texto):
        if(self.enter == 1 and self.tablesp == 0):
            fcpy= self.bl2._fontname
            self.bl2= self.pdf.beginText()
            self.bl2.setTextOrigin(40,50)
            self.bl2.setFont(fcpy,13)
            self.enter= 0
        elif(self.tablesp == 1):
            fcpy= self.bl2._fontname
            self.bl2= self.pdf.beginText()
            self.bl2.setTextOrigin(self.util[0],self.util[1])
            self.bl2.setFont(fcpy,13)
            self.enter= 0
        for line in texto:
            (x,y) = self.bl2.getCursor()
            if(self.pagebreak == 1):
                self.aux2 += line
            elif(line == "|"):
                self.bl2.setTextOrigin(40,y)
                self.bl2.textLine()
            elif(x >= 512 and line == " "):
                self.bl2.setTextOrigin(40,y)
                self.bl2.textLine(line)  
            else:
                if(line == "<"):
                    self.bl2.setFont("Helvetica-Bold",13)
                elif(line == "??"):
                    pass
                elif(line == ">"):
                    self.bl2.setFont("Helvetica",13)
                elif(line == "??"):
                    self.bl2.textLine()
                    (x,y) = self.bl2.getCursor()
                    if(y + 200 >= 714):
                        self.aux2= ""
                        self.enter= 1
                        self.pdf.drawText(self.bl2)
                        self.pdf.showPage()
                        x= 40
                        y= 50
                        self.pagebreak= 1
                    self.pdf.setFillColorRGB(219/255,229/255,241/255)
                    self.pdf.setStrokeColorRGB(75/255,172/255,198/255)
                    self.pdf.rect(x,y,width=512,height= 200, fill=1)
                    self.pdf.setFillColorRGB(1/255,64/255,191/255)
                    self.pdf.setFont("Helvetica-Bold",18)
                    self.pdf.drawCentredString(552/2,y+30,"   Casos OrthoAligner ONE e PRO")
                    self.pdf.line(x,y+45,x+512,y+45)
                    self.pdf.setFont("Helvetica",13)
                    txt= "Se o seu tratamento se encaixou em um pacote ONE e PRO, voc?? receber?? | somente at?? a etapa 10, para acompanharmos com voc?? a evolu????o do caso.||"
                    txt += "Por isso, quando estiver finalizando essa fase e o tratamento estiver avan??ando |conforme o planejado, voc?? deve solicitar o restante dos alinhadores atrav??s do |e-mail:|| &contato@compass3d.com.br# "
                    bl3= self.pdf.beginText()
                    xcp= x+20
                    ycp= y+70
                    bl3.setTextOrigin(xcp,ycp)
                    bl3.setFillColorRGB(0,0,0)
                    for i in range(0,16):
                        self.bl2.textLine()
                    for pp in txt:
                        (k,l) = bl3.getCursor()
                        if(pp == "|"):
                            bl3.setTextOrigin(xcp,l)
                            bl3.textLine()
                        elif(x >= 512 and line == " "):
                            bl3.setTextOrigin(xcp,l)
                            bl3.textLine(line)
                        elif(pp == "&"):
                            bl3.setTextOrigin(((512-xcp)/2)-20,l)
                            bl3.setFont("Helvetica",14)
                            self.coords[0]= k
                            self.coords[1]= l
                            bl3.setFillColorRGB(0,0,0.4)
                        elif(pp == "#"):
                            self.coords[2]= k
                            self.coords[3]= l
                            bl3.setFillColorRGB(0,0,0)
                            bl3.setFont("Helvetica",13)
                        else:
                            bl3.textOut(pp)
                    (k,l) = bl3.getCursor()
                    self.pdf.drawText(bl3)
                    self.pdf.linkURL("mailto:contato@compass3d.com.br",self.coords, relative=1)
                    self.pdf.setFont("Helvetica",13)
                    self.pdf.setStrokeColorRGB(1,1,1)
                    if(self.pagebreak == 1):
                        self.tablesp= 1
                        self.util[0]= 40
                        self.util[1] = l+60
                elif(line == "&"):
                    self.coords[0]= x
                    self.coords[1]= y
                    self.bl2.setFillColorRGB(0,0,0.4)
                elif(line == "#"):
                    self.coords[2]= x
                    self.coords[3]= y
                    self.bl2.setFillColorRGB(0,0,0)
                else:
                    if(y >= 714):
                        self.enter= 1
                        self.aux2= ""
                        self.pdf.drawText(self.bl2)
                        self.pdf.showPage()
                        self.pagebreak= 1
                        self.aux2 += line
                    self.bl2.textOut(line)
        if(self.pagebreak == 1):
            self.pagebreak= 0
            self.write(self.aux2)
            if(line == "??"):
                return 0;
            self.pdf.drawText(self.bl2)
        if(self.enter == 0):
            self.pdf.drawText(self.bl2)
    def rodape(self):
        self.pdf.setFillColorRGB(31/255,91/255,141/255)
        self.pdf.setStrokeColorRGB(31/255,91/255,141/255)
        self.pdf.rect(0,714,width= self.width, height= 300, fill=1)
        self.pdf.setFillColorRGB(1,1,1)
        self.pdf.setFont("Helvetica",11)
        self.pdf.drawString(30,759,"0800 601 7277")
        self.pdf.drawString(30,779,"@compasscomvoce                       /compasscomvoce")
        self.pdf.drawString(30,799,"contato@compass3d.com.br         www.compass3d.com.br")
        self.pdf.drawString(30,819,"Av. Caranda??, 161 - 2?? andar, Funcion??rios / BH-MG")
        img= ImageReader(self.masterpath + "\\Images\\Compass3D.png")
        self.pdf.scale(1,-1)
        self.pdf.drawImage(img,(self.width/5)*3 + 40,-1270, width= 168, height= 525, mask='auto', preserveAspectRatio= True, anchor="l")
    def body(self):
        if("ltda" in self.dentista):
            clin= ""
        else:
            clin= "Dr(a) "
        self.pdf.setFont("Helvetica",13)
        self.pdf.setFillColorRGB(0,0,0)
        self.pdf.drawString(40,200, "Prezado")
        self.pdf.setFont("Helvetica-Bold",13)
        self.pdf.drawString(96,200, clin + self.dentista)
        self.pdf.setFont("Helvetica",13)
        x= 40
        y= 220
        texto0= self.comment
        x= 40
        self.bl2= self.pdf.beginText()
        if(texto0 == ""):
            texto0= texto0.replace("\n","")
            texto= texto0
        else:
            texto = "{comment}|"
        texto= texto + "O Setup Virtual para <{Paciente}> foi realizado conforme suas instru????es.||Modelos virtuais anexados mostram o resultado do setup virtual e poder??o ser visualizados no software gratuito 3Shape Viewer.||"
        texto= texto + "<Poder?? ser necess??rio refinamento ap??s o t??rmino da movimenta????o ortod??ntica em virtude da caracter??stica de alguns movimentos dent??rios solicitados, da complexidade do caso, da resposta biol??gica de cada paciente, do uso correto e cont??nuo do aparelho, da condu????o do tratamento, entre outros.>||"
        texto= texto + "O refinamento dever?? ser solicitado atrav??s do e-mail &contato@compass3d.com.br# e novos modelos (ambas as arcadas) dever??o ser enviados. Se optar por realizar nova moldagem, haver?? necessidade de retirada dos attachments presentes para n??o ocorrer distor????es nos modelos em gesso. Caso a op????o seja o escaneamento intraoral, n??o h?? necessidade da retirada dos attachments.||"
        texto= texto + "Para realizar a etapa inicial do presente planejamento, ser??o necess??rios:||Alinhadores Superiores: <{sup}>|Alinhadores Inferiores: <{inf}>||"
        texto= texto + "Est?? indicado uso de attachments para maior controle do movimento dent??rio, para os elementos identificados abaixo:||"
        texto= texto + "Face Vestibular: <{v}>|Face Lingual: <{l}>|Face Oclusal: <{o}>||"
        texto= texto + "Os attachments dever??o ser instalados com o guia correspondente para cada arcada, confeccionado em placa de acetato 0,3mm enviada para este fim, antes de iniciar o uso do primeiro alinhador OrthoAligner.||"
        texto= texto + "Isto implica em mais <{att}> modelos prototipados (identificados como ???0???) e os respectivos guias para instala????o dos attachments.||Total de alinhadores: <{quant}({extenso})>.||"
        if("Refino" in self.pacote):
            if(self.pacote == "Refino I"):
                pass
            else:
                texto = texto + "<Tratado anteriormente com OrthoAligner Refino "
                if(self.pacote == "Refino II"):
                    texto= texto + "I."
                elif(self.pacote == "Refino III"):
                    texto= texto + "I, II."
                elif(self.pacote == "Refino IV"):
                    texto= texto + "I, II, III."
                elif(self.pacote == "Refino V"):
                    texto= texto + "I, II, III, IV."
                elif(self.pacote == "Refino VI"):
                    texto= texto + "I, II, III, IV, V."
                texto= texto + ">|"

        if("Fase" in self.pacote):
            if(self.pacote == "Fase I"):
                pass
            else:
                texto = texto + "<Tratado anteriormente com OrthoAligner Fase "
                if(self.pacote == "Fase II"):
                    texto= texto + "I."
                elif(self.pacote == "Fase III"):
                    texto= texto + "I, II."
                elif(self.pacote == "Fase IV"):
                    texto= texto + "I, II, III."
                elif(self.pacote == "Fase V"):
                    texto= texto + "I, II, III, IV."
                elif(self.pacote == "Fase VI"):
                    texto= texto + "I, II, III, IV, V."
                texto= texto + ">|"
                
        texto= texto + "O caso ser?? tratado com um <OrthoAligner {pacote}>.|"
        if(self.validade != ""):
            self.validade= self.validade.replace("\n","")
            texto= texto + "<" + self.validade + ">|"
        texto= texto + "|A placa utilizada para o tratamento ser?? <AL+> de 0,6mm que re??ne performance e resist??ncia para os melhores resultados.||"
        texto= texto + "Al??m disso, voc?? tamb??m pode optar pelo <recorte padr??o> (corte reto, 2mm acima da margem gengival) ou <recorte cervical> com contorno gengival.||"
        texto= texto + "Lembrando que a escolha das placas e do recorte deve ser baseada na experi??ncia do profissional e em especial no caso a ser tratado.||"
        texto= texto + "<Verifique com o seu consultor com rela????o aos custos do pacote indicado, placas e recorte escolhido.>||??"
        texto= texto + "Est?? indicado a realiza????o de ajuste oclusal durante e ap??s a movimenta????o dent??ria sugerida neste setup.||A situa????o periodontal do paciente deve ser mantida sob controle, como em todo tratamento ortod??ntico.||"
        texto= texto + "Em geral, os alinhadores ortod??nticos devem ser utilizados em tempo integral, dia e noite e devem ser retirados para a mastiga????o e higiene bucal.||"
        texto= texto + "A substitui????o dos alinhadores Ortho Aligner deve ocorrer a intervalos de quinze a vinte dias, observadas as caracter??sticas de cada paciente, tais como idade, sa??de geral, bucal e periodontal, ou ainda a crit??rio do profissional respons??vel pelo tratamento.||"
        texto= texto + "Em casos com indica????o de desgastes interproximais (Stripping/IPR), a quantidade e locais a serem feitos esses desgastes est??o assinalados no arquivo PDF anexo. Os desgastes interproximais dever??o ser iniciados j?? na instala????o dos primeiros alinhadores e prosseguir a taxa de 0,1mm por etapa subsequente.||"
        texto= texto + "A conten????o p??s tratamento dever?? ser instalada ap??s o uso do ??ltimo alinhador.||"
        texto= texto + "<Informamos que caso seja solicitada a altera????o do setup, iremos acrescentar mais (2) dois dias ??teis no prazo de entrega do planejamento para o envio do mesmo.>||"
        texto= texto + "<{ortodont}>|Compass3D??"
        if(self.sup == ""):
            self.sup = "0"
        if(self.inf == ""):
            self.inf= "0"
        aux= ""
        for i in self.vest:
            if(i == ","):
                aux += i + " "
            else:
                aux += i
        self.vest = aux
        aux= ""
        for i in self.lin:
            if(i == ","):
                aux += i + " "
            else:
                aux += i
        self.lin= aux
        aux= ""
        for i in self.ocl:
            if(i == ","):
                aux += i + " "
            else:
                aux += i
        self.ocl= aux
        self.att= 0
        arcsup= ["11","12","13","14","15","16","17","21","22","23","24","25","26","27"]
        arcinf= ["31","32","33","34","35","36","37","41","42","43","44","45","46","47"]
        self.supatt= 0
        self.infatt= 0
        for k in arcsup:
            if(k in self.vest or k in self.lin or k in self.ocl):
                self.supatt= 1
        for i in arcinf:
            if(i in self.vest or i in self.lin or i in self.ocl and self.att == 1):
                self.infatt= 1
                
        if(self.sup == "0"):
            self.supatt = 0
        elif(self.inf == "0"):
            self.infatt= 0

        self.att= self.supatt + self.infatt
        with open(os.environ["USERPROFILE"] + "\\Sunshine\\Cache\\FormMain.cache","r") as file:
            db= json.loads(file.read())
            if(self.supatt == 1):
                db["supatt"]= " + Attach"
            else:
                db["supatt"]= ""
            if(self.infatt == 1):
                db["infatt"]= " + Attach"
            else:
                db["infatt"]= ""
        with open(os.environ["USERPROFILE"] + "\\Sunshine\\Cache\\FormMain.cache","w") as file:
            file.write(json.dumps(db))
        texto= texto.format(comment= texto0,Paciente= self.paciente,sup=self.extenso(self.sup),inf=self.extenso(self.inf),v=self.vest,l=self.lin,o=self.ocl,att=self.extenso(str(self.att)),quant=int(self.sup) + int(self.inf) + self.att,extenso=self.extenso(int(self.sup) + int(self.inf) + self.att),pacote=self.pacote,ortodont=self.ortodont)
        self.bl2.setTextOrigin(int(x),int(y))
        self.coords = [0,0,0,0]
        self.write(texto)
        self.rodape()
        self.pdf.setAuthor("Compass3D")
        self.pdf.setTitle("Relat??rio de Instru????es")
        self.pdf.linkURL('mailto:contato@compass3d.com.br', self.coords, relative=1)
    def extenso(self,num):
                listadef= {}
                n= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90,100]
                nums= ["um","dois","Tr??s","Quatro","Cinco","Seis","Sete","Oito","Nove","Dez","Onze",
                       "Doze","Treze","Quatorze","Quinze","Dezesseis","Dezessete","Dezoito","Dezenove",
                       "Vinte","Trinta","Quarenta","Cinquenta","Sessenta","Setenta","Oitenta","Noventa",
                       "Cem"]
                if(int(num) == 0):
                    if(num == self.sup or num == self.inf):
                        return "-"
                    else:
                        return "zero"
                for pp in range(0,len(n)):
                        listadef[n[pp]]= nums[pp]
                if(int(num) in n):
                        return listadef[int(num)]
                kk= ""
                x=0
                numstr= str(num)
                total = int(self.sup) + int(self.inf)
                if(int(num) > 100):
                        kk += "Cento e "
                        numstr= numstr[1] + numstr[2]
                if(int(num) > 10 and int(num) < 100 or total > 100):
                        numstr= int(numstr)
                        if(numstr in n):
                            kk = kk + listadef[int(numstr)]
                        else:
                            numstr= str(numstr)
                            dez= int(numstr[0] + "0")
                            un= int(numstr[1])
                            kk= kk + listadef[dez] + " e " + listadef[un]
                #kk = kk + listadef[int(str(str(num[x]) + "0"))] + " e " + listadef[int(str(num[x+1]))]
                return kk

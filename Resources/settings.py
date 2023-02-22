import pyautogui as p
import time as t
import json, os

class settings:
    def __init__(self):
        try:
            self.ortho= p.getWindowsWithTitle("OrthoAnalyzer")
            self.ortho[0].activate()
            self.ortho[0].maximize()
            self.chrome= p.getWindowsWithTitle("Google Chrome")
        except Exception:
            pass
    def loadCoordsEst(self):
        arquivo= open(os.environ["USERPROFILE"] + "\\Sunshine\\coords.json","r")
        self.stCoords= json.loads(arquivo.readlines()[0])
        arquivo.close()
    def setupActive(self):
        p.click(26,237)
    def estCapt(self, op, arcs):
        self.loadCoordsEst()
        p.click(self.stCoords["BLANK"])
        t.sleep(2)
        path= self.path + "\\"
        p.click(self.stCoords["STARTMENU"])
        t.sleep(3)
        p.click(self.stCoords["BTNEST"])
        t.sleep(1)
        if(op == "SIM"):
            p.click(self.stCoords["UPMENUEST"])
            t.sleep(1)
            if(arcs == "Superior" or arcs == "Ambas"):
                p.click(self.stCoords["UPMENUEST"])
                p.click(self.stCoords["BLANK"])
                t.sleep(2)
                p.screenshot(region=(self.stCoords["STARTPOSITIONEST"][0],self.stCoords["STARTPOSITIONEST"][1],self.stCoords["ENDPOSITIONEST"][0] - self.stCoords["STARTPOSITIONEST"][0],self.stCoords["ENDPOSITIONEST"][1] - self.stCoords["STARTPOSITIONEST"][1])).save(path + "09 - Estagiamento " + str(self.master["sup"]) + " Superior - " + self.master["setup"] + ".png")
            if(arcs == "Inferior" or arcs == "Ambas"):
                p.click(self.stCoords["DOWNMENUEST"])
                p.click(self.stCoords["BLANK"])
                t.sleep(2)
                p.screenshot(region=(self.stCoords["STARTPOSITIONEST"][0],self.stCoords["STARTPOSITIONEST"][1],self.stCoords["ENDPOSITIONEST"][0] - self.stCoords["STARTPOSITIONEST"][0],self.stCoords["ENDPOSITIONEST"][1] - self.stCoords["STARTPOSITIONEST"][1])).save(path + "10 - Estagiamento " + str(self.master["inf"]) + " Inferior - " + self.master["setup"] + ".png")
        p.click(self.stCoords["CLOSEEST"])
        p.click(self.stCoords["BTNMOV"])
        t.sleep(4)
        p.screenshot(region=(self.stCoords["STARTPOSITIONMOV"][0],self.stCoords["STARTPOSITIONMOV"][1],self.stCoords["ENDPOSITIONMOV"][0] - self.stCoords["STARTPOSITIONMOV"][0],self.stCoords["ENDPOSITIONMOV"][1] - self.stCoords["STARTPOSITIONMOV"][1])).save(path + "11 - Tabela de Movimentacao - " + self.master["setup"] + ".png")
        p.alert(title="Sucesso!", text="Capturas realizadas com sucesso!")
    def modelAc(self):
        p.press("pagedown")
        p.press("enter", presses=3)
    def btnBack(self):
        p.click(67,55)
    def modelDefault(self):
        p.click(70,264, clicks=3)
    def report(self):
        t.sleep(3)
        self.ortho[0].activate()
        self.PAUSE= 2
        self.btnBack()
        p.click(185,304)
        p.click(102,274)
        p.click(900,275)
        t.sleep(5)
        p.press("tab")
        p.press("enter")                 
        self.chrome[0].activate()
        self.chrome[0].maximize()
        t.sleep(10)
        p.hotkey("ctrl","p")
        t.sleep(2)
        p.press("enter")
        t.sleep(6)
        p.write(self.path)
        p.press("enter")
        p.write("13")
        p.press("tab", presses=3)
        p.press("enter")
        p.PAUSE= 1
        self.ortho[0].activate()
        self.ortho[0].maximize()
        t.sleep(5)
        self.btnBack()
        self.btnMV()
        self.modelDefault()
        p.PAUSE= 2
        self.modelAc()
        self.setupActive()
        p.PAUSE= 1
    def btnMV(self):
        p.click(33,414)
        

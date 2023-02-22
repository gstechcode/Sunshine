import json, os, time, sys
import psutil
import pyautogui
from tkinter import *
from tkinter import ttk, messagebox
from threading import Thread
from Views import FormMain
from Libs import Capture
from Libs import Report14
from Libs import Report12
from Libs import IPR
from Libs import ConvGIF
from Libs.Report19 import Report19		
from Libs import ConvertSTLs

class Sunshine:
	def __init__(self):
		formulario= FormMain.Execute()
		banco= self.getBanco()
		if(banco["relatorios1214"]):
			report14= Report14.Report14(banco)
			report12= Report12.Report12(banco)
		report19= Report19()
		if(banco["capturas"]):
			try:
				capturas= Capture.CaptureView(banco)
			except pyautogui.PyAutoGUIException:
				messagebox.showerror("Sunshine - Erro de Coordenadas","Você possui coordenadas não cadastradas! Certifique-se de cadastra-las primeiro antes de executar a etapa de captura!")
		if(banco["relatorioipr"]): 
			ipr= IPR.Report(banco)
		if(banco["otimizargifs"]):
			gifot= ConvGIF.ConvGIF(banco)
		if(banco["otimizarstls"]):
			stGabriellot= ConvertSTLs.ConvertSTLs(banco)
	def getBanco(self):
		db= open(os.environ["USERPROFILE"] + "\\Sunshine\\Cache\\FormMain.cache","r")
		return json.loads(db.readlines()[0])
x= Sunshine()
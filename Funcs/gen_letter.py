# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 20:48:25 2023

@author: Matt0
"""

from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Mm
from tkinter import filedialog

def gen_letter(paydata):
    tpl = DocxTemplate("Funcs/Letter template.docx") # In same directory
    
    filepath=filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("doc files",["*.doc","*.docx"]), ("All files", "*.*")])
    
    timeworked=paydata['date'][len(paydata['date'])-1].year-paydata['date'][0].year
    pctchange=paydata['deltapctstart'][len(paydata['date'])-1]
    currpay=paydata['pay'][len(paydata['date'])-1]
    adjusted=paydata['adjusted'][len(paydata['date'])-1]
    
    graph = InlineImage(tpl, image_descriptor=r"C:\Users\Matt0\Downloads\sad cat.jpg", width=Mm(45), height=Mm(70))
    
    
    context={'timeworked': timeworked, 
             'pctchange': pctchange,
             'graph': graph,
             'currpay':currpay,
             'adjusted': adjusted}
    
    tpl.render(context)
    
    tpl.save(filepath)
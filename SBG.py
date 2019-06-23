# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 11:53:53 2018

@author: ls
"""
# MuSBG: Mumax3 scripts batch generator

# Description: This is a scripts batch generating program
#              for Micromagnetic simulation package Mumax3.

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from SubWin import mesh,region,para,excitation,misc,output
from Loop import main

# =============================================================================
#                             Main Frame
# =============================================================================
win = tk.Tk()
win.title('SBG')
win.geometry('900x650')
win.resizable(False,False)

s = ttk.Style()
s.configure('.', font=('Aria', 14))

# main var
name_e_var = tk.StringVar()
Dir_e_var = tk.StringVar()

# name & dir frame
first_f = ttk.LabelFrame(win,text='   File Name & Dir   ')
first_f.grid(column=0,row=0,rowspan=2,padx=20,pady=20)

name_l = ttk.Label(first_f,text='Name:')
name_l.grid(column=0,row=0)

Dir_l = ttk.Label(first_f,text='Dir:')
Dir_l.grid(column=0,row=1)

name_e = ttk.Entry(first_f,textvariable=name_e_var)
name_e.grid(column=1,row=0)

Dir_e = ttk.Entry(first_f,textvariable=Dir_e_var)
Dir_e.grid(column=1,row=1)

for child in first_f.winfo_children():
    child.grid_configure(padx=8,pady=4)

# class frame
b_width =16
class_f = ttk.LabelFrame(win,text='   Add Elements  ')
class_f.grid(column=0,row=2,rowspan=6,padx=20,pady=20)

mesh_b = tk.Button(class_f,text='Mesh & Geometry',
                   command=lambda:mesh(text_monitor),
                   font=('Aria', 14),width=b_width,height=2)
mesh_b.grid(column=0,row=0)

region_b = tk.Button(class_f,text='Define Regions',
                     command=lambda:region(text_monitor),
                     font=('Aria', 14),width=b_width,height=2)
region_b.grid(column=0,row=1)

para_b = tk.Button(class_f,text='Parameters &\n Initial m',
                   command=lambda:para(text_monitor),
                   font=('Aria',14),
                   width=b_width,height=2)
para_b.grid(column=0,row=2)

exc_b = tk.Button(class_f,text='Excitations',font=('Aria', 14),
                  command=lambda:excitation(text_monitor),
                  width=b_width,height=2)
exc_b.grid(column=0,row=3)

misc_b = tk.Button(class_f,text='Miscellaneous',font=('Aria', 14),
                   command=lambda:misc(text_monitor),
                   width=b_width,height=2)
misc_b.grid(column=0,row=4)

output_b = tk.Button(class_f,text='Running & Output',
                     command=lambda:output(text_monitor),
                     font=('Aria', 14),width=b_width,height=2)
output_b.grid(column=0,row=5)

for child in class_f.winfo_children():
    child.grid_configure(padx=8,pady=8)

# text monitor
text_monitor = scrolledtext.ScrolledText(win,font=('Arial',13),
                                         height=28,width=63,
                                         wrap=tk.WORD)
text_monitor.grid(column=1,row=0,rowspan=8,
                  columnspan=3,padx=30,pady=15)

# OK button
ok = tk.Button(win,text='OK',
               command=lambda:main(name_e_var,
                                   Dir_e_var,
                                   text_monitor),
               font=('Arial', 14),width=8,height=1)
ok.grid(column=3,row=8)

win.mainloop()
import time

from PIL import ImageTk

from Logica import Kenteken_Uitlezen
from Services import Rest_Service
from Logica import Kenteken_Controleren
import tkinter as tk
from tkinter import filedialog, Text
import os
from PIL import ImageTk, Image

root = tk.Tk()

def auto1():
    tekst = Kenteken_Controleren.checkReservering('Logica/test1.jpg')
    label = tk.Label(root, text=tekst,bg="#4169E1",font=(None, 44), fg="black",pady=100,wraplengt=600)
    label.grid(row=0, column=0,columnspan=3)
    label.after(5000,label.destroy)
def auto2():
    tekst = Kenteken_Controleren.checkReservering('Logica/test2.jpg')
    label = tk.Label(root, text=tekst,bg="#4169E1",font=(None, 44), fg="black",pady=100,wraplengt=600)
    label.grid(row=0, column=0,columnspan=3)
    label.after(5000, label.destroy)
def auto3():
    tekst = Kenteken_Controleren.checkReservering('Logica/test3.jpg')
    label = tk.Label(root, text=tekst,bg="#4169E1",font=(None, 44), fg="black",pady=100,wraplengt=600)
    label.grid(row=0, column=0,columnspan=3)
    label.after(5000, label.destroy)

canvas = tk.Canvas(root, height=700,width=700,bg="#4169E1")
canvas.grid(row=0, column=0, columnspan=3)

auto1 = tk.Button(root, text="Auto 1", padx=10,pady=5,fg="black",highlightbackground='#3E4149', command=auto1)
auto1.grid(row=1,column=0)
auto2 = tk.Button(root, text="Auto 2", padx=10,pady=5,fg="black",highlightbackground='#3E4149', command=auto2)
auto2.grid(row=1,column=1)
auto3 = tk.Button(root, text="Auto 3", padx=10,pady=5,fg="black",highlightbackground='#3E4149', command=auto3)
auto3.grid(row=1,column=2)

root.mainloop()


#print(Kenteken_Controleren.checkReservering())

# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:53:57 2019

@author: alesa
"""
from tkinter import *
import calendario as ca
raiz = Tk()
width = 1000
height = 600
micanvas = Canvas(raiz, bg = "green", width = width, height = height)

micanvas.pack()
#Button(miframe,text="dfd",command=None).pack()

lista = []
x=80
div_width= width/16
div_height = (height-x)/12

mes = 0

def dibujar (nombre_mes, dia_inicial, dias_del_mes ):
    """Dibujar calendario
       """
    micanvas.create_text(width/2, x/3, text = nombre_mes, anchor = CENTER, font = ("Arial", "20"))
    for q in range (1,7):
        for h in range (1, 8):
            lista.append(((2*(h-1)+2)*div_width,x+(2*(q-1)+1)*div_height ))
    count = dia_inicial
    if count == 6: count = -1
    for q in range(dias_del_mes):
        count+=1
        bt_numeros = Button(raiz,width= 3, text=q+1,command=None,font = ('Arial','30'))
        micanvas.create_window(lista[count][0],lista[count][1],anchor=CENTER,window= bt_numeros)
    for dias_semana in range(7):
        micanvas.create_text((2*(dias_semana)+2)*div_width , 3*x/4, text = ca.dias[(5 + dias_semana) % 7],font = ("Arial","20"))
    
    siguiente = Button(raiz,width = 2,  anchor=W, text = ">", command  = siguiente_mes)
    micanvas.create_window(width - 30 , height/2, window = siguiente) 
    
    anterior = Button(raiz, width = 2, text = "<", command  = anterior_mes)
    micanvas.create_window(30 , height/2,  window = anterior)
    raiz.update()

def limpiar ():
    micanvas.delete("all")

  
def inicio():
    dibujar(ca.año.month[mes].name, ca.dia_ano(1,mes+1)[1], ca.año.month[mes].fef)



def siguiente_mes():
    global mes
    limpiar()
    mes += 1
    mes = mes%12
    print(mes)
    dibujar (ca.año.month[mes].name, ca.dia_ano(1,mes+1)[1], ca.año.month[mes].fef)
    
def anterior_mes():
    global mes
    limpiar()
    mes -= 1
    mes = mes%12
    print(mes)
    dibujar (ca.año.month[mes].name, ca.dia_ano(1,mes+1)[1], ca.año.month[mes].fef)  
    
inicio()

raiz.mainloop()

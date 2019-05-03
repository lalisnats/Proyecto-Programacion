# -*- coding: utf-8 -*-
"""
Created on Fri May  3 17:43:44 2019

@author: alesa
"""

import time
##############################################################################
# Clases

dias = {
     1 : "Tue" ,
     2 : "Wed" ,
     3 : "Thu" ,
     4 : "Fri" ,
     5 : "Sat" ,
     6 : "Sun" ,
     7 : "Mon"
    }
class day:
    """ Clase day:
        Crea un objeto de tipo day cuyos atributos son horas, minutos,
        segundos y el nombre del dia
        """
    def __init__(self, h = 0, m = 0, s = 0, name = None, num = 0):
        self.h = h
        self.m = m
        self.s = s
        self.name = name
        self.num = num

    def __str__(self):
        b = str(self.h) + "," + str(self.m) + "," + str(self.s)
        return b


class month:
    """ Clase month:
        Crea un objeto tipo month cuyos atributos son dias y nombre del mes
        """
    def __init__(self, days, name, num):
        self.days = [day(0,0,0,None,i) for i in range(1, days + 1)]
        self.name = name
        self.num = num
        self.fef= days


class year:
    """ Clase year:
        Crea un objeto de tipo year cuyos atibutos son tipo de año y el nombre
        del año
        """
    def __init__(self, name):
        self.month = []
        self.month.append(month(31, "Enero", "01"))
        if (int(name) % 4 == 0):
            self.month.append(month(29, "Febrero", "02"))
        else:
            self.month.append(month(28, "Febrero", "02"))
        self.month.append(month(31, "Marzo", "03"))
        self.month.append(month(30, "Abril", "04"))
        self.month.append(month(31, "Mayo", "05"))
        self.month.append(month(30, "Junio", "06"))
        self.month.append(month(31, "Julio", "07"))
        self.month.append(month(31, "Agosto", "08"))
        self.month.append(month(30, "Septiembre", "09"))
        self.month.append(month(31, "Octubre", "10"))
        self.month.append(month(30, "Noviembre", "11"))
        self.month.append(month(31, "Diciembre", "12"))
        
        self.name = name

##############################################################################
# Funciones
    
##############################################################################
# Bloque principal de instrucciones

hora = time.strftime("%H:%M:%S")
fecha = time.strftime("%a/%d/%m/%Y")

x = hora.split(":")
h = x[0]
m = x[1]
s = x[2]

y = fecha.split("/")
diana = y[0]
dianu = y[1]
me = y[2]
an = y[3]

#print(x)
#print(y)

def dia_ano (dianu, me):
    count = 0
    ano = year(an)
    for q in range (me-1):
        count += ano.month[q].fef
    count+=dianu
    print(dias[count % 7])
        

def semana_an(an):
    nombres = []
    if an % 4 == 0:
        fir= 365
    else:
        fir = 366
    count = 0
    for q in range (fir-1):
        count += 1
        f = dias[1 + q % 7]
        # print(f)
        nombres.append(f)
    return nombres

names = semana_an (2019)
año = year(y[3])

it = 0
for k in año.month:
    for l in k.days:
        l.name = names[it]
        it += 1

for k in año.month:
    h = 0
    for l in k.days:
        semana = l.name
        
        print(l.name, l.num, k.name)
#        h = 0
#        if h < 7:
#            print(l.num, end= " ")
#        else:
#            print()
#            h = 0


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 18:23:58 2019

@author: lovelace
"""
# Librerias importadas

import time

##############################################################################
# Clases

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
añ = y[3]

#print(x)
#print(y)


año = year(y[3])
#print(len(año.month))
#print(año.name)

# for i in año.month:
#     # print(i.name, i.num)
#     for j in i.days:
#         print(j.num, end = " ")
#     print()

for i in año.month:
    if i.num == me:
        for j in i.days:
            if j.num == int(dianu):
                j.name = diana

dias = []
for i in range(0, 6):
    dias.append("Mon")
    dias.append("Tue")
    dias.append("Wed")
    dias.append("Thu")
    dias.append("Fri")
    dias.append("Sat")
    dias.append("Sun")

###############################################################################

while dias[int(dianu) - 1] != diana:
    del dias[0]
while len(dias) > len(año.month[3].days):
    del dias[-1]
    #print(len(dias))
for i in range(0, len(año.month[3].days)):
    año.month[3].days[i].name = dias[i]

# print(año.month[3].name)
# print()
#for o in año.month[3].days:
 #   print(o.name, o.num)
#for j in año.month:
    #print(i.name, i.num)
for k in j.days:
    print(k.name, end = " ")
print()
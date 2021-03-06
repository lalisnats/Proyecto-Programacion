# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:01:28 2019

@author: alesa
"""

import time
##############################################################################
# Clases

dias = {
     0 : "Tue" ,
     1 : "Wed" ,
     2 : "Thu" ,
     3 : "Fri" ,
     4 : "Sat" ,
     5 : "Sun" ,
     6 : "Mon"
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
        self.month.append(month(31, "January", "01"))
        if (int(name) % 4 == 0):
            self.month.append(month(29, "February", "02"))
        else:
            self.month.append(month(28, "February", "02"))
        self.month.append(month(31, "March", "03"))
        self.month.append(month(30, "April", "04"))
        self.month.append(month(31, "May", "05"))
        self.month.append(month(30, "June", "06"))
        self.month.append(month(31, "July", "07"))
        self.month.append(month(31, "August", "08"))
        self.month.append(month(30, "September", "09"))
        self.month.append(month(31, "October", "10"))
        self.month.append(month(30, "November", "11"))
        self.month.append(month(31, "December", "12"))
        
        self.name = name

##############################################################################
# Funciones
def dia_ano (dianu, me):
    count = 0
    ano = year(an)
    for q in range (me-1):
        count += ano.month[q].fef
    count+=dianu
    return(dias[count % 7],count%7)
        

def semana_an(an):
    nombres = []
    if an % 4 == 0:
        fir= 365
    else:
        fir = 366
    count = 0
    for q in range (fir-1):
        count += 1
        f = dias[q % 7]
        # print(f)
        nombres.append(f)
    return nombres

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
        
        #print(l.name, l.num, k.name)
        
print(dia_ano(1,2)[1],año.month[1].name,año.month[1].fef)
#        h = 0
#        if h < 7:
#            print(l.num, end= " ")
#        else:
#            print()
#            h = 0
        
#str1 = calendar.month(year,month)
#print(str1)


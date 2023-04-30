#CALCULADORA DE MES

#Importar librerias
import calendar

#Definir variables
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))
dia = int(input("Ingrese el dia: "))
#Proceso

#Salida
print(calendar.monthrange(año,mes))

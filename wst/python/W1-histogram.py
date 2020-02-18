#Entspricht dem matlab-skript W1.m, erstellt von Jörg Urban
#Autor: David Spörri

import matplotlib.pyplot as plt
import numpy


# 1 Balken pro Wert
liste = [5,2,1,1,1]
x = numpy.arange(len(liste))
plt.bar(x, liste)
plt.show()

liste = [10,10, 75, 60, 60, 55, 50, 45, 75, 260]
liste_sorted = numpy.sort(liste)

plt.hist(liste, 5) # 5 Klassen
plt.show()
plt.hist(liste,[0,50,100,300])  #vordefinierte Klassengrenzen
plt.show()

mean = numpy.mean(liste)
print('Mittelwert: ' + str(mean))

# Enstpricht matlab: std(liste,1) (Faktor 1/n)
std = numpy.std(liste)
print('Standardabweichung: ' + str(std))

# Entspricht matlab: std(liste) (Faktor 1/n-1)
std1 = numpy.std(liste, ddof=1)
print('standard deviation1: ' + str(std1))

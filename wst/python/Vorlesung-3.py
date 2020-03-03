# Verschiedene Funktionen, welche in Vorlesung 3 behandelt wurden
# Autor: David Spörri
import numpy
from scipy import special

# Fakultät 3!=6
f = numpy.math.factorial(3)
print('3! = ' + str(f))

# Kombination ohne Wiederholung (nCk)
# TI-30: 10 nCr 4
nck = special.comb(10,4)
print('10 nCr 4 = ' + str(nck))

# Variation ohne Wiederholung (nPk)
# TI-30: 10 nPr 4
npr = special.comb(10,4)*numpy.math.factorial(4)
print('10 nPr 4 = ' + str(npr))

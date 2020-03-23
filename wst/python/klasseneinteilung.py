import json
import decimal
import sys
import math
import matplotlib.pyplot as plt

data = json.load(open(sys.path[0] + '/data/klassen.json'))
range = max(data) - min(data)

# get the rounding parameter of decimals the numbers in data have. example: 20.3 has a rounding of -1; 200 has a rounding of 2 
rounding = None
for i in data:
    d = 1
    while (i%d == 0):
        d = d*10
    d= d/10

    if (i%d == 0):
        log = round(math.log(d, 10))
        if (rounding == None or log < rounding):
            rounding = round(log)
            continue

    if (i%1 != 0):
        exponent = decimal.Decimal(str(i)).as_tuple().exponent
        if (rounding == None or exponent < rounding):
            rounding = exponent

print(rounding)
width = range/math.sqrt(len(data))
width = round(width, -1*rounding)
print(width)

classes = []
classAmounts = {}
classBorders = []

classStart = min(data)-(5*(10 ** (rounding-1)))
classBorders.append(classStart)

while (classStart<max(data)):
    classEnd = classStart + width
    classBorders.append(classEnd)
    thisClass = []
    for i in data:
        if (i > classStart and i < classEnd):
            thisClass.append(i)
    classes.append(thisClass)
    classAmounts[str(classStart) + ' - ' + str(classEnd)] = len(thisClass)
    classStart += width

plt.hist(data, classBorders)  # vordefinierte Klassengrenzen
plt.show()

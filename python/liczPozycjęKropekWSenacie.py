import math
def getX(a,i,m):
    return round(math.sin(math.radians(270+(180/(a-1))*i))*m)
def getY(a,i,m):
    return round(math.cos(math.radians(270+(180/(a-1))*i))*m)

a = int(input('Wprowadź liczbę rzędów: '))

i = 0;
j = 0;

while j < 10:
    while i < a:
        print(str(getX(a,i,55+(15*j)))+" "+str(getY(a,i,55+(15*j))))
        i=i+1
    j=j+1
    i=0

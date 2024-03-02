import math
def getX(a,i,m):
    return round(math.sin(math.radians(270+(180/(a-1))*i))*m)
def getY(a,i,m):
    return round(math.cos(math.radians(270+(180/(a-1))*i))*m)

a = int(input('Wprowadź liczbę rzędów: '))

i = 0;
j = 0;
f = open("senate.gui","w",newline='\r\n')
while j < 10:
    while i < a:
        f.write("icontype = {\n\t"+
            "name = \"GFX_CAL_senate_seat_"+str(i)+"_"+str(j)+"\"\n\t"+
            "position = {\n\t\t"+
                "x = "+str(getX(a,i,55+(15*j))+250)+"\n\t\t"+
                "y = "+str(200-getY(a,i,55+(15*j)))+"\n\t"+
            "}\n\t"+
            "spriteType = \"GFX_neutral_seat\"\n}\n")
        i=i+1
    j=j+1
    i=0
f.close()

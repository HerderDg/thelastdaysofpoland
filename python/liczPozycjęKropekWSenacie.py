import math
def getX(a,i,m):
    return round(math.sin(math.radians(270+(180/(a-1))*i))*m)
def getY(a,i,m):
    return round(math.cos(math.radians(270+(180/(a-1))*i))*m)

a = int(input('Wprowadź liczbę miejsc: '))
x = 250
y = 200
i = 0
j = 0
r = 55
p = math.ceil(math.pi*r/9)
f = open("senate.gui","w",newline='\r\n')
t = open("triggers.txt","w",newline='\r\n')
f.write("containerWindowType = {\n\t"+
	"name = \"GFX_CAL_senate_seats\"\n\t"+
	"position = { x = 0 y = 0 }\n\t")
t.write("triggers = {\n\t")
while i < a:
    # print ("x = "+str(x+getX(p,i,r)))
    # print ("y = "+str(y-getX(p,i,r)))
    f.write("icontype = {\n\t\t"+
        "name = \"GFX_CAL_senate_seat_"+str(i)+"\"\n\t\t"+
        "position = {\n\t\t\t"+
            "x = "+str(x+getX(p,j,r))+"\n\t\t\t"+
            "y = "+str(y-getY(p,j,r))+"\n\t\t"+
        "}\n\t\t"+
        "scale = 0.6\n\t\t"+
        "spriteType = \"GFX_neutral_seat\"\n\t}\n\t")
    if i >= 100 and i < 150 :
        t.write("GFX_CAL_senate_seat_"+str(i)+"_visible = { check_variable = { CAL_senate_lvl > 1 } }\n\t")
    elif i >= 150 and i < 300:
        t.write("GFX_CAL_senate_seat_"+str(i)+"_visible = { check_variable = { CAL_senate_lvl > 2 } }\n\t")
    elif i >= 300:
        t.write("GFX_CAL_senate_seat_"+str(i)+"_visible = { check_variable = { CAL_senate_lvl = 4 } }\n\t")
    i=i+1
    j=j+1
    if j==p:
        r=r+9
        p = math.ceil(math.pi*r/9)
        j=0

f.write("}")
f.close()
t.write("}")
t.close()
# while j < 10:
#     while i < a:
#         f.write("icontype = {\n\t"+
#             "name = \"GFX_CAL_senate_seat_"+str(i)+"_"+str(j)+"\"\n\t"+
#             "position = {\n\t\t"+
#                 "x = "+str(getX(a,i,55+(15*j))+250)+"\n\t\t"+
#                 "y = "+str(200-getY(a,i,55+(15*j)))+"\n\t"+
#             "}\n\t"+
#             "spriteType = \"GFX_neutral_seat\"\n}\n")
#         i=i+1
#     j=j+1
#     i=0


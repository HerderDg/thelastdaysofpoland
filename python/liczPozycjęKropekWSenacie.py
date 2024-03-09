import math
def getX(a,i,m):
    return round(math.sin(math.radians(270+(180/(a-1))*i))*m)
def getY(a,i,m):
    return round(math.cos(math.radians(270+(180/(a-1))*i))*m)


x = 250
y = 200
i = 0
j = 0
r = 55
p = math.ceil(math.pi*r/9)
f = open("senate.gui","w",newline='\r\n')
t = open("triggers.txt","w",newline='\r\n')
props = open("properties.txt","w",newline='\r\n')
scriptedLocs = open("CAL_senate_scripted_loc.txt","w",newline='\r\n')
f.write("containerWindowType = {\n\t"+
	"name = \"GFX_CAL_senate_seats\"\n\t"+
	"position = { x = 0 y = 0 }\n\t")
t.write("triggers = {\n\t")
while i < 900:
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
    props.write("GFX_CAL_senate_seat_"+str(i)+" = { image = \"[GetSeatDotNo"+str(i)+"]\"}\n")
    if i >= 100 and i < 150 :
        t.write("GFX_CAL_senate_seat_"+str(i)+"_visible = { check_variable = { CAL_senate_lvl > 1 } }\n\t")
    elif i >= 150 and i < 300:
        t.write("GFX_CAL_senate_seat_"+str(i)+"_visible = { check_variable = { CAL_senate_lvl > 2 } }\n\t")
    elif i >= 300:
        t.write("GFX_CAL_senate_seat_"+str(i)+"_visible = { check_variable = { CAL_senate_lvl = 4 } }\n\t")
    scriptedLocs.write("defined_text = {\n\t"+
        "name = GetSeatDotNo"+str(i)+"\n\t")#+
#        "text = {\n\t\t"+
#            "localisation_key = GFX_optimates_seat\n\t}\n")
    if i < 20:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row1 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
    if i >= 20 and i < 43:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row2 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
    if i >= 43 and i < 69:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row3 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
    if i >= 69 and i < 98:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row4 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
    if i >= 98 and  i < 130:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row5 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
    if i >= 130 and  i < 165:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row6 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
    if i >= 165 and  i < 204:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row7 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
    if i >= 204 and  i < 246:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row8 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
    if i >= 246 and  i < 291:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row9 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
    if i >= 291 and  i < 339:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row10 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
    if i >= 339 and  i < 390:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row11 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
    if i >= 390 and  i < 444:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row12 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
    if i >= 444 and  i < 501:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row13 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
    if i >= 501 and  i < 562:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row14 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
    if i >= 562 and  i < 626:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row15 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
    if i >= 626 and  i < 693:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row16 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
    if i >= 693 and  i < 763:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row17 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
    if i >= 763 and  i < 836:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row18 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
    if i >= 836:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row19 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
    scriptedLocs.write("text = {\n\t\t"+
            "localization_key = GFX_optimates_seat\n\t}\n")
    scriptedLocs.write("}\n")
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
props.close()
scriptedLocs.close()
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


import math
def getX(a,i,m):
    return round(math.sin(math.radians(270+(180/(a-1))*i))*m)
def getY(a,i,m):
    return round(math.cos(math.radians(270+(180/(a-1))*i))*m)


x = 250
y = 220
i = 0
j = 0
r = 55
p = 21
f = open("senate.gui","w",newline='\r\n')
t = open("triggers.txt","w",newline='\r\n')
props = open("properties.txt","w",newline='\r\n')
scriptedLocs = open("CAL_senate_scripted_loc.txt","w",newline='\r\n')
f.write("containerWindowType = {\n\t"+
	"name = \"GFX_CAL_senate_seats\"\n\t"+
	"position = { x = 0 y = 0 }\n\t")
t.write("triggers = {\n\t")
while i < 900:

    f.write("icontype = {\n\t\t"+
        "name = \"GFX_CAL_senate_seat_"+str(i)+"\"\n\t\t"+
        "position = {\n\t\t\t"+
            "x = "+str(x+getX(p,j,r))+"\n\t\t\t"+
            "y = "+str(y-getY(p,j,r))+"\n\t\t"+
        "}\n\t\t"+
        "scale = 0.6\n\t\t"+
        "spriteType = \"GFX_neutral_seat\"\n\t}\n\t")
    scriptedLocs.write("defined_text = {\n\t"+
        "name = GetSeatDotNo"+str(i)+"\n\t")
    if i < 21:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row1 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row1 < "+str(j+1)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row1 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row1 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_hard_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row1 < "+str(j+1)+" }\n\t\t\t"
                "check_variable = { CAL_optimates_hard_at_row1 > "+str(20-j)+" }\n\t\t\t"
            "}\n\t\t"+
            "localization_key = GFX_optimates_hard_seat\n\t}\n\t")
    if i >= 21 and i < 45:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row2 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row2 < "+str(j+1)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row2 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row2 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_hard_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row2 < "+str(j+1)+" }\n\t\t\t"
                "check_variable = { CAL_optimates_hard_at_row2 > "+str(23-j)+" }\n\t\t\t"
            "}\n\t\t"+
            "localization_key = GFX_optimates_hard_seat\n\t}\n\t")
    if i >= 45 and i < 71:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row3 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row3 < "+str(j+1)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row3 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row3 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_hard_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row3 < "+str(j+1)+" }\n\t\t\t"
                "check_variable = { CAL_optimates_hard_at_row3 > "+str(25-j)+" }\n\t\t\t"
            "}\n\t\t"+
            "localization_key = GFX_optimates_hard_seat\n\t}\n\t")
    if i >= 71 and i < 100:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row4 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row4 < "+str(j+1)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row4 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row4 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_hard_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row4 < "+str(j+1)+" }\n\t\t\t"
                "check_variable = { CAL_optimates_hard_at_row4 > "+str(28-j)+" }\n\t\t\t"
            "}\n\t\t"+
            "localization_key = GFX_optimates_hard_seat\n\t}\n\t")
    if i >= 100 and  i < 125:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row5 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row5 < "+str(j+1)+"}\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row5 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row5 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_hard_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row5 < "+str(j+1)+" }\n\t\t\t"
                "check_variable = { CAL_optimates_hard_at_row5 > "+str(24-j)+" }\n\t\t\t"
            "}\n\t\t"+
            "localization_key = GFX_optimates_hard_seat\n\t}\n\t")
    if i >= 125 and  i < 150:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row6 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row6 < "+str(j+1)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row6 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row6 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_hard_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row6 < "+str(j+1)+" }\n\t\t\t"
                "check_variable = { CAL_optimates_hard_at_row6 > "+str(24-j)+" }\n\t\t\t"
            "}\n\t\t"+
            "localization_key = GFX_optimates_hard_seat\n\t}\n\t")
    if i >= 150 and  i < 183:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row7 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row7 < "+str(j+1)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row7 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row7 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_hard_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row7 < "+str(j+1)+" }\n\t\t\t"
                "check_variable = { CAL_optimates_hard_at_row7 > "+str(32-j)+" }\n\t\t\t"
            "}\n\t\t"+
            "localization_key = GFX_optimates_hard_seat\n\t}\n\t")
    if i >= 183 and  i < 218:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row8 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row8 < "+str(j+1)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row8 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row8 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_hard_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row8 < "+str(j+1)+" }\n\t\t\t"
                "check_variable = { CAL_optimates_hard_at_row8 > "+str(34-j)+" }\n\t\t\t"
            "}\n\t\t"+
            "localization_key = GFX_optimates_hard_seat\n\t}\n\t")
    if i >= 218 and  i < 257:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row9 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row9 < "+str(j+1)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row9 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row9 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_hard_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row9 < "+str(j+1)+" }\n\t\t\t"
                "check_variable = { CAL_optimates_hard_at_row9 > "+str(38-j)+" }\n\t\t\t"
            "}\n\t\t"+
            "localization_key = GFX_optimates_hard_seat\n\t}\n\t")
    if i >= 257 and  i < 300:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row10 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row10 < "+str(j+1)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row10 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row10 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_hard_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row10 < "+str(j+1)+" }\n\t\t\t"
                "check_variable = { CAL_optimates_hard_at_row10 > "+str(42-j)+" }\n\t\t\t"
            "}\n\t\t"+
            "localization_key = GFX_optimates_hard_seat\n\t}\n\t")
    if i >= 300 and  i < 347:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row11 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row11 < "+str(j+1)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row11 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row11 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_hard_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row11 < "+str(j+1)+" }\n\t\t\t"
                "check_variable = { CAL_optimates_hard_at_row11 > "+str(46-j)+" }\n\t\t\t"
            "}\n\t\t"+
            "localization_key = GFX_optimates_hard_seat\n\t}\n\t")
    if i >= 347 and  i < 456:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row12 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row12 < "+str(j+1)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row12 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row12 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_hard_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row12 < "+str(j+1)+" }\n\t\t\t"
                "check_variable = { CAL_optimates_hard_at_row12 > "+str(51-j)+" }\n\t\t\t"
            "}\n\t\t"+
            "localization_key = GFX_optimates_hard_seat\n\t}\n\t")
    if i >= 399 and  i < 456:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row13 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row13 < "+str(j+1)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row13 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row13 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_hard_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row13 < "+str(j+1)+" }\n\t\t\t"
                "check_variable = { CAL_optimates_hard_at_row13 > "+str(56-j)+" }\n\t\t\t"
            "}\n\t\t"+
            "localization_key = GFX_optimates_hard_seat\n\t}\n\t")
    if i >= 456 and  i < 516:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row14 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row14 < "+str(j+1)+"}\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row14 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row14 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_hard_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row14 < "+str(j+1)+" }\n\t\t\t"
                "check_variable = { CAL_optimates_hard_at_row14 > "+str(59-j)+" }\n\t\t\t"
            "}\n\t\t"+
            "localization_key = GFX_optimates_hard_seat\n\t}\n\t")
    if i >= 516 and  i < 579:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row15 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row15 < "+str(j+1)+"}\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row15 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row15 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_hard_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row15 < "+str(j+1)+" }\n\t\t\t"
                "check_variable = { CAL_optimates_hard_at_row15 > "+str(62-j)+" }\n\t\t\t"
            "}\n\t\t"+
            "localization_key = GFX_optimates_hard_seat\n\t}\n\t")
    if i >= 579 and  i < 648:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row16 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row16 < "+str(j+1)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row16 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row16 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_hard_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row16 < "+str(j+1)+" }\n\t\t\t"
                "check_variable = { CAL_optimates_hard_at_row16 > "+str(68-j)+" }\n\t\t\t"
            "}\n\t\t"+
            "localization_key = GFX_optimates_hard_seat\n\t}\n\t")
    if i >= 648 and  i < 724:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row17 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row17 < "+str(j+1)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row17 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row17 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_hard_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row17 < "+str(j+1)+" }\n\t\t\t"
                "check_variable = { CAL_optimates_hard_at_row17 > "+str(75-j)+" }\n\t\t\t"
            "}\n\t\t"+
            "localization_key = GFX_optimates_hard_seat\n\t}\n\t")
    if i >= 724 and  i < 808:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row18 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row18 < "+str(j+1)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row18 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row18 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_hard_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row18 < "+str(j+1)+" }\n\t\t\t"
                "check_variable = { CAL_optimates_hard_at_row18 > "+str(83-j)+" }\n\t\t\t"
            "}\n\t\t"+
            "localization_key = GFX_optimates_hard_seat\n\t}\n\t")
    if i >= 808:
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row19 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row19 < "+str(j+1)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row19 > "+str(j)+" }\n\t\t\t"
                "check_variable = { CAL_populares_hard_at_row19 > "+str(j)+" }\n\t\t"
            "}\n\t\t"+
            "localization_key = GFX_populares_hard_seat\n\t}\n\t")
        scriptedLocs.write("text = {\n\t\t"+
            "trigger = {\n\t\t\t"+
                "check_variable = { CAL_populares_at_row19 < "+str(j+1)+" }\n\t\t\t"
                "check_variable = { CAL_optimates_hard_at_row19 > "+str(92-j)+" }\n\t\t\t"
            "}\n\t\t"+
            "localization_key = GFX_optimates_hard_seat\n\t}\n\t")
    scriptedLocs.write("text = {\n\t\t"+
            "localization_key = GFX_optimates_seat\n\t}\n")
    scriptedLocs.write("}\n")
    i=i+1
    j=j+1
    if j==p:
        r=r+9
        j=0
    match i:
        case 21:
            p=24
        case 45:
            p=26
        case 71:
            p=29
        case 100:
            p=25
        case 150:
            p=33
        case 183:
            p=35
        case 218:
            p=39
        case 257:
            p=43
        case 300:
            p=47
        case 347:
            p=52
        case 399:
            p=57
        case 456:
            p=60
        case 516:
            p=63
        case 579:
            p=69
        case 648:
            p=76
        case 724:
            p=84
        case 808:
            p=92
        

f.write("}")
f.close()
t.write("}")
t.close()
props.close()
scriptedLocs.close()



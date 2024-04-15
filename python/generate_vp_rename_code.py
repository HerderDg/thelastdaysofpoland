import string;


f = open("victory_points_l_english.yml","r",encoding="utf_8_sig",newline='\r\n')
array_create = open("generate_vp_arrays.txt","w",newline='\r\n')
# latin = open("change_vp_name_to_latin.txt","w",newline='\r\n')
# czepanese = open("change_vp_name_to_czepanese.txt","w",newline='\r\n')
# german = open("change_vp_name_to_german.txt","w",newline='\r\n')
# nordic = open("change_vp_name_to_nordic.txt","w",newline='\r\n')
# lechite = open("change_vp_name_to_lechite.txt","w",newline='\r\n')
# russian = open("change_vp_name_to_russian.txt","w",newline='\r\n')
# kolonkish = open("change_vp_name_to_kolonkish.txt","w",newline='\r\n')
# kashubian = open("change_vp_name_to_kashubian.txt","w",newline='\r\n')
# notthatprussian = open("change_vp_name_to_notthatprussian.txt","w",newline='\r\n')
# silesian = open("change_vp_name_to_silesian.txt","w",newline='\r\n')
# polish = open("reset_vp_name.txt","w",newline='\r\n')
provinceIDs = []
provinceIDs_KSZ = []
provinceIDs_PRU = []
provinceIDs_SIL = []
while True:
    line = f.readline()
    if not line:
        break
    elif "\"" in line:
        if line.split(':')[0].split('_')[2] not in provinceIDs:
            provinceIDs.append(line.split(':')[0].split('_')[2])
        if len(line.split(':')[0].split('_')) == 4:
            language = line.split(':')[0].split('_')[3]
        else: language = "POL"
        if language == "KSZ" and line.split(':')[0].split('_')[2] not in provinceIDs_KSZ:
            provinceIDs_KSZ.append(line.split(':')[0].split('_')[2])
        elif language == "PRU" and line.split(':')[0].split('_')[2] not in provinceIDs_PRU:
            provinceIDs_PRU.append(line.split(':')[0].split('_')[2])
        elif language == "SIL" and line.split(':')[0].split('_')[2] not in provinceIDs_SIL:
            provinceIDs_SIL.append(line.split(':')[0].split('_')[2])
f.close()
for provinceID in provinceIDs:
    array_create.write("add_to_array = { global.vps_to_rename = "+provinceID+" }\n")
for provinceID in provinceIDs_KSZ:
    array_create.write("add_to_array = { global.KSZ_vps_to_rename = "+provinceID+" }\n")
for provinceID in provinceIDs_PRU:
    array_create.write("add_to_array = { global.PRU_vps_to_rename = "+provinceID+" }\n")
for provinceID in provinceIDs_SIL:
    array_create.write("add_to_array = { global.SIL_vps_to_rename = "+provinceID+" }\n")
array_create.close()
# polish.close();
# latin.close();
# czepanese.close();
# german.close();
# nordic.close();
# lechite.close();
# russian.close();
# kolonkish.close();
# kashubian.close();
# notthatprussian.close();
# silesian.close();

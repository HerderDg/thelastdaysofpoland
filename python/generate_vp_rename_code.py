import string;


f = open("victory_points_l_english.yml","r",encoding="utf_8_sig",newline='\r\n')
latin = open("change_vp_name_to_latin.txt","w",newline='\r\n')
czepanese = open("change_vp_name_to_czepanese.txt","w",newline='\r\n')
german = open("change_vp_name_to_german.txt","w",newline='\r\n')
nordic = open("change_vp_name_to_nordic.txt","w",newline='\r\n')
lechite = open("change_vp_name_to_lechite.txt","w",newline='\r\n')
russian = open("change_vp_name_to_russian.txt","w",newline='\r\n')
kolonkish = open("change_vp_name_to_kolonkish.txt","w",newline='\r\n')
kashubian = open("change_vp_name_to_kashubian.txt","w",newline='\r\n')
notthatprussian = open("change_vp_name_to_notthatprussian.txt","w",newline='\r\n')
silesian = open("change_vp_name_to_silesian.txt","w",newline='\r\n')
polish = open("reset_vp_name.txt","w",newline='\r\n')
czepanese.write("change_vp_name_to_czepanese = {\n")
kashubian.write("change_vp_name_to_kashubian = {\n")
german.write("change_vp_name_to_german = {\n")
nordic.write("change_vp_name_to_nordic = {\n")
latin.write("change_vp_name_to_latin = {\n")
lechite.write("change_vp_name_to_lechite = {\n")
russian.write("change_vp_name_to_russian = {\n")
kolonkish.write("change_vp_name_to_kolonkish = {\n")
notthatprussian.write("change_vp_name_to_notthatprussian = {\n")
silesian.write("change_vp_name_to_silesian = {\n")
polish.write("reset_vp_name = {\n")

while True:
    line = f.readline();
    if not line:
        break
    elif "\"" in line:
        province_id = line.split(':')[0].split('_')[2]
        if len(line.split(':')[0].split('_')) == 4:
            language = line.split(':')[0].split('_')[3];
        else: language = "POL";
        #print(language);
        if language == "POL":
            polish.write("\tif = {\n\t\tlimit = {\n\t\t\tcontrols_province = "+province_id+"\n\t\t}\n\t\tset_province_name = {\n\t\t\tid = "+province_id+"\n\t\t\tname = VICTORY_POINTS_"+province_id+"\n\t\t}\n\t}\n");
        elif language == "CAL":
            if province_id in ["13760","13763","13771"]:
                latin.write("\tif = {\n\t\tlimit = {\n\t\t\tcontrols_province = "+province_id+"\n\t\t\tNOT = {\n\t\t\t\thas_global_flag = CAL_"+province_id+"_alt_name\n\t\t\t}\n\t\t}\n\t\tset_province_name = {\n\t\t\tid = "+province_id+"\n\t\t\tname = VICTORY_POINTS_"+province_id+"_CAL\n\t\t}\n\t}\n");
            else:
                latin.write("\tif = {\n\t\tlimit = {\n\t\t\tcontrols_province = "+province_id+"\n\t\t}\n\t\tset_province_name = {\n\t\t\tid = "+province_id+"\n\t\t\tname = VICTORY_POINTS_"+province_id+"_CAL\n\t\t}\n\t}\n");
        elif language == "CAL2":
            latin.write("\tif = {\n\t\tlimit = {\n\t\t\tcontrols_province = "+province_id+"\n\t\t\thas_global_flag = CAL_"+province_id+"_alt_name\n\t\t}\n\t\tset_province_name = {\n\t\t\tid = "+province_id+"\n\t\t\tname = VICTORY_POINTS_"+province_id+"_CAL2\n\t\t}\n\t}\n");
        elif language == "CZE":
            czepanese.write("\tif = {\n\t\tlimit = {\n\t\t\tcontrols_province = "+province_id+"\n\t\t}\n\t\tset_province_name = {\n\t\t\tid = "+province_id+"\n\t\t\tname = VICTORY_POINTS_"+province_id+"_CZE\n\t\t}\n\t}\n");
        elif language == "GER":   
            german.write("\tif = {\n\t\tlimit = {\n\t\t\tcontrols_province = "+province_id+"\n\t\t}\n\t\tset_province_name = {\n\t\t\tid = "+province_id+"\n\t\t\tname = VICTORY_POINTS_"+province_id+"_GER\n\t\t}\n\t}\n");
        elif language == "JOM":
            nordic.write("\tif = {\n\t\tlimit = {\n\t\t\tcontrols_province = "+province_id+"\n\t\t}\n\t\tset_province_name = {\n\t\t\tid = "+province_id+"\n\t\t\tname = VICTORY_POINTS_"+province_id+"_JOM\n\t\t}\n\t}\n");
        elif language == "LEH":
            lechite.write("\tif = {\n\t\tlimit = {\n\t\t\tcontrols_province = "+province_id+"\n\t\t}\n\t\tset_province_name = {\n\t\t\tid = "+province_id+"\n\t\t\tname = VICTORY_POINTS_"+province_id+"_LEH\n\t\t}\n\t}\n");
        elif language == "UKROS":
            russian.write("\tif = {\n\t\tlimit = {\n\t\t\tcontrols_province = "+province_id+"\n\t\t}\n\t\tset_province_name = {\n\t\t\tid = "+province_id+"\n\t\t\tname = VICTORY_POINTS_"+province_id+"_UKROS\n\t\t}\n\t}\n");
        elif language == "USP":
            kolonkish.write("\tif = {\n\t\tlimit = {\n\t\t\tcontrols_province = "+province_id+"\n\t\t}\n\t\tset_province_name = {\n\t\t\tid = "+province_id+"\n\t\t\tname = VICTORY_POINTS_"+province_id+"_USP\n\t\t}\n\t}\n");
        elif language == "KSZ":
            kashubian.write("\tif = {\n\t\tlimit = {\n\t\t\tcontrols_province = "+province_id+"\n\t\t}\n\t\tset_province_name = {\n\t\t\tid = "+province_id+"\n\t\t\tname = VICTORY_POINTS_"+province_id+"_KSZ\n\t\t}\n\t}\n");
        elif language == "PRU":
            notthatprussian.write("\tif = {\n\t\tlimit = {\n\t\t\tcontrols_province = "+province_id+"\n\t\t}\n\t\tset_province_name = {\n\t\t\tid = "+province_id+"\n\t\t\tname = VICTORY_POINTS_"+province_id+"_PRU\n\t\t}\n\t}\n");
        elif language == "SIL":
            silesian.write("\tif = {\n\t\tlimit = {\n\t\t\tcontrols_province = "+province_id+"\n\t\t}\n\t\tset_province_name = {\n\t\t\tid = "+province_id+"\n\t\t\tname = VICTORY_POINTS_"+province_id+"_SIL\n\t\t}\n\t}\n");
f.close();
polish.write("}")
polish.close();
latin.write("}")
latin.close();
czepanese.write("}")
czepanese.close();
german.write("}")
german.close();
nordic.write("}")
nordic.close();
lechite.write("}")
lechite.close();
russian.write("}")
russian.close();
kolonkish.write("}")
kolonkish.close();
kashubian.write("}")
kashubian.close()
notthatprussian.write("}");
notthatprussian.close();
silesian.write("}")
silesian.close();

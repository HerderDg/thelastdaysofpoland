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
            polish.write("if = {\n\tlimit = {\n\t\tcontrols_province = "+province_id+"\n\t}\n\tset_province_name = {\n\t\tid = "+province_id+"\n\t\tname = VICTORY_POINTS_"+province_id+"\n\t}\n}\n");
        elif language == "CAL":
            latin.write("if = {\n\tlimit = {\n\t\tcontrols_province = "+province_id+"\n\t}\n\tset_province_name = {\n\t\tid = "+province_id+"\n\t\tname = VICTORY_POINTS_"+province_id+"_CAL\n\t}\n}\n");
        elif language == "CZE":
            czepanese.write("if = {\n\tlimit = {\n\t\tcontrols_province = "+province_id+"\n\t}\n\tset_province_name = {\n\t\tid = "+province_id+"\n\t\tname = VICTORY_POINTS_"+province_id+"_CZE\n\t}\n}\n");
        elif language == "GER":   
            german.write("if = {\n\tlimit = {\n\t\tcontrols_province = "+province_id+"\n\t}\n\tset_province_name = {\n\t\tid = "+province_id+"\n\t\tname = VICTORY_POINTS_"+province_id+"_GER\n\t}\n}\n");
        elif language == "JOM":
            nordic.write("if = {\n\tlimit = {\n\t\tcontrols_province = "+province_id+"\n\t}\n\tset_province_name = {\n\t\tid = "+province_id+"\n\t\tname = VICTORY_POINTS_"+province_id+"_JOM\n\t}\n}\n");
        elif language == "LEH":
            lechite.write("if = {\n\tlimit = {\n\t\tcontrols_province = "+province_id+"\n\t}\n\tset_province_name = {\n\t\tid = "+province_id+"\n\t\tname = VICTORY_POINTS_"+province_id+"_LEH\n\t}\n}\n");
        elif language == "UKROS":
            russian.write("if = {\n\tlimit = {\n\t\tcontrols_province = "+province_id+"\n\t}\n\tset_province_name = {\n\t\tid = "+province_id+"\n\t\tname = VICTORY_POINTS_"+province_id+"_UKROS\n\t}\n}\n");
        elif language == "USP":
            kolonkish.write("if = {\n\tlimit = {\n\t\tcontrols_province = "+province_id+"\n\t}\n\tset_province_name = {\n\t\tid = "+province_id+"\n\t\tname = VICTORY_POINTS_"+province_id+"_USP\n\t}\n}\n");
        elif language == "KSZ":
            kashubian.write("if = {\n\tlimit = {\n\t\tcontrols_province = "+province_id+"\n\t}\n\tset_province_name = {\n\t\tid = "+province_id+"\n\t\tname = VICTORY_POINTS_"+province_id+"_KSZ\n\t}\n}\n");
        elif language == "PRU":
            notthatprussian.write("if = {\n\tlimit = {\n\t\tcontrols_province = "+province_id+"\n\t}\n\tset_province_name = {\n\t\tid = "+province_id+"\n\t\tname = VICTORY_POINTS_"+province_id+"_PRU\n\t}\n}\n");
        elif language == "SIL":
            silesian.write("if = {\n\tlimit = {\n\t\tcontrols_province = "+province_id+"\n\t}\n\tset_province_name = {\n\t\tid = "+province_id+"\n\t\tname = VICTORY_POINTS_"+province_id+"_SIL\n\t}\n}\n");
f.close();
polish.close();
latin.close();
czepanese.close();
german.close();
nordic.close();
lechite.close();
russian.close();
kolonkish.close();
kashubian.close();
notthatprussian.close();
silesian.close();

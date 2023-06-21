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
polish = open("reset_vp_name.txt","w",newline='\r\n')

while True:
    line = f.readline();
    if not line:
        break
    elif line.split(':')[0].endswith(tuple(string.digits)):
        province_id = line.split(':')[0].split('_')[2]
        polish.write("if = {\n\tlimit = {\n\t\tcontrols_province = "+province_id+"\n\t}\n\tset_province_name = {\n\t\tid = "+province_id+"\n\t\tname = VICTORY_POINTS_"+province_id+"\n\t}\n}\n");
        latin.write("if = {\n\tlimit = {\n\t\tcontrols_province = "+province_id+"\n\t}\n\tset_province_name = {\n\t\tid = "+province_id+"\n\t\tname = VICTORY_POINTS_"+province_id+"_CAL\n\t}\n}\n");
        czepanese.write("if = {\n\tlimit = {\n\t\tcontrols_province = "+province_id+"\n\t}\n\tset_province_name = {\n\t\tid = "+province_id+"\n\t\tname = VICTORY_POINTS_"+province_id+"_CZE\n\t}\n}\n");
        german.write("if = {\n\tlimit = {\n\t\tcontrols_province = "+province_id+"\n\t}\n\tset_province_name = {\n\t\tid = "+province_id+"\n\t\tname = VICTORY_POINTS_"+province_id+"_GER\n\t}\n}\n");
        nordic.write("if = {\n\tlimit = {\n\t\tcontrols_province = "+province_id+"\n\t}\n\tset_province_name = {\n\t\tid = "+province_id+"\n\t\tname = VICTORY_POINTS_"+province_id+"_JOM\n\t}\n}\n");
        lechite.write("if = {\n\tlimit = {\n\t\tcontrols_province = "+province_id+"\n\t}\n\tset_province_name = {\n\t\tid = "+province_id+"\n\t\tname = VICTORY_POINTS_"+province_id+"_LEH\n\t}\n}\n");
        russian.write("if = {\n\tlimit = {\n\t\tcontrols_province = "+province_id+"\n\t}\n\tset_province_name = {\n\t\tid = "+province_id+"\n\t\tname = VICTORY_POINTS_"+province_id+"_UKROS\n\t}\n}\n");
        kolonkish.write("if = {\n\tlimit = {\n\t\tcontrols_province = "+province_id+"\n\t}\n\tset_province_name = {\n\t\tid = "+province_id+"\n\t\tname = VICTORY_POINTS_"+province_id+"_USP\n\t}\n}\n");
        kashubian.write("if = {\n\tlimit = {\n\t\tcontrols_province = "+province_id+"\n\t}\n\tset_province_name = {\n\t\tid = "+province_id+"\n\t\tname = VICTORY_POINTS_"+province_id+"_KSZ\n\t}\n}\n");
        notthatprussian.write("if = {\n\tlimit = {\n\t\tcontrols_province = "+province_id+"\n\t}\n\tset_province_name = {\n\t\tid = "+province_id+"\n\t\tname = VICTORY_POINTS_"+province_id+"_PRU\n\t}\n}\n");
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
on_actions = open("on_actions.txt","w",newline='\r\n')
for tag in ['CAL']:
    on_actions.write("on_daily_"+tag+" = {\n\teffect = {\n\t\tchange_vp_name_to_latin = yes\n\t}\n}\n");
for tag in ['KAM','MNI','RAS','WRT','POM','KES','KOS','TEU','GER']:
    on_actions.write("on_daily_"+tag+" = {\n\teffect = {\n\t\tchange_vp_name_to_german = yes\n\t}\n}\n");
for tag in ['LEH','LCH','WAN','JAS']:
    on_actions.write("on_daily_"+tag+" = {\n\teffect = {\n\t\tchange_vp_name_to_lechite = yes\n\t}\n}\n");
for tag in ['UPA','KOZ','UHR','BEL','ROS']:
    on_actions.write("on_daily_"+tag+" = {\n\teffect = {\n\t\tchange_vp_name_to_russian = yes\n\t}\n}\n");
for tag in ['KSZ']:
    on_actions.write("on_daily_"+tag+" = {\n\teffect = {\n\t\tchange_vp_name_to_kashubian = yes\n\t}\n}\n");
for tag in ['PRU']:
    on_actions.write("on_daily_"+tag+" = {\n\teffect = {\n\t\tchange_vp_name_to_notthatprussian = yes\n\t}\n}\n");
for tag in ['CHO','GLI','FER','RUD','JSW','TRC']:
    on_actions.write("#on_daily_"+tag+" = {\n#\teffect = {\n#\t\tchange_vp_name_to_silesian = yes\n#\t}\n#}\n");
on_actions.close();

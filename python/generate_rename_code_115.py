import string;


vp = open("victory_points_l_english.yml","r",encoding="utf_8_sig",newline='\r\n')
vp_new = open("victory_points_l_english_new.yml","w",encoding="utf_8_sig",newline='\n')
vp_new.write("l_english:\n")

while True:
    line = vp.readline();
    if not line:
        break
    elif "\"" in line:
        province_id = line.split(':')[0].split('_')[2]
        if len(line.split(':')[0].split('_')) == 4:
            language = line.split(':')[0].split('_')[3];
        else: language = "POL";
        if language == "CAL":
            for tag in ['CAL','ALP','PRT']:
                vp_new.write(' '+tag+'_'+line.split(':')[0].replace('_'+language,'')+':'+line.split(':')[1])
        elif language == "JOM":
            for tag in ['JOM','JUT']:
                vp_new.write(' '+tag+'_'+line.split(':')[0].replace('_'+language,'')+':'+line.split(':')[1])
        elif language == "PRU":
            for tag in ['PRU','AES','GAL']:
                vp_new.write(' '+tag+'_'+line.split(':')[0].replace('_'+language,'')+':'+line.split(':')[1])
        elif language == "KSZ":
            for tag in ['KSZ','KSC']:
                vp_new.write(' '+tag+'_'+line.split(':')[0].replace('_'+language,'')+':'+line.split(':')[1])
        elif language == "CZE":
            vp_new.write(' CZE_'+line.split(':')[0].replace('_'+language,'')+':'+line.split(':')[1])
        elif language == "GER":
            for tag in ['GER', 'KAM', 'MNI', 'RAS', 'WRT', 
                        'POM', 'KES', 'KOS', 'TEU', 'BRG', 
                        'BRE', 'KLB', 'OST', 'WIZ', 'FRK',
                        'VAN', 'SAX', 'EKS', 'EKW', 'TOU', 'BOG', 'LUB']:
                vp_new.write(' '+tag+'_'+line.split(':')[0].replace('_'+language,'')+':'+line.split(':')[1])
        elif language == "UKROS":
            for tag in ['UPA', 'KOZ', 'UHR', 'BEL', 'ROS', 'RUS', 'RMA', 'UKR', 'LEM']:
                vp_new.write(' '+tag+'_'+line.split(':')[0].replace('_'+language,'')+':'+line.split(':')[1])
        elif language == "LEH":
            for tag in ['LEH', 'LCH', 'WAN', 'JAS', 'SNF', 'BOR', 'STR']:
                vp_new.write(' '+tag+'_'+line.split(':')[0].replace('_'+language,'')+':'+line.split(':')[1])
        elif language == "SIL":
            for tag in [ 'CHO', 'GLI', 'FER', 'RUD', 'JSW', 'TRC', 'DUR', 'SBW', 'WYM']:
                vp_new.write(' '+tag+'_'+line.split(':')[0].replace('_'+language,'')+':'+line.split(':')[1])
        elif language == "USP":
            vp_new.write(' USP_'+line.split(':')[0].replace('_'+language,'')+':'+line.split(':')[1])
        elif language == "POL":
            vp_new.write(' '+line.split(':')[0].replace('_'+language,'')+':'+line.split(':')[1])
        elif language == "CAL2":
            vp_new.write(' '+'CAL_'+line.split(':')[0].replace('_'+language,'_ALT')+':'+line.split(':')[1])
        else:
            print(line)
vp.close();
vp_new.close()

# s = open("state_names_l_english.yml","r",encoding="utf_8_sig",newline='\r\n')
# s_new = open("state_names_l_english_new.yml","w",encoding="utf_8_sig",newline='\n')


# s_new.write("l_english:\n")

# while True:
#     line = s.readline();
#     if not line:
#         break
#     elif "\"" in line:
#         if len(line.split(':')[0].split('_')) == 3:
#             language = line.split(':')[0].split('_')[2];
#         else: language = "POL";
#         if language == "CAL":
#             for tag in ['CAL','ALP','PRT']:
#                 s_new.write(' '+tag+'_'+line.split(':')[0].strip().replace('_'+language,'')+':'+line.split(':')[1])
#         elif language == "JOM":
#             for tag in ['JOM','JUT']:
#                 s_new.write(' '+tag+'_'+line.split(':')[0].strip().replace('_'+language,'')+':'+line.split(':')[1])
#         elif language == "PRU":
#             for tag in ['PRU','AES','GAL']:
#                 s_new.write(' '+tag+'_'+line.split(':')[0].strip().replace('_'+language,'')+':'+line.split(':')[1])
#         elif language == "KSZ":
#             for tag in ['KSZ','KSC']:
#                 s_new.write(' '+tag+'_'+line.split(':')[0].strip().replace('_'+language,'')+':'+line.split(':')[1])
#         elif language == "CZE":
#             s_new.write(' CZE_'+line.split(':')[0].strip().replace('_'+language,'')+':'+line.split(':')[1])
#         elif language == "GER":
#             for tag in ['GER', 'KAM', 'MNI', 'RAS', 'WRT', 
#                         'POM', 'KES', 'KOS', 'TEU', 'BRG', 
#                         'BRE', 'KLB', 'OST', 'WIZ', 'FRK',
#                         'VAN', 'SAX', 'EKS', 'EKW', 'TOU', 'BOG', 'LUB']:
#                 s_new.write(' '+tag+'_'+line.split(':')[0].strip().replace('_'+language,'')+':'+line.split(':')[1])
#         elif language == "UKROS":
#             for tag in ['UPA', 'KOZ', 'UHR', 'BEL', 'ROS', 'RUS', 'RMA', 'UKR', 'LEM']:
#                 s_new.write(' '+tag+'_'+line.split(':')[0].strip().replace('_'+language,'')+':'+line.split(':')[1])
#         elif language == "LEH":
#             for tag in ['LEH', 'LCH', 'WAN', 'JAS', 'SNF', 'BOR', 'STR']:
#                 s_new.write(' '+tag+'_'+line.split(':')[0].strip().replace('_'+language,'')+':'+line.split(':')[1])
#         elif language == "SIL":
#             for tag in [ 'CHO', 'GLI', 'FER', 'RUD', 'JSW', 'TRC', 'DUR', 'SBW', 'WYM']:
#                 s_new.write(' '+tag+'_'+line.split(':')[0].strip().replace('_'+language,'')+':'+line.split(':')[1])
#         elif language == "USP":
#             s_new.write(' USP_'+line.split(':')[0].strip().replace('_'+language,'')+':'+line.split(':')[1])
#         elif language == "POL":
#             s_new.write(' '+line.split(':')[0].strip().replace('_'+language,'')+':'+line.split(':')[1])
#         else:
#             s_new.write(' '+language+'_'+line.split(':')[0].strip().replace('_'+language,'')+':'+line.split(':')[1])

# s.close()
# s_new.close()




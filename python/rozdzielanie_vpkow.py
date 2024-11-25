import string;


vp = open("victory_points_l_english_new.yml","r",encoding="utf_8_sig",newline='\n')
vp_CAL = open("calisia_victory_points_l_english.yml","w",encoding="utf_8_sig",newline='\n')
vp_PRU = open("old_prussian_victory_points_l_english.yml","w",encoding="utf_8_sig",newline='\n')
vp_EK = open("EK_impostor_states_victory_points_l_english.yml","w",encoding="utf_8_sig",newline='\n')
vp_JOM = open("JOM_victory_points_l_english.yml","w",encoding="utf_8_sig",newline='\n')
vp_RAS = open("RAS_victory_points_l_english.yml","w",encoding="utf_8_sig",newline='\n')
vp_USP = open("USP_victory_points_l_english.yml","w",encoding="utf_8_sig",newline='\n')
vp_WYM = open("WYM_victory_points_l_english.yml","w",encoding="utf_8_sig",newline='\n')
vp_barbares = open("barbares_victory_points_l_english.yml","w",encoding="utf_8_sig",newline='\n')
vp_CZE = open("czechojapan_victory_points_l_english.yml","w",encoding="utf_8_sig",newline='\n')
vp_east_slav = open("east_slavic_victory_points_l_english.yml","w",encoding="utf_8_sig",newline='\n')
vp_german = open("german_victory_points_l_english.yml","w",encoding="utf_8_sig",newline='\n')
vp_kashubian = open("kashubian_victory_points_l_english.yml","w",encoding="utf_8_sig",newline='\n')
vp_lechitic = open("lechitic_victory_points_l_english.yml","w",encoding="utf_8_sig",newline='\n')
vp_silesian = open("silesian_victory_points_l_english.yml","w",encoding="utf_8_sig",newline='\n')
vp_TEU = open("tełtonik_victory_points_l_english.yml","w",encoding="utf_8_sig",newline='\n')
vp_default = open("victory_points_l_english.yml","w",encoding="utf_8_sig",newline='\n')
vp_barbares.write("l_english:\r\n")
vp_CAL.write("l_english:\r\n")
vp_PRU.write("l_english:\r\n")
vp_EK.write("l_english:\r\n")
vp_JOM.write("l_english:\r\n")
vp_RAS.write("l_english:\r\n")
vp_USP.write("l_english:\r\n")
vp_WYM.write("l_english:\r\n")
vp_CZE.write("l_english:\r\n")
vp_east_slav.write("l_english:\r\n")
vp_german.write("l_english:\r\n")
vp_kashubian.write("l_english:\r\n")
vp_lechitic.write("l_english:\r\n")
vp_silesian.write("l_english:\r\n")
vp_default.write("l_english:\r\n")
vp_TEU.write("l_english:\r\n")
CAL = []
PRT = []
ALP = []
GAL = []
PRU = []
GER = []
KAM = []
MNI = []
RAS = []
WRT = []
POM = []
KES = []
KOS = []
TEU = []
BRG = []
BRE = []
KLB = []
OST = []
WIZ = []
FRK = []
VAN = []
SAX = []
EKS = []
EKW = []
TOU = []
BOG = []
LUB = []
JOM = []
USP = []
WYM = []
JUT = []
AES = []
CZE = []
BEL = []
KOZ = []
LEM = []
ROS = []
RMA = []
RUS = []
UPA = []
UKR = []
UHR = []
KSZ = []
KSC = []
BOR = []
JAS = []
LEH = []
LCH = []
SNF = []
STR = []
WAN = []
CHO = []
DUR = []
FER = []
GLI = []
JSW = []
RUD = []
SBW = []
TRC = []
DEFAULT = []
while True:
    line = vp.readline()
    if not line:
        break
    elif "\"" in line:
        tag = line.split(':')[0].split('_')[0].strip()
        if len(tag) == 3:
            if tag == 'CAL':
                CAL.append(line)
            elif tag == 'PRT':
                PRT.append(line)
            elif tag == 'ALP':
                ALP.append(line)
            elif tag == 'GAL':
                GAL.append(line)
            elif tag == 'PRU':
                PRU.append(line)
            elif tag == 'BOG':
                BOG.append(line)
            elif tag == 'EKW':
                EKW.append(line)
            elif tag == 'EKS':
                EKS.append(line)
            elif tag == 'TOU':
                TOU.append(line)
            elif tag == 'JOM':
                JOM.append(line)
            elif tag == 'RAS':
                RAS.append(line)
            elif tag == 'USP':
                USP.append(line)
            elif tag == 'WYM':
                WYM.append(line)
            elif tag == 'WIZ':
                WIZ.append(line)
            elif tag == 'VAN':
                VAN.append(line)
            elif tag == 'SAX':
                SAX.append(line)
            elif tag == 'OST':
                OST.append(line)
            elif tag == 'JUT':
                JUT.append(line)
            elif tag == 'FRK':
                FRK.append(line)    
            elif tag == 'AES':
                AES.append(line)
            elif tag == 'CZE':
                CZE.append(line)
            elif tag == 'BEL':
                BEL.append(line)
            elif tag == 'KOZ':
                KOZ.append(line)
            elif tag == 'LEM':
                LEM.append(line)
            elif tag == 'ROS':
                ROS.append(line) 
            elif tag == 'RMA':
                RMA.append(line)
            elif tag == 'RUS':
                RUS.append(line) 
            elif tag == 'UPA':
                UPA.append(line) 
            elif tag == 'UKR':
                UKR.append(line)
            elif tag == 'UHR':
                UHR.append(line)
            elif tag == 'BRG':
                BRG.append(line)
            elif tag == 'BRE':
                BRE.append(line)
            elif tag == 'KOS':
                KOS.append(line)
            elif tag == 'KLB':
                KLB.append(line)
            elif tag == 'KES':
                KES.append(line)
            elif tag == 'KAM':
                KAM.append(line)
            elif tag == 'POM':
                POM.append(line)
            elif tag == 'WRT':
                WRT.append(line)
            elif tag == 'GER':
                GER.append(line)
            elif tag == 'MNI':
                MNI.append(line)
            elif tag == 'KSZ':
                KSZ.append(line)
            elif tag == 'KSC':
                KSC.append(line)
            elif tag == 'BOR':
                BOR.append(line)
            elif tag == 'JAS':
                JAS.append(line)
            elif tag == 'LEH':
                LEH.append(line)
            elif tag == 'LCH':
                LCH.append(line)
            elif tag == 'SNF':
                LCH.append(line)
            elif tag == 'STR':
                LCH.append(line)
            elif tag == 'WAN':
                WAN.append(line)
            elif tag == 'CHO':
                CHO.append(line)
            elif tag == 'DUR':
                DUR.append(line)
            elif tag == 'FER':
                FER.append(line)
            elif tag == 'GLI':
                GLI.append(line)
            elif tag == 'JSW':
                JSW.append(line)
            elif tag == 'RUD':
                RUD.append(line)
            elif tag == 'SBW':
                SBW.append(line)
            elif tag == 'TRC':
                TRC.append(line)
            elif tag == 'TEU':
                TEU.append(line)
            elif tag == 'LUB':
                LUB.append(line)
            else:
                DEFAULT.append(line)
        else:
            DEFAULT.append(line)
vp.close()
for a in [CAL,PRT,ALP]:
    for l in a:
        vp_CAL.write(l)
for a in [PRU,GAL]:
    for l in a:
        vp_PRU.write(l)
for a in [BOG,EKW,EKS,TOU]:
    for l in a:
        vp_EK.write(l)
for a in [WIZ,VAN,SAX,OST,JUT,FRK,AES]:
    for l in a:
        vp_barbares.write(l)
for a in [BEL,KOZ,LEM,ROS,RMA,RUS,UPA,UKR,UHR]:
    for l in a:
        vp_east_slav.write(l)
for a in [BRG,BRE,KOS,KLB,KES,KAM,POM,WRT,GER,MNI]:
    for l in a:
        vp_german.write(l)
for a in [KSZ,KSC]:
    for l in a:
        vp_german.write(l)
for a in [BOR,JAS,LEH,LCH,WAN]:
    for l in a:
        vp_lechitic.write(l)
for a in [CHO,DUR,FER,GLI,JSW,RUD,SBW,TRC]:
    for l in a:
        vp_silesian.write(l)
for a in [TEU,LUB]:
    for l in a:
        vp_TEU.write(l)

for l in JOM:
        vp_JOM.write(l)
for l in RAS:
        vp_RAS.write(l)
for l in RAS:
        vp_RAS.write(l)
for l in USP:
        vp_USP.write(l)
for l in WYM:
        vp_WYM.write(l)
for l in CZE:
        vp_CZE.write(l)
for l in DEFAULT:
        vp_default.write(l)


vp_CAL.close()
vp_PRU.close()
vp_EK.close()
vp_JOM.close()
vp_RAS.close()
vp_USP.close()
vp_WYM.close()
vp_barbares.close()
vp_east_slav.close()
vp_german.close()
vp_silesian.close()
vp_TEU.close()
vp_default.close()



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




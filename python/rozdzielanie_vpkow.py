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
CAL = {}
PRT = {}
ALP = {}
GAL = {}
PRU = {}
GER = {}
KAM = {}
MNI = {}
RAS = {}
WRT = {}
POM = {}
KES = {}
KOS = {}
TEU = {}
BRG = {}
BRE = {}
KLB = {}
OST = {}
WIZ = {}
FRK = {}
VAN = {}
SAX = {}
EKS = {}
EKW = {}
TOU = {}
BOG = {}
LUB = {}
JOM = {}
USP = {}
WYM = {}
JUT = {}
AES = {}
CZE = {}
BEL = {}
KOZ = {}
LEM = {}
ROS = {}
RMA = {}
RUS = {}
UPA = {}
UKR = {}
UHR = {}
KSZ = {}
KSC = {}
BOR = {}
JAS = {}
LEH = {}
LCH = {}
SNF = {}
STR = {}
WAN = {}
CHO = {}
DUR = {}
FER = {}
GLI = {}
JSW = {}
RUD = {}
SBW = {}
TRC = {}
DEFAULT = {}
while True:
    line = vp.readline()
    if not line:
        break
    elif "\"" in line:
        tag = line.split(':')[0].split('_')[0].strip()
        i = len(line.split(':')[0].split('_')) -1
        if len(tag) == 3:
            if tag == 'CAL':
                CAL.update({ '_'.join(line.split(':')[0].split('_')[3:]):line})
            elif tag == 'PRT':
                PRT.update({ '_'.join(line.split(':')[0].split('_')[3:]):line})
            elif tag == 'ALP':
                ALP.update({ '_'.join(line.split(':')[0].split('_')[3:]):line})
            elif tag == 'GAL':
                GAL.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'PRU':
                PRU.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'BOG':
                BOG.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'EKW':
                EKW.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'EKS':
                EKS.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'TOU':
                TOU.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'JOM':
                JOM.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'RAS':
                RAS.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'USP':
                USP.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'WYM':
                WYM.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'WIZ':
                WIZ.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'VAN':
                VAN.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'SAX':
                SAX.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'OST':
                OST.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'JUT':
                JUT.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'FRK':
                FRK.update({ int(line.split(':')[0].split('_')[3:][0]):line})    
            elif tag == 'AES':
                AES.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'CZE':
                CZE.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'BEL':
                BEL.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'KOZ':
                KOZ.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'LEM':
                LEM.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'ROS':
                ROS.update({ int(line.split(':')[0].split('_')[3:][0]):line}) 
            elif tag == 'RMA':
                RMA.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'RUS':
                RUS.update({ int(line.split(':')[0].split('_')[3:][0]):line}) 
            elif tag == 'UPA':
                UPA.update({ int(line.split(':')[0].split('_')[3:][0]):line}) 
            elif tag == 'UKR':
                UKR.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'UHR':
                UHR.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'BRG':
                BRG.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'BRE':
                BRE.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'KOS':
                KOS.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'KLB':
                KLB.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'KES':
                KES.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'KAM':
                KAM.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'POM':
                POM.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'WRT':
                WRT.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'GER':
                GER.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'MNI':
                MNI.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'KSZ':
                KSZ.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'KSC':
                KSC.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'BOR':
                BOR.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'JAS':
                JAS.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'LEH':
                LEH.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'LCH':
                LCH.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'SNF':
                LCH.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'STR':
                LCH.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'WAN':
                WAN.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'CHO':
                CHO.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'DUR':
                DUR.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'FER':
                FER.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'GLI':
                GLI.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'JSW':
                JSW.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'RUD':
                RUD.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'SBW':
                SBW.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'TRC':
                TRC.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'TEU':
                TEU.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            elif tag == 'LUB':
                LUB.update({ int(line.split(':')[0].split('_')[3:][0]):line})
            else:
                DEFAULT.update({ int(line.split(':')[0].split('_')[3:][0]):line})
        else:
            DEFAULT.update({ line.split(':')[0].split('_')[i]:line})
vp.close()
k = list(CAL.keys())
for aa in [PRT,ALP]:
    for x in list(aa.keys()):
        if x not in k:
            k.append(x)
k.sort()
for p in k:
    for a in [CAL,PRT,ALP]:
        if p in a:
            vp_CAL.write(a[p])
    vp_CAL.write("\r\n")
k = list(PRU.keys())
for x in list(GAL.keys()):
    if x not in k:
        k.append(x)
k.sort()
for p in k:
    for a in [PRU,GAL]:
        vp_PRU.write(a[p])
    vp_PRU.write("\r\n")
k = list(BOG.keys())
for aa in [EKW,EKS,TOU]:
    for x in list(aa.keys()):
        if x not in k:
            k.append(x)
k.sort()
for p in k:
    for a in [BOG,EKW,EKS,TOU]:
        vp_EK.write(a[p])
    vp_EK.write("\r\n")
k = list(WIZ.keys())
k.sort()
for aa in [VAN,SAX,OST,JUT,FRK,AES]:
    for x in list(aa.keys()):
        if x not in k:
            k.append(x)
k.sort()
for p in k:
    for a in [WIZ,VAN,SAX,OST,JUT,FRK,AES]:
        if p in a:
            vp_barbares.write(a[p])
    vp_barbares.write("\r\n")
k = list(BEL.keys())
for aa in [KOZ,LEM,ROS,RMA,RUS,UPA,UKR,UHR]:
    for x in list(aa.keys()):
        if x not in k:
            k.append(x)
k.sort()
for p in k:
    for a in [BEL,KOZ,LEM,ROS,RMA,RUS,UPA,UKR,UHR]:
        if p in a:
            vp_east_slav.write(a[p])
    vp_east_slav.write("\r\n")
k = list(BRG.keys())
for aa in [BRE,KOS,KLB,KES,KAM,POM,WRT,GER,MNI]:
    for x in list(aa.keys()):
        if x not in k:
            k.append(x)
k.sort()
for p in k:
    for a in [BRG,BRE,KOS,KLB,KES,KAM,POM,WRT,GER,MNI]:
        if p in a:
            vp_german.write(a[p])
    vp_german.write("\r\n")
k = list(KSZ.keys())
for x in list(KSC.keys()):
    if x not in k:
        k.append(x)
k.sort()
for p in k:
    for a in [KSZ,KSC]:
        if p in a:
            vp_kashubian.write(a[p])
k = list(BOR.keys())
for aa in [JAS,LEH,LCH,WAN]:
    for x in list(aa.keys()):
        if x not in k:
            k.append(x)
k.sort()
for p in k:
    for a in [BOR,JAS,LEH,LCH,WAN]:
        if p in a:
            vp_lechitic.write(a[p])
    vp_lechitic.write("\r\n")
k = list(CHO.keys())
for aa in [DUR,FER,GLI,JSW,RUD,SBW,TRC]:
    for x in list(aa.keys()):
        if x not in k:
            k.append(x)
k.sort()
for p in k:
    for a in [CHO,DUR,FER,GLI,JSW,RUD,SBW,TRC]:
        if p in a:
            vp_silesian.write(a[p])
    vp_silesian.write("\r\n")
k = list(TEU.keys())
for x in list(LUB.keys()):
    if x not in k:
        k.append(x)
k.sort()
for p in k:
    for a in [TEU,LUB]:
        if p in a:
            vp_TEU.write(a[p])
    vp_TEU.write("\r\n")
for aa in [JOM,RAS,USP,WYM,CZE,DEFAULT]:
    k = list(aa.keys())
    k.sort()
    for p in k:
        if aa == JOM:
            vp_JOM.write(aa[p])
        elif aa == RAS:
            vp_RAS.write(aa[p])
        elif aa == USP:
            vp_USP.write(aa[p])
        elif aa == WYM:
            vp_WYM.write(aa[p])
        elif aa == CZE:
            vp_CZE.write(aa[p])
        else:
            vp_default.write(aa[p])

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

for d in [CAL,PRT,ALP,GAL,PRU,
          GER,KAM,MNI,RAS,WRT,
          POM,KES,KOS,TEU,BRG,
          BRE,KLB,OST,WIZ,FRK,
          VAN,SAX,EKS,EKW,TOU,
          BOG,LUB,JOM,USP,WYM,
          JUT,AES,CZE,BEL,KOZ,
          LEM,ROS,RMA,RUS,UPA,
          UKR,UHR,KSZ,KSC,BOR,
          JAS,LEH,LCH,SNF,STR,
          WAN,CHO,DUR,FER,GLI,
          JSW,RUD,SBW,TRC,DEFAULT]:
    d.clear()

ATM = {}
s = open("state_names_l_english_new.yml","r",encoding="utf_8_sig",newline='\r\n')
s_CAL = open("calisia_states_l_english.yml","w",encoding="utf_8_sig",newline='\n')
s_PRU = open("old_prussian_states_l_english.yml","w",encoding="utf_8_sig",newline='\n')
s_EK = open("EK_impostor_states_states_l_english.yml","w",encoding="utf_8_sig",newline='\n')
s_JOM = open("JOM_states_l_english.yml","w",encoding="utf_8_sig",newline='\n')
s_RAS = open("RAS_states_l_english.yml","w",encoding="utf_8_sig",newline='\n')
s_USP = open("USP_states_l_english.yml","w",encoding="utf_8_sig",newline='\n')
s_WYM = open("WYM_states_l_english.yml","w",encoding="utf_8_sig",newline='\n')
s_barbares = open("barbares_states_l_english.yml","w",encoding="utf_8_sig",newline='\n')
s_CZE = open("czechojapan_states_l_english.yml","w",encoding="utf_8_sig",newline='\n')
s_east_slav = open("east_slavic_states_l_english.yml","w",encoding="utf_8_sig",newline='\n')
s_german = open("german_states_l_english.yml","w",encoding="utf_8_sig",newline='\n')
s_kashubian = open("kashubian_states_l_english.yml","w",encoding="utf_8_sig",newline='\n')
s_lechitic = open("lechitic_states_l_english.yml","w",encoding="utf_8_sig",newline='\n')
s_silesian = open("silesian_states_l_english.yml","w",encoding="utf_8_sig",newline='\n')
s_ATM = open("ATM_states_l_english.yml","w",encoding="utf_8_sig",newline='\n')
s_TEU = open("tełtonik_states_l_english.yml","w",encoding="utf_8_sig",newline='\n')
s_default = open("states_l_english.yml","w",encoding="utf_8_sig",newline='\n')
s_barbares.write("l_english:\r\n")
s_CAL.write("l_english:\r\n")
s_PRU.write("l_english:\r\n")
s_EK.write("l_english:\r\n")
s_JOM.write("l_english:\r\n")
s_RAS.write("l_english:\r\n")
s_USP.write("l_english:\r\n")
s_WYM.write("l_english:\r\n")
s_CZE.write("l_english:\r\n")
s_east_slav.write("l_english:\r\n")
s_german.write("l_english:\r\n")
s_kashubian.write("l_english:\r\n")
s_lechitic.write("l_english:\r\n")
s_silesian.write("l_english:\r\n")
s_default.write("l_english:\r\n")
s_TEU.write("l_english:\r\n")
s_ATM.write("l_english:\r\n")
while True:
    line = s.readline()
    if not line:
        break
    elif "\"" in line:
        tag = line.split(':')[0].split('_')[0].strip()
        i = len(line.split(':')[0].split('_')) -1
        if len(tag) == 3:
            if tag == 'CAL':
                CAL.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'PRT':
                PRT.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'ALP':
                ALP.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'GAL':
                GAL.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'PRU':
                PRU.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'BOG':
                BOG.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'EKW':
                EKW.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'EKS':
                EKS.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'TOU':
                TOU.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'JOM':
                JOM.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'RAS':
                RAS.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'USP':
                USP.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'WYM':
                WYM.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'WIZ':
                WIZ.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'VAN':
                VAN.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'SAX':
                SAX.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'OST':
                OST.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'JUT':
                JUT.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'FRK':
                FRK.update({ int(line.split(':')[0].split('_')[i]):line})    
            elif tag == 'AES':
                AES.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'CZE':
                CZE.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'BEL':
                BEL.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'KOZ':
                KOZ.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'LEM':
                LEM.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'ROS':
                ROS.update({ int(line.split(':')[0].split('_')[i]):line}) 
            elif tag == 'RMA':
                RMA.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'RUS':
                RUS.update({ int(line.split(':')[0].split('_')[i]):line}) 
            elif tag == 'UPA':
                UPA.update({ int(line.split(':')[0].split('_')[i]):line}) 
            elif tag == 'UKR':
                UKR.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'UHR':
                UHR.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'BRG':
                BRG.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'BRE':
                BRE.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'KOS':
                KOS.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'KLB':
                KLB.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'KES':
                KES.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'KAM':
                KAM.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'POM':
                POM.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'WRT':
                WRT.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'GER':
                GER.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'MNI':
                MNI.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'KSZ':
                KSZ.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'KSC':
                KSC.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'BOR':
                BOR.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'JAS':
                JAS.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'LEH':
                LEH.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'LCH':
                LCH.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'SNF':
                LCH.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'STR':
                LCH.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'WAN':
                WAN.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'CHO':
                CHO.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'DUR':
                DUR.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'FER':
                FER.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'GLI':
                GLI.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'JSW':
                JSW.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'RUD':
                RUD.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'SBW':
                SBW.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'TRC':
                TRC.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'TEU':
                TEU.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'LUB':
                LUB.update({ int(line.split(':')[0].split('_')[i]):line})
            elif tag == 'ATM':
                ATM.update({ int(line.split(':')[0].split('_')[i]):line})
            else:
                DEFAULT.update({ int(line.split(':')[0].split('_')[i]):line})
        else:
            DEFAULT.update({ int(line.split(':')[0].split('_')[i]):line})
s.close()

k = list(CAL.keys())
for aa in [PRT,ALP]:
    for x in list(aa.keys()):
        if x not in k:
            k.append(x)
k.sort()
for p in k:
    for a in [CAL,PRT,ALP]:
        if p in a:
            s_CAL.write(a[p])
    s_CAL.write("\r\n")
k = list(PRU.keys())
for x in list(GAL.keys()):
    if x not in k:
        k.append(x)
k.sort()
for p in k:
    for a in [PRU,GAL]:
        s_PRU.write(a[p])
    s_PRU.write("\r\n")
k = list(BOG.keys())
for aa in [EKW,EKS,TOU]:
    for x in list(aa.keys()):
        if x not in k:
            k.append(x)
k.sort()
for p in k:
    for a in [BOG,EKW,EKS,TOU]:
        s_EK.write(a[p])
    s_EK.write("\r\n")
k = list(WIZ.keys())
k.sort()
for aa in [VAN,SAX,OST,JUT,FRK,AES]:
    for x in list(aa.keys()):
        if x not in k:
            k.append(x)
k.sort()
for p in k:
    for a in [WIZ,VAN,SAX,OST,JUT,FRK,AES]:
        if p in a:
            s_barbares.write(a[p])
    s_barbares.write("\r\n")
k = list(BEL.keys())
for aa in [KOZ,LEM,ROS,RMA,RUS,UPA,UKR,UHR]:
    for x in list(aa.keys()):
        if x not in k:
            k.append(x)
k.sort()
for p in k:
    for a in [BEL,KOZ,LEM,ROS,RMA,RUS,UPA,UKR,UHR]:
        if p in a:
            s_east_slav.write(a[p])
    s_east_slav.write("\r\n")
k = list(BRG.keys())
for aa in [BRE,KOS,KLB,KES,KAM,POM,WRT,GER,MNI]:
    for x in list(aa.keys()):
        if x not in k:
            k.append(x)
k.sort()
for p in k:
    for a in [BRG,BRE,KOS,KLB,KES,KAM,POM,WRT,GER,MNI]:
        if p in a:
            s_german.write(a[p])
    s_german.write("\r\n")
k = list(KSZ.keys())
for x in list(KSC.keys()):
    if x not in k:
        k.append(x)
k.sort()
for p in k:
    for a in [KSZ,KSC]:
        if p in a:
            s_kashubian.write(a[p])
k = list(BOR.keys())
for aa in [JAS,LEH,LCH,WAN]:
    for x in list(aa.keys()):
        if x not in k:
            k.append(x)
k.sort()
for p in k:
    for a in [BOR,JAS,LEH,LCH,WAN]:
        if p in a:
            s_lechitic.write(a[p])
    s_lechitic.write("\r\n")
k = list(CHO.keys())
for aa in [DUR,FER,GLI,JSW,RUD,SBW,TRC]:
    for x in list(aa.keys()):
        if x not in k:
            k.append(x)
k.sort()
for p in k:
    for a in [CHO,DUR,FER,GLI,JSW,RUD,SBW,TRC]:
        if p in a:
            s_silesian.write(a[p])
    s_silesian.write("\r\n")
k = list(TEU.keys())
for x in list(LUB.keys()):
    if x not in k:
        k.append(x)
k.sort()
for p in k:
    for a in [TEU,LUB]:
        if p in a:
            s_TEU.write(a[p])
    s_TEU.write("\r\n")
for aa in [JOM,RAS,USP,WYM,CZE,ATM,DEFAULT]:
    k = list(aa.keys())
    k.sort()
    for p in k:
        if aa == JOM:
            s_JOM.write(aa[p])
        elif aa == RAS:
            s_RAS.write(aa[p])
        elif aa == USP:
            s_USP.write(aa[p])
        elif aa == WYM:
            s_WYM.write(aa[p])
        elif aa == CZE:
            s_CZE.write(aa[p])
        elif aa == ATM:
            s_ATM.write(aa[p])
        else:
            s_default.write(aa[p])

s_CAL.close()
s_PRU.close()
s_EK.close()
s_JOM.close()
s_RAS.close()
s_USP.close()
s_WYM.close()
s_barbares.close()
s_east_slav.close()
s_german.close()
s_silesian.close()
s_TEU.close()
s_default.close()



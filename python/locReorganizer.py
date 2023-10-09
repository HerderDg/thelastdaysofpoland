import glob,os,string;

vanillaPath = "C:/Gry/Steam/steamapps/common/Hearts of Iron IV/localisation/english/*.yml"
vanillaLocs = glob.glob(vanillaPath)
os.chdir("./localisation/english")
modPath = os.getcwd()+"/*.yml"
modLocs = glob.glob(modPath)



for file in vanillaLocs:
    vanillaKV = {}
    modKV = {}
    replaceOutput = ["l_english:"]
    modOutput = ["l_english:"]
    if os.path.basename(file) in ['countries_l_english.yml','victory_points_l_english.yml','state_names_l_english.yml','strategic_region_names_l_english.yml']:
        print("geo file, skippping")
    else:
        for modLocs in os.walk(os.getcwd()):
            if os.path.basename(file) not in modLocs[2]:
                print("File "+os.path.basename(file)+" not found, skipping")
            else:
                vanillaFileHandle =  open(file,"r",encoding="utf_8_sig",newline='\n')
                for i,line in enumerate(vanillaFileHandle):
                    if i!=0 and ':' in line:
                        vanillaKey = line.strip().split(':',1)[0]
                        vanillaValue = line.strip().split(':',1)[1].split("\"")[1:]
                        vanillaKV[vanillaKey] = ''.join(list(filter(None,vanillaValue))).replace('\\','"')
                vanillaFileHandle.close()
                modFileHandle =  open(os.getcwd()+'\\'+os.path.basename(file),"r",encoding="utf_8_sig",newline='\r\n')
                for i,line in enumerate(modFileHandle):
                    if i!=0 and ':' in line:
                        modKey = line.strip().split(':',1)[0]
                        modValue = line.strip().split(':',1)[1].split("\"")[1:]
                        modKV[modKey] = ''.join(list(filter(None,modValue))).replace('\\','"')
                modFileHandle.close()
                for key in vanillaKV:
                    if key in modKV:
                        if vanillaKV[key] != modKV[key]:
                            replaceOutput.append(' '+key+': '+'"'+modKV[key]+'"')
                for key in modKV:
                    if key not in vanillaKV and key[0] != '#':
                        modOutput.append(" "+key+': '+'"'+modKV[key]+'"')
                if not os.path.exists(os.getcwd()+"\\replace"):
                    os.makedirs(os.getcwd()+"\\replace")
                if len(modOutput) > 1:
                    modOutputFile = open("PaF_"+os.path.basename(file),"w",encoding="utf_8_sig")
                    for line in modOutput:
                        modOutputFile.write(line+'\n')
                    modOutputFile.close()
                if len(replaceOutput) > 1:
                    replaceOutputFile = open(os.getcwd()+"\\replace\\"+"replace_"+os.path.basename(file),"w",encoding="utf_8_sig")
                    for line in replaceOutput:
                        replaceOutputFile.write(line+'\n')
                    replaceOutputFile.close()
print("Done :)")
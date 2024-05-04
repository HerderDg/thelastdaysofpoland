import os;

os.chdir('./gfx/flags')
flagsDir = os.getcwd()
for root,dirs,files in os.walk(flagsDir):
    for name in files:
        if 'barbarian' in name:
            if 'JOM' in name:
                os.rename(os.path.join(root, name),os.path.join(root, "JUT.tga"))
            elif 'ECO' in name:
                os.rename(os.path.join(root, name),os.path.join(root, "WIZ.tga"))
            elif 'EKS' in name:
                os.rename(os.path.join(root, name),os.path.join(root, "SAX.tga"))
            elif 'EKW' in name:
                os.rename(os.path.join(root, name),os.path.join(root, "OST.tga"))
            elif 'ROS' in name:
                os.rename(os.path.join(root, name),os.path.join(root, "AES.tga"))
            elif 'KAM' in name:
                os.rename(os.path.join(root, name),os.path.join(root, "FRK.tga"))
            elif 'KON' in name:
                os.rename(os.path.join(root, name),os.path.join(root, "HNN.tga"))
            elif 'KOZ' in name:
                os.rename(os.path.join(root, name),os.path.join(root, "SCY.tga"))
        if 'slave_revolt' in name:
            os.rename(os.path.join(root, name),os.path.join(root, "SPA.tga"))




    


                

import os;

ideasFiles = []
ideas = []
hasCountryIdeas = False
bracketLayer = 0
os.chdir('./common/ideas')
ideasDir = os.getcwd()
for file in os.listdir(ideasDir):
    if file[:3] in ['JOM','EK_','EKS','KAM','ECO''WAN','ROS','KON','KOZ','SOS']:
        ideasFiles.append(open(file,"r",newline='\r\n'))
     
for ideaFileHandler in ideasFiles:
    hasCountryIdeas = False
    bracketLayer = 0
    while True:
        line = ideaFileHandler.readline()
        if not line:
            ideaFileHandler.close()
            break
        elif 'country' in line:
            hasCountryIdeas = True
        elif hasCountryIdeas:
            #print(line)
            if '{' in line and '}' not in line:
                bracketLayer+=1
                if bracketLayer==1:
                    ideas.append(line.split('=')[0].strip())
            elif '}' in line and '{' not in line:
                if bracketLayer>0:
                    bracketLayer-=1
                else:
                    hasCountryIdeas = False

hasCountryIdeas = False
skip = False
bracketLayer = 0
genericIdeaFile = open('PAF_generic_ideas.txt',"r",newline='\r\n')
while True:
    line = genericIdeaFile.readline()
    if not line:
        genericIdeaFile.close()
        break
    elif 'country' in line or 'hidden_ideas' in line:
        if 'observer_country' not in line:
            hasCountryIdeas = True
        else: skip = True
    elif hasCountryIdeas and not skip:
        if '{' in line and '}' not in line:
            bracketLayer+=1
            if bracketLayer==1:
                ideas.append(line.split('=')[0].strip())
        elif '}' in line and '{' not in line:
            if bracketLayer>0:
                bracketLayer-=1
            else:
                hasCountryIdeas = False

os.chdir('../../python')
effect =  open("strip.txt","w",newline='\r\n')
effect.write("barbarians_strip_ideas = {\n\t")
for idea in ideas:
    if idea != "barbarians_idea":
        effect.write('if = {\n\t\tlimit = {\n\t\t\thas_idea = '+idea+'\n\t\t}\n\t\tremove_ideas = '+idea+'\n\t}\n\t')
effect.write("}")
effect.close()



    


                

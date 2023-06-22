import string;

f = open("state_names_l_english.yml","r",encoding="utf_8_sig",newline='\r\n');
kashubianStates = [];
silesianStates = [];
prussianStates = [];
while True:
    line = f.readline();
    if not line:
        break
    elif line.split(':')[0].endswith('KSZ'):
        stateID = line.split(':')[0].split('_')[1];
        kashubianStates.append(stateID);
    elif line.split(':')[0].endswith('PRU'):
        stateID = line.split(':')[0].split('_')[1];
        prussianStates.append(stateID);
    elif line.split(':')[0].endswith('SIL'):
        stateID = line.split(':')[0].split('_')[1];
        silesianStates.append(stateID);
f.close();

for state in kashubianStates:
    print('state = '+state);
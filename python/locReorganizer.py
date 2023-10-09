import glob,string;

vanillaPath = "C:/Gry/Steam/steamapps/Hearts of Iron IV/localisation/*.yml"
vanillaLocs = glob.glob(vanillaPath)
print(vanillaLocs)

foo = "l_english:\r\n foo:0 \"foo\"\r\n bar:0 \"bar\"\r\n baz:0 \"baz\""
bar = "l_english:\r\n foo:\"foo\"\r\n bar: \"baz\"\r\n #baz: \"baz\"\r\n boo: \"\\\"boo\\\"\""

foo = foo.split("\r\n")
bar = bar.split("\r\n")
fooKV = {}
barKV = {}
for line in foo[1:]:
    fooKey = line.strip().split(':',1)[0]
    fooValue = line.strip().split(':',1)[1].split("\"")[1:]
    fooKV[fooKey] = ''.join(list(filter(None,fooValue))).replace('\\','"')
for line in bar[1:]:
    barKey = line.strip().split(':',1)[0]
    barValue = line.strip().split(':',1)[1].split("\"")[1:]
    barKV[barKey] = ''.join(list(filter(None,barValue))).replace('\\','"')
for key in fooKV:
    if key in barKV:
        if fooKV[key] != barKV[key]:
            print('replaced '+key+': '+barKV[key])
        else:
            print(key+': '+fooKV[key])
    else:
        print(key+': '+fooKV[key])
for key in barKV:
    if key not in fooKV and key[0] != '#':
            print('new '+key+': '+barKV[key])
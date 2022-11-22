charset = ['abc','code','band','band','abc']
wc={}

for key in charset:
    wc[key] = wc.get(key,0)+1
print(wc)
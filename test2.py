dictt={}
key = ['a','b','c','d']
for i in range(5,1,-1):
    dictt[i]=i

print(dictt)

print(dict(sorted(dictt.items(), key=lambda item: item[1],reverse=True)))
rev = dict(sorted(dictt.items(), key=lambda item: item[1],reverse=True))

for i in rev:
    print(i, rev[i])

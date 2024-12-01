import random
ls=[]
for i in range(1000):
    ls.append(random.randint(20,30))
d={}
for num in ls:
    d[num]=d.get(num,0)+1
l=list(d.items())
l.sort(key=lambda x:x[0],reverse=False)
for item in l:
    print(item[0],':',item[1])
genes=['RUNX2','WNT1','TP53','WDR34']
expression=[12.4,5.6,14.2,7.5]
d={}
for i in range(len(genes)):
    d[genes[i]]=expression[i]
ls=list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)
for item in ls:
    print(item[0])
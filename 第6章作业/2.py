f=open('test.txt','r').read()
string='python'+f+'python'
f=open('test.txt','w')
f.write(string)
f.close()
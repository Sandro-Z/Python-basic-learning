import os
for i in range(5):
	f=open(str(i),'w')
	f.write('')
	f.close()
for i in range(5):
	os.rename(str(i),str(i)+'python')
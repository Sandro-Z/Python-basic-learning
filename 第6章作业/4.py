import os
files=os.getcwd()
for file in os.listdir(files):
	if file.endswith('python'):
		os.rename(file,file[0]+'class')
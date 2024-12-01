a=input()
b=input()
b_splited=[]
if a not in b:
	print('字符串b中不存在子串a')
else:
	b_splited=b.split(a)
	a_count=b.count(a)
	#indexes=[i for i in range(len(b)) if b.startswith(a,i)]#str.startswith(sub_str,i)用于检测str索引为i的位置是不是sub_str
	indexes=[]
	for i in range(len(b)):
		if b.startswith(a,i):
			indexes.append(i)
	#该语句可以找出全部子串的位置
	if a_count==1:print('子串a在b中出现了1次，其索引值为{}'.format(b.index(a)))
	else:
		print('子串a在b中出现了{0}次，索引值分别为'.format(a_count),end='')
		for i in range(len(indexes)-2):
			print(indexes[i],end=',')
		print(indexes[-2],end='')
		print('和{}'.format(indexes[-1]))
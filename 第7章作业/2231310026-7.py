#生物强基2301张海阳 第7章
class Person:
	def __init__(self, name:str, age):
		self.name = name
		self.age = age
	def get_name(self):
		return self.name
	def get_age(self):
		return self.age
man=Person('Kobe',42)
jntm=Person('CaiXuKun',26)
print(man.get_name())
print(jntm.get_name())
class Student(Person):
	def __init__(self, name, age, score:list):
		super().__init__(name, age)
		self.score:list = score
	def get_maxscore(self):
		return max(self.score)

s1=Student('Xiaoming',19,[95,65,96])
print(s1.get_name())
print(s1.get_age())
print(s1.get_maxscore())
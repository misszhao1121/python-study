class Person(object):
	"""人的类 Person"""
	def __init__(self, name):
		super(Person, self).__init__()
		self.name = name
		self.ak47l = None
		self.hp = 100
	def Actizd(self,Djia_temp,zidan_temp):
		"""把子弹装到弹夹中"""
		Djia_temp.save(zidan_temp)
	def ADjia(self,AK47_temp,Djia_temp):
		"""把弹夹安装在枪中"""	
		AK47_temp.save(Djia_temp)
	
	def get(self,ak47_temp):
		self.ak47l = ak47_temp

	def kill(self,D_person_temp):
		#开火
		self.ak47l.fire(D_person_temp)

	def diaoxue(self,max_gls_temp):
		self.hp -=max_gls_temp

	def __str__(self):
		if self.ak47l:
			return "%s有血量%d，他有%s"%(self.name,self.hp,self.ak47l)
		else:
			if self.hp>0:
				return "%s有血量%d，他没有枪"%(self.name,self.hp)
			else:
				return "%s已死亡，请重新开始"%self.name

class Gun(object):
	"""docstring for Gun"""
	def __init__(self, name):
		super(Gun, self).__init__()
		self.name = name#用来记录枪的类型
		self.danjia = None#用来记录枪的类型

	def save(self,Djia_temp):
		self.danjia = Djia_temp

	def fire(self,D_person_temp):
		tanchuzd = self.danjia.tanchu()
		if tanchuzd:
        	        tanchuzd.sheji(D_person_temp)
		else:
        	        print("弹夹没有子弹了")

	def __str__(self):
		if self.danjia != None:
			return "这把枪是%s,%s"%(self.name,self.danjia)	
		else:
			return "这把枪是%s"%self.name

class Dj(object):
	"""docstring for Dj"""
	def __init__(self, max_num):
		super(Dj, self).__init__()
		self.max_num = max_num#用来记录弹夹最大容量
		self.zidan_list = [] #所有的子弹

	def save(self,zidan_temp):
		"""将这个子弹保存"""
		self.zidan_list.append(zidan_temp)

	def tanchu(self):
		if self.zidan_list:
			return self.zidan_list.pop()
		else:
			return None

	def __str__(self):
		return "弹夹信息为：%d/%d"%(len(self.zidan_list),self.max_num)
class zi_dan(object):
		"""docstring for zi_dan"""
		def __init__(self, max_gls):
			super(zi_dan, self).__init__()
			self.max_gls = max_gls#用来记录子弹造成伤害

		def sheji(self,D_person_temp):
			"""打中敌人"""
			D_person_temp.diaoxue(self.max_gls)

class Dperson(object):
		"""docstring for Dperson"""
		def __init__(self, arg):
			super(Dperson, self).__init__()
			self.arg = arg
				
def main():

	#1.创建一个人对像
	laowang = Person("老王")

	#2.创建一个枪对象
	ak47 = Gun("AK47")

	#3.创建一个弹夹对象
	Djia = Dj(20)

	#4.创建一个子弹
	for x in range(15):
		zidan = zi_dan(10)
	#6.老王装子弹
		laowang.Actizd(Djia,zidan)
	#7.老王装弹夹
	laowang.ADjia(ak47,Djia)
	#test枪信息
	#print(ak47)
	#test弹夹信
	#print(Djia)


	#8.老王拿枪
	laowang.get(ak47)
	print(laowang)	
	#5.创建一个敌人
	D_person = Person("隔壁老王")
	print(D_person)
	#9.老王开枪
	while D_person.hp >0:
		laowang.kill(D_person)
		print(D_person)
		print(laowang)
	else:
		print("射击结束")

if __name__ =='__main__':
	main()

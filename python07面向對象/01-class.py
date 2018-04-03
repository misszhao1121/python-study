class Test:
    #屬性
    #cat = 0
    #dog = 0
    
    
    #方法必須有參數
    def eat(self):
        print("吃魚")

    def drink(self):
        print("正在喝水")

    def printl(self):
        print("%s的年齡是:%d"%(self.name,self.age))
        #self誰調用就是誰
#創建一個對象
Tom = Test()
#Tom.printl()

Tom.eat()
#給Tom定義兩個屬性
Tom.name ="湯姆"
Tom.age = 40

#獲取屬性的第一種方式
#print("%s的年齡是:%d"%(Tom.name,Tom.age))
Tom.printl()


lanmao = Test()
lanmao.name = "藍貓"
lanmao.age =15
lanmao.printl()   #相當於lanmao.printl(lanmao)





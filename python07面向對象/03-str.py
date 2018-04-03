class Test:
    #屬性
    #cat = 0
    #dog = 0
    #初始化對像
    def __init__(self,n_name,n_age):
       self.name = n_name
       self.age = n_age
    
    def __str__(self):
        return "%s的年齡是%d"%(self.name,self.age)
    #方法必須有參數
    def eat(self):
        print("吃魚")

    def drink(self):
        print("正在喝水")

    def printl(self):
        print("%s的年齡是:%d"%(self.name,self.age))
        #self誰調用就是誰

#創建一個對象
Tom = Test("湯姆",40)


lanmao = Test("藍貓",15)



print(Tom)
print(lanmao)

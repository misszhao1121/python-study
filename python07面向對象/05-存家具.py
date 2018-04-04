class home:
    def __init__(self,price,info,addr):
        self.price = price
        self.info = info
        self.addr =addr
        self.left_info = info
        self.continer_item = []  
    
    def __str__(self):
        msg =  "你的房間面積%d剩餘面積%d房間在%s價值%d"%(self.info,self.left_info,self.addr,self.price)
        msg += "當前房子裏的物品有%s"%(str(self.continer_item))
        return msg

    def addbad(self,item):
        #item是對badroom的指向
        self.left_info-=item.getpice()
        self.continer_item.append(item.getarea()) 

    
class badroom:
    def __init__(self,area,pice):
        self.area = area
        self.pice = pice

    #def __str__(self):
    #  return "%s佔用面積是%d"%(self.area,self.pice)

    def getarea(self):
        return self.area
        #返回牀名字    
    def getpice(self):
        return self.pice
        #返回牀大小

T = home(123,333,"柏樹")
print(T)

B = badroom("name",20)
T.addbad(B)
print(T)

B1 = badroom("冰牀",50)
T.addbad(B1)
print(T)






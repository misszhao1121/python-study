class Potato:


    def __init__(self):
        self.cookString ="生的"
        self.cookedLevel =0
        self.condiments =[]

    def __str__(self):
        msg = self.cookString+"地瓜"
        if len(self.condiments) > 0:
            msg = msg +"("
            for temp in self.condiments:
                msg = msg + temp + ","
            msg = msg.strip(",") 

            msg = msg+ "味道的)"
        return msg
    def addcondiments(self,condiment):
        self.condiments.append(condiment)

    def cook(self,time):
        self.cookedLevel+=time
        if self.cookedLevel < 3:
            self.cookString = "生的"
        elif self.cookedLevel < 5:
            self.cookString = "半生不熟"

        elif self.cookedLevel < 8:
            self.cookString = "烤好了"
        else:
            self.cookString = "烤成灰了"



            
T = Potato()
print(T.cookedLevel)
print(T.cookString)
print(T.condiments)

print("----開始----")
A = int(input("請輸入你要掃考的時間"))
B = input("請輸入天價什麼調料")
T.cook(A)
T.addcondiments(B)
print(T)






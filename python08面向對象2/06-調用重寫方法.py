class animal:
    def eat(self):
        print("1")
class cat:
    def catal(self):
        print("貓池")
class scat(cat):#繼承
    #重寫
    def cata(self):
        print("小貓")
        #super().cata()
        cat.catal(self)

an = animal()
cat = cat()
scat = scat()


#scat.eat()
scat.cata()

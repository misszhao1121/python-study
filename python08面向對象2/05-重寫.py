class animal:
    def eat(self):
        print("1")
class cat(animal):
    def cata(self):
        print("貓池")
class scat(cat):#繼承
    #重寫
    def cata(self):
        print("小貓")



an = animal()
cat = cat()
scat = scat()


scat.eat()
scat.cata()

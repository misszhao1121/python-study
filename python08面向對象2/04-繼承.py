class animal:

    def eat(slef):
        print("吃")
    def drink(self):
        print("喝")
    def la(self):
        print("啦")
    def sa(self):
        print("撒")
class dog(animal):
 
    """def eat(slef):
        print("吃")
    def drink(self):
        print("喝")
    def la(self):
        print("啦")
    def sa(self):
        print("撒")"""
    def breakl(self):
        print("旺旺")
class cat(animal):
    def catch(self):
        print("老鼠")
class xiaotq(dog):
    def speak(self):
        print("fly")
dy = animal()
dg = dog()
dy.eat()
dg.eat()
dc = cat()
dc.eat()
dc.catch()
#可向上繼承所有類,多次繼承
xiaotq = xiaotq()
xiaotq.speak()
xiaotq.breakl()
xiaotq.eat()

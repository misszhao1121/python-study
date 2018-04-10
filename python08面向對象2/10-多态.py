class Dog(object):
    def print_self(self):
        print("我是谁谁谁,x")

class Xiaotq(Dog):
    def print_self(self):
        print("hello erverbody,f")

def introduce(dog1):
    dog1.print_self()
   # dog2.print_self()


dog1 = Dog()
dog2 = Xiaotq()

introduce(dog1)
introduce(dog2)
        

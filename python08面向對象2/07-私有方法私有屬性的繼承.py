class A:
    def __init__(self):
        self.n1 =100
        self.__n2 =200
    
    def test1(self):
        print("-*20")
    
    def __test2(self):
        print("**20")

    def test3(self):
        self.__test2

class B(A):
    def test4(self):
        #self.__test2()
        #print(self.__n2)

b = B()
b.test1()
#b.__test2() 私有方法沒有被繼承
print(b.n1)
#print(b.__n2) 私有屬性也不會被繼承
b.test3()
b.test4()



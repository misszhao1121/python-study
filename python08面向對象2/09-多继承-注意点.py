class Base(object):  #新式類
    #不寫就是經典類
    def test(self):
        print("----Base")

class A(Base):
    def test(self):
        print("test1")
class B(Base):
    def test(self):
        print("test2")
class C(A,B):   #多繼承
    pass


c = C()
c.test()
print(C.__mro__)#打印一个类的调用顺序

#全局變量
def test1():
    print("a=%d"%a)
    #全局變量在函數調用之前定義在函數裏面都可以使用.

def test2():
    print("a=%d"%a)


a = 100
test1()
test2()

def test1():
    a = 100

def test2():
    print("a=%d"%a)

test1()
#test2() 調用次函數會報錯，因爲a是局部變量沒有定義


print("a=%d"%a)#報錯，因爲a定義在test1函數裏面,只能在函數李敏使用，在函數外面使用就是未定義的函數.



def test(a,b,func):
    result = func(a,b)
    return result

func_new = input("請輸入一個匿名函數:")
func_new = eval(func_new)

num = test(11,22,func_new)

print(num)

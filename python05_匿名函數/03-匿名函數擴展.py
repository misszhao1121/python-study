def test(a,b,func):
    result =func(a,b)
    return result


num = test(111,22,lambda x,y:x+y)
print(num)

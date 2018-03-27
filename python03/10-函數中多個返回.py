def test():
    a = 11
    b = 22
    c = 33
   #n = [a,b,c]
   #return [a,b,c]
   #return a,b,c#相當於封裝成一個元祖
    return {"a":a,"b":b,"c":c}
num =test()
print(num)

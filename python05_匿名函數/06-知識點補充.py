#a =100 
a = [100]
def test(num):
    #num+=num
    #num+=num  直接修改num指向的值

    num = num + num
    #只是將num計算出來，然後賦值
    print(num)

#可變數據類型---列表，字典
test(a)


print(a)

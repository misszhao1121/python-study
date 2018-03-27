def Tnum(a,b,c):
    num = a+b+c
    #print("%d+%d+%d=%d"%(a,b,c,num))
    return num
def avg(a,b,c):
    result = Tnum(a,b,c)/3
    print("平均值是:%d"%result)
#Tnum(a,b,c)
a = int(input("請輸入第一個數"))
b = int(input("請輸入第二個數"))
c = int(input("請輸入第三個數"))
avg(a,b,c)



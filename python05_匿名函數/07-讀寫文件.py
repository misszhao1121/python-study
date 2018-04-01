def readfile():   
    f=open("test1.py","r")
    print(f.read())
    f.close
def writefile():

    f=open("test1.py","a+")
    a = input("請輸入你要寫入文件的話")
    f.write(a)
    print(f.read())


while True:
    a = int(input("你你想要打開文件還是寫文件"))
    if a == 1:
        readfile()
    elif a == 2:
        writefile()
    else:
        break


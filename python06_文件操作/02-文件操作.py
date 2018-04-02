import os
#更改文件名
#os.rename("01-文件復制_附件.py","02-文件復制_附件.py")
#刪除文件
#os.remove("01-文件復制_附件.py")
#獲取目錄
#os.listdir

dirl = input("請輸入你要重命名的文件目錄")

dirlist = os.listdir(dirl)
n = 0
for dl in dirlist:
    i = str(n)
    dirlista = input("請輸入第"+i+"個的新文件名")
    os.chdir(dirl)
    os.rename(dl,dirlista)
    n+=1    
print(os.listdir(dirl))




def copy():
    copyfile = input("請輸入你要膚質的文件名")
    f = open(copyfile,"r")
    strl = f.read()
    l = open("附件_"+copyfile,"w+")
    l.write(strl)
    print("復制文件結束")
    f.close()
    l.close()



copy()

def copy():
    copyfile = input("請輸入你要膚質的文件名")
    f = open(copyfile,"r")
    #從後往前找到文件名後綴名之前的下標
    position = copyfile.rfind(".")
    new_file =  copyfile[:position]+"_附件"+copyfile[position:]
    while True:
        strl = f.read(1024)
        if len(strl) == 0:
            break
        l = open(new_file,"w+")
        l.write(strl)
    print("復制文件結束")
    f.close()
    l.close()

copy()

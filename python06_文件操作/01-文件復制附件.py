def copy():
    copyfile = input("請輸入你要膚質的文件名")
    f = open(copyfile,"r")
    strl = f.read()

    position = copyfile.rfind(".")
    new_file =  copyfile[:position]+"附件"+copyfile[position:]
    l = open(new_file,"w+")
    l.write(strl)
    print("復制文件結束")
    f.close()
    l.close()



copy()

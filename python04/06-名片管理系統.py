#名片管理系
card = []
def print_menu():   
    print("#"*50)
    print("1:添加一個名片")
    print("2:刪除一個名片")
    print("3:修改一個名片")
    print("4:查詢一個名片")
    print("#"*50)
#添加名片函數

def add_card():
    """
    這是用來添加信息的
    """
    print("請輸入你要添加的名片")
    name = input("請輸入名字:")
    age = input("請輸入年齡:")
    sex = input("請輸入性別:")
    like = input("請輸入愛好:")
    dictl ={}
    dictl["name"] = name
    dictl["age"] = age
    dictl["sex"] = sex
    dictl["like"] = like
    global card
    card.append(dictl)
    print("恭喜您,添加成功！！")
    print("%s\t%s\t%s\t%s"%(dictl["name"],dictl["age"],dictl["sex"],dictl["like"]))
    print(card)
#刪除名片函數

def del_card():
    """
    着使用來完成刪除功能的
    """
    dictl={}
    print("請輸入你要刪除的名片")
    name = input("請輸入名字:")
    age = input("請輸入年齡:")
    sex = input("請輸入性別:")
    like = input("請輸入愛好:")
    dictl["name"] = name
    dictl["age"] = age
    dictl["sex"] = sex
    dictl["like"] = like
    if dictl in card: 
         card.remove(dictl)
         print("恭喜你，刪除成功")
         print("%s\t%s\t%s\t%s"%(dictl["name"],dictl["age"],dictl["sex"],dictl["like"]))
         print("#"*50)
         print(card)
#修改和查詢函數
def gdit_select(): 
         temp={}
         print("請輸入你要查詢的名片1")
         if list == 3:
            print("請輸入你要查詢的名片")
         if list ==4:
             print("請輸入要修改的名字")
         name = input("請輸入名字:")
         age = input("請輸入年齡:")
         sex = input("請輸入性別:")
         like = input("請輸入愛好:")
         temp["name"] = name
         temp["age"] = age
         temp["sex"] = sex
         temp["like"] = like
         n=0
         for templ in card:
             find_plag = 0
             if list==3:
                 if  templ == temp: 
                    print("#"*50)
                    print("恭喜您，找到了")
                    print(templ)
                    find_plag = 1
                    break
                 else:
                    print("查無此人")     
            #continue
             if list == 4: 
                 gdit={}
                 if templ == temp:
                    print("111")
                    name = input("請輸入你要修改成：")
                    age = input("年齡：")
                    sex = input("性別：")
                    like = input("愛好：")
                    gdit["name"] = name
                    gdit["age"] = age
                    gdit["sex"] = sex
                    gdit["like"]= like
                    card[n]=gdit
                    print("#"*50)
                    print("修改成功")
                    print(card)
                   # print(n)
                # print(n)
                 n+=1
                # print(n)
                # else:
                    # print("並沒有這個人")
                   #  continue
             continue       
#1.打印功能提示

def main():
    """封裝主函數"""
    print_menu()

    while True:
        global list
        list = int(input("請輸入你的選擇："))
        if list == 1:
             add_card()
        elif list == 2:
             del_card()
        elif list == 3 or list == 4:
             gdit_select()
        elif list == 5:
             print("退出系統")
             break
        else:
             print("您輸入的東西錯誤")
        continue

main()

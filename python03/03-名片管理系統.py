#名片管理系
print("#"*50)
print("1:添加一個名片")
print("2:刪除一個名片")
print("3:修改一個名片")
print("4:查詢一個名片")
print("#"*50)
card = []
while True:
    list = int(input("請輸入你的選擇："))
    dictl = {}
    if list == 1:
         print("請輸入你要添加的名片")
         name = input("請輸入名字:")
         age = input("請輸入年齡:")
         sex = input("請輸入性別:")
         like = input("請輸入愛好:")
         dictl["name"] = name
         dictl["age"] = age
         dictl["sex"] = sex
         dictl["like"] = like
         card.append(dictl)
         print("恭喜您,添加成功！！")
         print("%s\t%s\t%s\t%s"%(dictl["name"],dictl["age"],dictl["sex"],dictl["like"]))
         print(card)
         continue
    elif list == 2:
         print("請輸入你要刪除的名片")
         name = input("請輸入名字:")
         age = input("請輸入年齡:")
         sex = input("請輸入性別:")
         like = input("請輸入愛好:")
         dictl["name"] = name
         dictl["age"] = age
         dictl["sex"] = sex
         dictl["like"] = like
         for dictl in card: 
             card.remove(dictl)
             print("恭喜你，刪除成功")
             print("%s\t%s\t%s\t%s"%(dictl["name"],dictl["age"],dictl["sex"],dictl["like"]))
             print("#"*50)
             print(card)
         continue        
    elif list == 3 or list == 4:
         temp={}
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
         for templ in card:
             n = 0
             if list==3:
                 if  templ["name"] == temp["name"]: 
                    print("#"*50)
                    print("恭喜您，找到了")
                    print(templ)
                    continue
                 continue
             if list == 4: 
                 if temp == templ:
                    gdit={}
                    name = input("請輸入你要修改成：")
                    age = input("年齡：")
                    sex = input("性別：")
                    like = input("愛好：")
                    gdit["name"] = name
                    gdit["age"] = age
                    gdit["sex"] = sex
                    gdit["like"]=like
                    card[n] = gdit
                    n+=1
                    print("#")
                    print("修改成功")
                    print(card)
                    continue
             continue

    elif list == 5:
         print("退出系統")
         break
    else:
         print("您輸入的東西錯誤")
    continue

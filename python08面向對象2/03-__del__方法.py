class dog:
    
    #當對象沒有人引用是，會自動調用這個函數
    def __del__(self):
        print("--------英雄over------")

dog1 = dog()
dog2 = dog1


del dog1
del dog2
print("--------------------")

class Dog:

    #私有屬性
    # __var = 5
    #私有方法
    def __send_msg(self):
        print("------正在發送短信-----")
        
    
    def send_msg(self,new_money):
        if new_money > 1000:
            self.__send_msg()
        else:
            print("------餘額不足，請充值-------")

dog =Dog()
dog.send_msg(100)


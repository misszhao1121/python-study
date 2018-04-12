i = []
class CarStore(object):
    def order(self,money,listl):
        if money>5000:
            return Car(listl)

def inputl():
    global i
    i.append(buy_car())
    print(i)
    return i


class Car(object):
    def __init__(self,listl):
        self.list = listl
  #  def print(self,listl):
  #       self.list = listl
  #      return self.list
    def move(self):
        print(self.list+"车在行走")
    
    def music(self):
        print(self.list+"放音乐")

    def stop(self):
        print(self.list+"车停下来了")

def car_num():
    inputl()
    print("当前商店有这么多车"+inputl())
def buy_car():
    buy = input("请输入你想买的车")
    return buy

while True:
    flag = input("是否要买新车")
    if flag == "是":
        buy_car()
    else:
        break
    
while True:
    car_num()
    car_store = CarStore()
    listl = buy_car()
    car = car_store.order(50000,listl)
    car.move()
    car.music()
    car.stop()


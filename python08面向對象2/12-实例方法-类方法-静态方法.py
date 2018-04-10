class game(object):
    #类属性
    num =0


    #实例方法
    def __int__(self):
        #实例属性
        self.name = "laowang"
    #类方法
    @classmethod #固定的装饰器
    def add_num(cls):
        cls.num =100
    @staticmethod #静态方法
    def print_mean():
        print("-"*50)
        print("穿越火线v1.1")
        print("-"*50)

Game =game()
#game.add_num()
Game.add_num()
print(game.num)

#Game.print_mean() #通过类直接调用
game.print_mean() #通过实例对象，去掉用静态方法

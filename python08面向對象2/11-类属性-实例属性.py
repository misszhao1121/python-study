class Tool(object):
    #类对象
    num=0#类属性

    #方法
    def __init__(self,new_name):
        self.name = new_name
        Tool.num +=1
        


tool1=Tool("铁锹")#实例对象  实例属性


#实例属性和某个具体的实例对象式关联的，实例对象之间部供销
#；类属性属于类对象，可以在多个实例之间共享
tool2 = Tool("22")
tool2 = Tool("333")

print(Tool.num)

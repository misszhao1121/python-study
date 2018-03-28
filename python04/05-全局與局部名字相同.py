a =100
def test1():
    a=200#要想更改全局變臉得值需要global a
    print("a=%d"%a)

def test2():
    print("a=%d"%a)

test1()
test2()

#施行加函數
def add(*c,**kwargs):
    result = 0
    for i in c:
        result = result+i
    for l in kwargs.values():
        resutl = result +l
    print(result)
    return result

add(11,22,33,44,55,task=66,done=77)

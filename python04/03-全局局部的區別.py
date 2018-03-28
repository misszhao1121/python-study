"""
def get_wendu():
    wendu =33
    return wendu
def print_wendu(a):#定義一個形參
    print("wendu=%d"%a)


wendul = get_wendu()
print_wendu(wendul)
"""
wendu =0
def get_wendu():
    
  global  wendu
  wendu =33 
  #在函數中對全局變量進行修改，需要通過global聲明全局變量，告訴python解析器，這是一個全局變量。

def print_wendu():
    print("wendu=%d"%wendu)


get_wendu()
print_wendu()

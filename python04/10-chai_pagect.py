#不可便類型
#元祖 字符串 整型
"""
列表，字典可變
遞歸調用
"""
#4! = 4*3*2*1

def multiply(num):
    if num > 1:
        return num * multiply(num-1)
    else:
        return num
    #continue    
def main():
    numl = int(input("請輸入你要計算的階乘"))
    
    num =  multiply(numl)
    print(num)
main()


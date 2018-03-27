#函數返回值
def get_wendu():
    wendu = 22
    print("當前的溫度死:%d"%wendu)
    return wendu

def get_huashi_wendu(wendiu):
    wendu = wendu +3
    print("當前的溫度是:%d"%wendu)

get_huashi_wendu(get_wendu())


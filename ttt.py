import os
if __name__ == '__main__':
    return1 = os.system('ping 8.8.8.8 -c 2')
    # return1=os.system('ping 192.168.88.1 -c 2')
    while return1:
        print('ping fail')
        os.system('wget --post-data "username=MF1733058&&password=tan15237679619" http://p.nju.edu.cn/portal_io/login')
    else:
        print('ping ok')
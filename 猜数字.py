# -*- coding: utf-8 -*-

import random
a=random.randint(1,100)
n=input('请输入数字')
if n.isdigit():
    n=int(n)
    if n==a:
        print('猜对了')
    elif n>a:
        print('大了')
    else:
        print('小了')
    print('这个数是:',a)
else:
    print('你输入的不是数字')

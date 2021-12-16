#!/Users/genisshou/opt/anaconda3/bin/python
# -*- coding: utf-8 -*-

import sys
import time

recieve = ''
print('no...')
for n in range(100):
    recieve = sys.stdin.readline()
    print('no...')
    if recieve == 'qqq':
        f = open('test.txt', 'x')
        print(recieve)
    else:
        print('no...')

    # time.sleep(1)
    print(n)
# recieve = recieve + "OK!"

# print('Content-type: text/html\n')
# print(recieve)
#!/Users/genisshou/opt/anaconda3/bin/python
# -*- coding: utf-8 -*-

import sys

recieve = sys.stdin.readline()
recieve = recieve + "OK!"

print('Content-type: text/html\n')
print(recieve)
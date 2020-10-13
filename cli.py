#coding:utf-8

import mmap
import contextlib
import time

while True:
    with contextlib.closing(mmap.mmap(-1, 1024, tagname='test', access=mmap.ACCESS_READ)) as m:
        s = m.read(1024).replace('\x00', '')
        print (s)
    time.sleep(1)
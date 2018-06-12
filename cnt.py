#!/usr/bin/python3
import string
arq = open('enp3s0' , 'r+')
for i in arq.readlines():
    print (i)
    string.replace(i ,'enp3s0' , 'eth0')
    print (i)
    arq.close
    
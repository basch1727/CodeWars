"""
Created on Sun Aug 27 23:53:51 2017

@author: Dmitry White
"""

# TODO: A stream of data is received and needs to be reversed.
# Each segment is 8 bits meaning the order of these segments need to be reversed:
# 11111111 00000000 00001111 10101010
# (byte1) (byte2) (byte3) (byte4)
# 10101010 00001111 00000000 11111111
# (byte4) (byte3) (byte2) (byte1)
# Total number of bits will always be a multiple of 8. The data is given in an array as such:
# [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]


def data_reverse(data):
    l = len(data)
    data_new = []
    start = 0
    end = l
    for x in range(l, -1, -8):
        start = x
        if start != end:
            [data_new.append(item) for item in data[start:end]]
        end = x
    return data_new


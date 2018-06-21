# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 19:59:49 2018

@author: vamshi
"""

def rollingmean(Input,window):
    result = []
    flag =len(Input)-window+1
    for i in range(len(Input)):
        if i < flag:
            result.append(int(sum(Input[i:i+window])/window))
    return result
window=4
Input=[3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
print(rollingmean(Input,window))
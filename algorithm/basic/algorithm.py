#-*- coding:UTF-8 -*-
"""
"""
#@filename: algorithm
#@author: liuxh
#@date: 2018/9/11 9:24

def ysfh(n,k,m):
    people = list(range(1,n+1))

    i = k -1
    for nums in range(n):
        count = 0
        while count < m:
            if count < m and people[i] != 0:
                count += 1
            if count == m:
                print(people[i],",")
                people[i] = 0
            i = (i+1)%n

    return

a = ysfh(10,2,7)

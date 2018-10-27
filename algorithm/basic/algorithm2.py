#-*- coding:UTF-8 -*-
"""
"""
#@filename: algorithm2
#@author: liuxh
#@date: 2018/9/11 10:08


# def ysef(n,k,m):
#     people = list(range(1,n+1))
#
#     i= k -1
#     for num in range(n):
#         count = 0
#         while count < m:
#             if count < m:
#                 count += 1
#             if count == m:
#                 print(people[i])
#                 people.pop(i)
#             i = (i+1)%len(people)
#
#     return
#
# ysef(10,2,7)



a = [x + 1 for x in range(10)]  # 人数为10人，编号1~10
index, step = 1, 7    # 数到3的人出列。多谢华水小书童指正错误~
while len(a) > 1:
    index = (index + step - 1) % len(a)
    print('kill No. ', a[index])
    del a[index]
print('Winner is:', a[0])







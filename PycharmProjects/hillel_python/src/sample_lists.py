import random

a = ['a', 'b', 'c']

b = ['a', 2, 'c', [0, 10, [4, 'z']]]

#
# print(type(a))
# print(type(b))
# print(b[0])
# print(b[0:2])
# print(len(b))
#
# for i in range(len(b)):
#     print(b[i])
#
# print(b[3][2][1])

n = 3
random_list = []

for i in range(n+1):
    random_list.append(random.random())

print(random_list)
print(len(random_list))


# реализовать все методы из модуля list
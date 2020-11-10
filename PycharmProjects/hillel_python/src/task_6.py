# Программа = Алгоритмы+ Структура данных (с) Н.Вирт
# В Python - динамическая типизыция

# Пример из pascal:
# var a : integer;
#     b : string;


#
# a = input('Enter number 1: ')
# # b = input('Enter number 2: ')
# #
# # c = a + b
# #
# # print(c)
#
# print(type(a))
# # print(type(b))
# # print(type(c))
#
# a = 3
# print(type(a))
#
# d1 = a / 2
# print(d1) # 1.5
# print(type(d1))
#
# d2 = a // 2 # 1
# ost = a % 2 # 1
# print(d2)
# print(ost)
#
# print(type(d2))
#
# bool_1 = True  # Логическая 1
# bool_2 = False  # логический 0
#
# print(type(bool_1))
#
# res_1 = (bool_1 != 0)
# print(res_1)
#
# res_2 = ('xyu' == "xyu")  # !=
# print(res_2)

# import numpy as np
# import pandas as pd
#
# a = np.linspace(0, 14, num=8)
#
# print(a)
# print(type(a))
#
# b = pd.read_csv('UCI_Credit_Card.csv')
# print(type(b))
# print(type(b.to_numpy()))

# a = 'text_1'
# b = a
# c = 'new_text'
#
# print(a)
# print (b)
# print(id(a))
# print(id(b))
# print(id(c))
#
#
# a = 'new_text'
# print(a)
# print(b)
# print(id(a))
# print(id(b))
# print(id(c))


# print(isinstance(a, int))
# print(isinstance(a, str))
#
# import math
#
#
# numerator = 2
# denominator = 0
#
# try:
# #     res = numerator / denominator
#     res = math.sqrt(-1)
#     print(res)
#
# except:
#
#     print('Division by zero!')
#
# finally:
#     print('Well done!')


# res = 2 / 0
# print(res)
#
#
# import math
# import cmath
#
# res = math.sqrt(0.25)
# print(res)
#
# res_2 = cmath.sqrt(-1)
# print(res_2)
#
# # ---------------------------------------
#
# from cmath import *
# from math import *
#
# res = sqrt(-1)
# print(res)


import logging
import math


number = float(input('Enter number: '))

logging.basicConfig(level=logging.DEBUG,
                    filename='app_test.log',
                    filemode='w')

logging.info("Start program")


try:
    res = math.sqrt(number)
    logging.info(f'result = {res}')

except:
    logging.info('SQRT() param is negative!')

finally:
    logging.info("End program")


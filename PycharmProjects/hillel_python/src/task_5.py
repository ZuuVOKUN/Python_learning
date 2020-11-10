# #
# #
# # def power_number(base, power):
# #
# #     res = 1
# #
# #     for i in range(1, power+1):
# #
# #         res = res * base
# #
# #     return res
# #
# # print(power_number(1000, 2))
#
#
# # files = ['1.txt', '2.txt', '3.txt']
# #
# # for file in files:
# #     print(file)
# #
# # len_files = len(files)
# # print(len_files)
#
#
# # colors = ['red', 'blue', 'green']
# # print(len(colors))
#
#
# # for color in colors:
# #     print(color)
# #
# #
# # for i in range(len(colors)):
# #     print(str(i) + '->' + colors[i])
#
#
# #
# #
# # a = 2  # основание степени
# #
# # b = 3000  # показатель степени
# #
# # c = a ** b # 2 * 2 * 2
# #
# # print(power_number())
# #
# #
#
# power = 100
# for i in range(5, power, 13):  # итератор
#     print(i)
#
init_temp = 8
init_fuel = 1
temp_step = 0.50

threshold_temp = 20

temperature = init_temp
fuel = init_fuel

while temperature < threshold_temp:
    # fuel = fuel + 1
    fuel += 1

    # temperature = temperature + temp_step
    temperature += temp_step

    print('Temp: ' + str(temperature) + 'Fuel: ' + str(fuel))  # not pythonic
    print(f'Temp: {temperature} Fuel: {fuel}')  # >= Python 3.6 # new pythonic
    print('Temp: {} Fuel: {}' .format(temperature, fuel))  # old pythonic

temperature = init_temp
# #
while True:

    temperature = temperature + temp_step
    print(temperature)
    if temperature >= threshold_temp:
        break

#
# # def tax(income):
# #     if income <= 10000:
# #         res = 0.03 * income
# #     elif income > 10000 and income <= 50000:
# #         res = 0.05 * income
# #     else:
# #         res = 0.07 * income
# #
# #     return res
# #
# #
# # print(tax(10000))
#
#
# import math
# import cmath
# import random
#
# # a = math.sqrt(25)
# # print(a)
# #
# # b = math.pow(5, 2)
# # print(b)
# #
# # a = 1
# # b = 6
# # c = 5
# #
# # d = b**2 - 4 a * c
# #
# # if d > 0:
# #     x1 =
# #     x2 =
# #     print(x1, x2)
# # else d < 0:
# #     print('No roots')
#
# # c = random.random()
# # print(c)
# #
# # def get_random_for():
# #     """for loop, while loop"""
# #
# # def get_random_while():
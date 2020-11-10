def benchmark(func):
    import time

    def wrapper(a, b):
        start = time.time()
        res = func(a, b)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
        return res

    return wrapper

@benchmark
def summa_2(a, b):
    for i in range(0, 10000):
        res = a ** 2 + b ** 2
    return res


@benchmark
def product_2(a, b):
    res = a ** 2 * b ** 2
    return res


@benchmark
def power_2(a, b):
    res = (a ** 2) ** (b ** 2)
    return res


result_1 = summa_2(a=10, b=20)

result_2 = product_2(a=result_1, b=30)
# dict_param = {'a': 2, 'b': 3}

print(summa_2(a=3, b=4))
print(product_2(a=3, b=4))
print(power_2(a=3, b=4))
#
# print(summa_2(**dict_param))
# print(product_2(**dict_param))
# print(power_2(**dict_param))
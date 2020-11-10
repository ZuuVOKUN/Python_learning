import math
import cmath
import logging


logging.basicConfig(level=logging.DEBUG,
                    filename='Discr.log',
                    filemode='w')


logging.info("Start program")


try:
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    c = float(input('Enter c: '))

    d = b ** 2 - 4 * a * c
    logging.info(f'Discr = {d}')

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        logging.info(f'Result if D > 0: 1st root = {x1}, 2nd root = {x2}')
        logging.info(f'Type x1, x2 = {(type(x1))}, {(type(x2))}')
        logging.info(f'isinstance = {isinstance(x1, int)}, {isinstance(x2, int)}')

    elif d == 0:
        x = -b / (2 * a)
        logging.info(f'Result if D = 0: One root = {x}')
        logging.info(f'Type x = {(type(x))}')
        logging.info(f'isinstance = {isinstance(x, int)}')

    elif d < 0:
        logging.info('Result: No roots!')


except:
    logging.info('Data not input or inputed incorrectly!')


finally:
    logging.info("End program")

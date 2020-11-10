# Не могу разобраться до сих пор с путем. Код упорно не воспринимает конфиги из другой папки.
# При чем при прописывании пути через терминал- выводит проверочный принт, но в логе по прежнему инкорект.


import math
import logging
import argparse
import json

logging.basicConfig(level=logging.DEBUG,
                    filename='diskr.log',
                    filemode='w')
logging.info('Start program')


try:
    def parse_args():
        parser = argparse.ArgumentParser(
            description='???')

        parser.add_argument('--path',
                            type=str,
                            required=True,
                            help='coefficients')

        return parser.parse_args()

    args = parse_args()
    path_config = args.path
    configs = open(path_config)

    config = json.loads(configs.read())

    a = config['a']
    b = config['b']
    c = config['c']
    d = b ** 2 - 4 * a * c

    logging.info(f'diskr = {d}')
    logging.info(f'Path : {args.path}')
    print(d)

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        logging.info(f'Result if D > 0: 1st root = {x1}, 2nd root = {x2}')
        logging.info(f'Type x1, x2 = {(type(x1))}, {(type(x2))}')
        logging.info(f'isinstance int x1, x2 = {isinstance(x1, int)}, {isinstance(x2, int)}')
        print(x1, x2)

    elif d == 0:
        x = -b / (2 * a)
        logging.info(f'Result if D = 0: One root = {x}')
        logging.info(f'Type x = {(type(x))}')
        logging.info(f'isinstance int x = {isinstance(x, int)}')

    elif d < 0:
        logging.info('Result: No roots!')
        logging.info(f'isinstance int d = {isinstance(d, int)}')


except:
    logging.info('Incorrect input!')

finally:
    logging.info("End program")

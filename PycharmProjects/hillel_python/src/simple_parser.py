import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description='Simple input for quadratic equation Ax^2 + Bx + C = 0')

    parser.add_argument('--a', type=float, required=True,
                        help='Coefficient A')
    parser.add_argument('--b', type=float, required=True,
                        help='Coefficient B')

    return parser.parse_args()



if __name__ == '__main__':
    print('This program is being run by itself')
    args = parse_args()
    print(args.b)

else:
    print('Program being imported from another module')
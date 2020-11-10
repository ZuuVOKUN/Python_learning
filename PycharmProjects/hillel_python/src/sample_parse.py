import argparse


def parse_args():
    # parser = argparse.ArgumentParser(
    #     description='Simple input for quadratic equation Ax^2 + Bx + C = 0')
    parser = argparse.ArgumentParser(description='My first argparse program')

    # parser.add_argument('--a',
    #                     type=float,
    #                     required=True,
    #                     help='coefficient A')
    #
    # parser.add_argument('--b',
    #                     type=float,
    #                     required=True,
    #                     help='Coefficient B')
    #
    parser.add_argument('--name',
                        type=str,
                        required=True,
                        help='We need your name')


    parser.add_argument('--surname',
                        type=str,
                        required=True,
                        help='We need your surname')

    return parser.parse_args()


args = parse_args()

print('Hello, ' + args.name + ' ' + args.surname + '!')
# print(args.a)
# print(args.b)


# if __name__ == '__main__':
#
#     print('This program is being run by itself')
#     args = parse_args()
#     print(args.b)

# else:
#
#     print('Program being imported from another module')
#
# print('Hello,' + args.name +  args.surname + '!')
# #
# #


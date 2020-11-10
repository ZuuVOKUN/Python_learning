import random


def get_random_for():
    for i in range(3):
        i = random.randint(1, 100)
        print(i)
    return

print(get_random_for())

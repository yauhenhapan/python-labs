import numpy as np


def enter_value():
    while True:
        try:
            val = int(input("Enter your value: "))
        except ValueError:
            print("Value must be a number, try again")
            continue

        if val <= 1:
            print("Value must be greater than 1, try again")
        else:
            break;
    return val

def print_matrix(dimension):
    array_result = np.ones((dimension, dimension))
    array_result[1: -1, 1: -1] = 0
    return array_result


def main():
    dimension = enter_value()
    print("dimension = ", dimension)
    print(print_matrix(dimension))

main()

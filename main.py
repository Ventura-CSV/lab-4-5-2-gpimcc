import random


def main():
    total = 0
    numbers = []
    while total <= 100:
        num = random.randint(1, 100)
        numbers.append(num)
        total += num
    total = total - numbers[-1]
    """
    ########################################
    Code Your Program here
    ########################################
    """

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()

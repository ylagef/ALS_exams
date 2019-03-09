from math import floor


def histogram(numbers):
    minimum = min(numbers)
    for i in range(len(numbers)):
        numbers[i] = floor(numbers[i] / minimum)

    maximum = max(numbers)
    for i in range(len(numbers)):
        numbers[i] = floor((numbers[i] * 11) / maximum)

    print(numbers)
    for n in numbers:
        output = ""
        for i in range(n):
            output += "*"
        print(output)


numbers = [3, 2, 20, 5, 3, 7, 14, 16, 10]
# numbers = [11, 3, 5, 2, 10, 2, 2, 1]

histogram(numbers)

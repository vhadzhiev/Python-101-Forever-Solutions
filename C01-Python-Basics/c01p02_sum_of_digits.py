def sum_of_digits(n):
    number = abs(n)
    result = 0
    while number != 0:
        result += abs(number % 10)
        number = number // 10

    return result


print(sum_of_digits(1325132435356))
print(sum_of_digits(123))
print(sum_of_digits(6))
print(sum_of_digits(-10))

def fact_digits(number):
    list_of_numbers = list(str(number))
    total = 0
    for num in list_of_numbers:
        result = 1
        for x in range(1, int(num) + 1):
            result *= x
        total += result

    return total


print(fact_digits(101))
print(fact_digits(111))
print(fact_digits(145))
print(fact_digits(999))

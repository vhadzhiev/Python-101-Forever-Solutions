def is_number_balanced(number):
    numbers_list = list(str(number))
    if len(numbers_list) == 1:
        return True
    middle_index = len(numbers_list) // 2
    left_part = numbers_list[:middle_index]
    right_part = numbers_list[middle_index:]
    if len(numbers_list) % 2 != 0:
        right_part = numbers_list[middle_index + 1:]

    return sum([int(x) for x in left_part]) == sum([int(x) for x in right_part])


print(is_number_balanced(9) is True)
print(is_number_balanced(4518) is True)
print(is_number_balanced(28471) is False)
print(is_number_balanced(1238033) is True)

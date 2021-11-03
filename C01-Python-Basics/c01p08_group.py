def group(items):
    groups = []
    if not items:
        return groups
    new_group = []
    for x in items:
        if not new_group or x in new_group:
            new_group.append(x)
        else:
            groups.append(new_group)
            new_group = [x]
    groups.append(new_group)

    return groups


print(group([1, 1, 1, 2, 3, 1, 1]) == [[1, 1, 1], [2], [3], [1, 1]])
print(group([1, 2, 1, 2, 3, 3]) == [[1], [2], [1], [2], [3, 3]])
print(group([]) == [])
print(group([1]) == [[1]])
print(group([1, 1, 1, 1]) == [[1, 1, 1, 1]])

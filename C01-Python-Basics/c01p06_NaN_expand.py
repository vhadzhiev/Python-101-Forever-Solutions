def nan_expand(times):
    if times > 0:
        return f"{times * 'Not a '}NaN"
    return ""


print(nan_expand(0) == "")
print(nan_expand(1) == "Not a NaN")
print(nan_expand(2) == "Not a Not a NaN")
print(nan_expand(3) == "Not a Not a Not a NaN")

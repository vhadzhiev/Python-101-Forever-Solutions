def iban_formatter(iban):
    iban = iban.replace(' ', '')
    split_iban = []
    chars = ''
    for i in range(len(iban)):
        chars += iban[i]
        if (i + 1) % 4 == 0 or i == (len(iban) - 1):
            split_iban.append(chars)
            chars = ''

    return ' '.join(split_iban)


print(iban_formatter("BG80BNBG96611020345678") == "BG80 BNBG 9661 1020 3456 78")
print(iban_formatter("BG80 BNBG 9661 1020 3456 78") == "BG80 BNBG 9661 1020 3456 78")
print(iban_formatter("BG14TTBB94005362446381") == "BG14 TTBB 9400 5362 4463 81")
print(iban_formatter("BG91UNCR70001864961754") == "BG91 UNCR 7000 1864 9617 54")


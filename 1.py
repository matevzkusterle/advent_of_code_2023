with open('file.txt', 'r') as f:
    total_sum = 0
    for line in f:
        digits = [int(i) for i in line if i.isdigit()]
        if len(digits) == 1:
            cifra = digits[0] * 10 + digits[0]
        elif len(digits) > 1:
            cifra = digits[0] * 10 + digits[len(digits) - 1]
        else:
            cifra = 0
        total_sum += cifra

print(total_sum)
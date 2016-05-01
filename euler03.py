num = 600851475143
factor = 2
while factor != num:
    if num % factor == 0:
        num //= factor
    else:
        factor += 1

print(factor)

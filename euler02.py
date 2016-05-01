a = 1
b = 1
sum = 0
while b < 4000000:
    if b % 2 == 0:
        sum += b

    tmp = a + b #2
    a = b #1
    b = tmp


print(sum)

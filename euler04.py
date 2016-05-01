def is_palindrome(num):
    s = str(num)
    return s == s[::-1]

largest = 0

for i in range(100,1000):
    for j in range(100,1000):
        p = i*j
        if is_palindrome(p):
            if p>largest:
                largest = p

print(largest)

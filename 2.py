a, b = 0, 1
summa = 0
while b <= 4000000:
    if b / 2 == b // 2:
        summa += b
    b, a = b + a, b
print(summa)

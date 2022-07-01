a = 600851475143
greatest_prime_divisor = 0


def simple_number(b):
    count = 0
    for i in range(1, b):
        if b % i == 0:
            count += 1
            if count > 1:
                break
    return count

'''необязательная проверка, но увеличивает быстродействие еще в 2 раза
 так как парные числа, кроме 2, точно не являются простыми'''

f = int(a ** 0.5)
if f % 2 == 0:
    z = f - 1
else:
    z = f

for i in range(z, 1, -2):
    c = a / i
    if a % i == 0:
        print("проверка на простоту")
        d = simple_number(i)
        if d == 1:
            greatest_prime_divisor = i
            print(greatest_prime_divisor)
            break

# This is slow!
def meets_realistic_divisibility_criteria(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True


num = 20
found = False
while not found:
    if meets_realistic_divisibility_criteria(num):
        print(num)
        break
    else:
        num += 20


# One could also...
num = 20
found = False
while not found:
    if set([n % x == 0 for x in range(1, 21)]) == {True}:
        print(num)
        break
    else:
        num += 20

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

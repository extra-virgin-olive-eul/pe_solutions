from itertools import permutations

"""
Not blazing fast, but well under the minute mark:

joe@nor:~/pe_solutions/43$ (master) time python3 lexical_leftovers.py 
<stdout redacted>

real    0m18.143s
user    0m18.136s
sys     0m0.004s

I always appreciate the opportunity to get to use all() :)

"""

def this_bizarre_divisibility_property(int_as_str):
    conds = [int(int_as_str[1:4]) % 2 == 0,
             int(int_as_str[2:5]) % 3 == 0,
             int(int_as_str[3:6]) % 5 == 0,
             int(int_as_str[4:7]) % 7 == 0,
             int(int_as_str[5:8]) % 11 == 0,
             int(int_as_str[6:9]) % 13 == 0,
             int(int_as_str[7:10]) % 17 == 0]

    return all(conds)


if __name__ == '__main__':
    p = permutations('0123456789')

    weirdos = list()
    for element in p:
        perm_as_str = ''.join([str(e) for e in element])

        if this_bizarre_divisibility_property(perm_as_str):
            weirdos.append(perm_as_str)

    print(sum([int(w) for w in weirdos]))

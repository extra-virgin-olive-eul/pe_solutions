"""

Slow, but good enough.

joe@nor:~/pe_solutions/32$ (master) time python3 uninformed.py 
<stdout redacated>

real    0m46.295s
user    0m46.016s
sys     0m0.256s

"""

def pair_product_is_pandigital(pair):
    left, right = pair
    product = left * right
    str_expr = [e for e in str(left) + str(right) + str(product)]
    str_expr.sort()
    if str_expr == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return (left, right, product)
    else:
        return False


def pairwise(L):
    """
    Given a sequence [1,2,3,4...],
    return a list of all pairwise
    combinations (where order doesn't matter).

    [1,2,3,4] => [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    """
    pairs = list()
    for idx, item in enumerate(L):
        for element in L[idx+1:]:
            pairs.append((item,element))
    return pairs


if __name__ == '__main__':
    pandigital_product_pairs = list()

    possible_pairs = pairwise([i for i in range(1, 5001)])

    for pair in possible_pairs:
        found_products = pair_product_is_pandigital(pair)
        if found_products:
            pandigital_product_pairs.append(found_products)

    print(pandigital_product_pairs)

    unique_products = list(set([fp[2] for fp in pandigital_product_pairs]))
    print(sum(unique_products))

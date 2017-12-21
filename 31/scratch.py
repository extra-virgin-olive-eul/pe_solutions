AMOUNT = 100


denominations = [{'value': 1, 'name': 'penny'},
                 {'value': 5, 'name': 'nickel'},
                 {'value': 10, 'name': 'dime'}]


combinations = []


for denom in denominations:
    solely_this_denom = "{} {}".format(int(AMOUNT/denom['value']), denom['name'])
    combinations.append(solely_this_denom)

    count, increment = int(AMOUNT/denom['value'])
    while count < AMOUNT:
        pass 

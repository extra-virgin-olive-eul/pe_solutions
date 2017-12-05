"""
Seed a dictionary where: 
    * each key is an int
    * each value is a natural language representation of said int

For each int in range (1-1000), add an entry to word_rep if one 
does not already exist.

Once that dict is built, sum the lengths of all the ints (as words),
but totalling all values in the word_rep dict (using letter_count to
strip hyphens and spaces).
"""

word_rep = {1   : 'one',
            2   : 'two',
            3   : 'three',
            4   : 'four',
            5   : 'five',
            6   : 'six',
            7   : 'seven',
            8   : 'eight',
            9   : 'nine',
            10  : 'ten',
            11  : 'eleven',
            12  : 'twelve',
            13  : 'thirteen', 
            14  : 'fourteen',
            15  : 'fifteen',
            16  : 'sixteen',
            17  : 'seventeen',
            18  : 'eighteen',
            19  : 'nineteen',
            1000: 'one thousand'}


def add_number_entry(i, num_dict=word_rep):
    """
    Given a number i (where 20 < i > 1000),
    add an entry to num_dict where:
        * the key is i
        * the value is a natural language rep of the int in question
    """
    prefixes = {2: 'twenty',
                3: 'thirty',
                4: 'forty',
                5: 'fifty',
                6: 'sixty',
                7: 'seventy',
                8: 'eighty',
                9: 'ninety'}

    if len(str(i)) == 2:
        first_digit, second_digit = str(i)[0], str(i)[1]
        if second_digit == '0':
            num_dict[i] = '{}'.format(prefixes[int(first_digit)])
        else:
            num_dict[i] = '{}-{}'.format(prefixes[int(first_digit)], num_dict[int(second_digit)])
    elif len(str(i)) == 3:
        first_digit, two_digit_remainder = str(i)[0], str(i)[1:]
        if two_digit_remainder == '00':
            num_dict[i] = '{} hundred'.format(num_dict[int(first_digit)])
        else:
            num_dict[i] = '{} hundred and {}'.format(num_dict[int(first_digit)], num_dict[int(two_digit_remainder)])
    else:
        raise ValueError("I only work with two or three digit ints!")


if __name__ == '__main__':
    # Populate the globally-accessible word_rep dictionary with
    # the linguistic representation of each num in the range
    for i in range(1, 1000):
        if i not in word_rep:
            add_number_entry(i)

    def letter_count(num_as_str):
        return len(num_as_str.replace('-', '').replace(' ', ''))

    TOTAL = 0
    for k, v in word_rep.items():
        TOTAL = TOTAL + letter_count(v)

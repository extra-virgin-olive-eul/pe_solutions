import os
import string


def file_to_sorted_list(abs_path_to_file):
    with open(abs_path_to_file) as f:
        contents = f.read()

    names = contents.replace('"', '').split(",")
    names.sort()
    return names


# A = 1, B = 2, C = 3, etc.
alpha_lookup = dict(zip(string.ascii_uppercase, range(1, 27)))


def name_score(name):
    return sum([alpha_lookup.get(letter) for letter in name])


if __name__ == '__main__':
    names = file_to_sorted_list('p022_names.txt')

    table = list()
    for idx, name in enumerate(names):
        d = {'index': idx+1,
             'name': name, 
             'name_score': name_score(name)}
        d['total_score'] = d['index'] * d['name_score']
        table.append(d)


    print(sum([name.get('total_score') for name in table]))

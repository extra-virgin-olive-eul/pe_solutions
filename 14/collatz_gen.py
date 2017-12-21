seq = [1,4,8,16]


def has_no_remainder(num):
    return str(num).endswith('.0')


def next_seq_member():
    seed_value = seq[-1]
    if has_no_remainder((seed_value-1)/3):
        seq.append(int((seed_value-1)/3))
    else:
        seq.append(seed_value*2)


def model_collatz_sequence(num_of_iterations):
    for i in range(1, num_of_iterations):
        next_seq_member()

"""
Keep track of the collatz_seq_len result per int in a globally-accessible dict.

If there's an entry in said dict during processing (say, {'13': 10}),
return the length of the partially constructed seq + the length of the
pre-computed list.

This provides a decent speedup over collatz.py.

joe@nor:~/pe_solutions/14$ (master) time python3 collatz.py 
<stdout redacted>

real    0m19.469s
user    0m19.460s
sys     0m0.004s


joe@nor:~/pe_solutions/14$ (master) time python3 collatz_memo.py
<stdout redacted>

real    0m4.779s
user    0m4.728s
sys     0m0.020s
"""

seq_len_counts = {} 


def collatz_seq_len(n):
    seq = list()
    while n != 1:
        if str(n) in seq_len_counts:
            return len(seq) + seq_len_counts[str(n)]
        if n == 2:
            seq.append(1)
            return len(seq)
        elif n % 2 == 0:
            seq.append(n)
            n = n//2
        else:
            seq.append(n)
            n = (3*n) + 1


generates_longest_seq = 0
max_seq_len = 0


for i in [n for n in range(2, 1000000) if n % 2 != 0]:
    new_seq_len = collatz_seq_len(i)
    # Cache the list lengths to avoid unnecessary recalculation
    seq_len_counts[str(i)] = new_seq_len
    if new_seq_len > max_seq_len:
        generates_longest_seq = i
        max_seq_len = new_seq_len

print(generates_longest_seq, max_seq_len)

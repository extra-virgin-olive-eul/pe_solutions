"""
My only half-decent insight here was to not bother with checking
the length of sequences starting w/ a num evenly divisible by 2.
(Hence the janky-looking "for" declaration surrounding a list
comprehension.)

Everything else is a fairly straightforward translation of the 
problem statement into code.

I can't help but think this sequence might be built in reverse
somehow, though I'm not sure how yet. This also seems like a good
use case for some memoization. Again though, I'm not sure how yet.

Maybe I'll revisit this one later.
"""

def collatz_seq(n):
    seq = list()
    while n != 1:
        if n == 2:
            seq.append(1)
            return seq
        elif n % 2 == 0:
            seq.append(n)
            n = n//2
        else:
            seq.append(n)
            n = (3*n) + 1


generates_longest_seq = 0
max_seq_len = 0


for i in [n for n in range(2, 1000000) if n % 2 != 0]:
    new_seq_len = len(collatz_seq(i))
    if new_seq_len > max_seq_len:
        generates_longest_seq = i
        max_seq_len = new_seq_len

print(generates_longest_seq, max_seq_len)

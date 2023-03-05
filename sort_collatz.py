import random
def collatz(n):
    collatz_list = []
    while n > 1:
        collatz_list.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    collatz_list.append(1)
    return collatz_list

def sort_collatz(limit):
    r_set = set(range(2, limit))
    max_len_set = set()
    while r_set:
        n = random.choice(list(r_set))
        collatz_set = set(collatz(n))
        max_len_set.update(collatz_set)
        r_set -= collatz_set
    max_len = list(max_len_set)
    max_len_lengths = [len(collatz(j)) for j in max_len]
    max_length = max(max_len_lengths)
    maxes = [i for i in max_len if len(collatz(i)) == max_length]
    print("maxes:", maxes)

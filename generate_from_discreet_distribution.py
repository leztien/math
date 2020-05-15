"""
generate discreet values according to the given probabilties 
"""


import random


def make_bin_breaks(probabilities):
    probabilities = sorted(probabilities)
    assert sum(probabilities)==1.0,"error"
    return [sum(probabilities[:i]) for i in range(1,len(probabilities)+1)]
    

def discretize(value, bins):
    for bin_number, bin_break in enumerate(bins):
        if value < bin_break:
            return bin_number
    else:
        return bin_number+1


def generate_from_discreet_distribution(probabilities, n=1000):
    bins = make_bin_breaks(probabilities)
    return [discretize(random.random(), bins=bins) for _ in range(n)]
    


p = (0.1, 0.6, 0.25, 0.05)  #must sum to 1.0
m = 500000
arr = generate_from_discreet_distribution(probabilities=p, n=m)

pp = sorted([arr.count(value)/len(arr) for value in frozenset(arr)])
pp = [round(v,3) for v in pp]
print(sorted(p), pp)

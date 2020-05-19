def jaccard_distance(set1, set2):
    """set distance"""
    S1,S2 = (frozenset(S) for S in (set1,set2))
    S = S1 | S2
    d = {v:k for k,v in enumerate(tuple(S))}
    S1,S2 = ({d[v] for v in S} for S in (S1,S2))
    return 1 - len(S1 & S2) / len(S1 | S2)
      
S1 = (10,20,"X", "Abc", None, object)
S2 = {10, "X", object, 300, 400}

ans = jaccard_distance(S1, S2)
print(ans)

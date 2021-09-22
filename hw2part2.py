def jaccardIndex(A, B):
    a1 = A.union(B)
    b1 = A.intersection(B) 
    aCard = len(a1)
    bCard = len(b1)
    jaccardIndex = bCard/aCard
    return jaccardIndex
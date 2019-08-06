def solution(L, x) :
    if x > L[len(L)-1]:
        L.insert(len(L), x)
    else:
        for i in range(len(L)):
            if x < L[i]:
                L.insert(i, x)
                break
    return L

L = [1,2,3,4,5,6]
print(solution(L,7))

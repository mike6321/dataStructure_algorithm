
def solution(L, x):
    answer = []

    for idx in range(len(L)):
        if L[idx] == x:
            answer.append(idx)

    if len(answer) == 0:
        answer.append(-1)
    return answer

L = [1, 2, 1, 1, 3]
print(solution(L,7))
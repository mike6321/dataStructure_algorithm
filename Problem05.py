def solution(x):
    answer = 0
    if x < 2 :
        return x
    return solution(x-1) + solution(x-2)


print(solution(7))
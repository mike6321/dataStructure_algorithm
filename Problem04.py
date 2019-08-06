def solution(L, x):
    #L = [2, 3, 5, 6, 9, 11, 15]
    answer = 0
    start = 0
    end = len(L)-1

    while start <= end:
        middle = (start+end)//2
        if L[middle] < x : #중간 값이 탐색 값보다 작을경우
            start = middle+1
            '''
            2, 3, 5, 6, 9, 11, 15
            middle 6(3)    x 5(2)
            2, 3, 5,   6,    9, 11, 15
            '''
        elif L[middle] > x :
            end = middle -1
        else: #같을때
            return middle

    return -1



    return answer


L = [2, 3, 5, 6, 9, 11, 15]
print(solution(L,5))
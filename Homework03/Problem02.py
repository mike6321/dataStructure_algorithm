class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

#저 그지같은 클래스를 사용하니 오류가 터져서 stack에서 제공하는 것을 사용하였습니다.
#저딴걸 왜 쓰라는거야 미친놈이

def solution(a):

    stack = []
    answer = ''
    for i in a:

        #수식이 아닌 문자들은 미리 문자열에 저장 시켜둡니다.
        if i not in ["*", "/", "+", "-", "(", ")"]:
            answer+=i
        #여는 괄호 일때 스택에 append 시킵니다.
        elif i == "(":
            stack.append(i)
        #닫는 괄호 일때 스택의 제일 첫번째가 여는 괄호가 아니라면 pop합니다.
        elif i == ")":
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.pop()
        #수식일때 제일 첫번째의 우선순위보다 작다면  pop 합니다.
        else:
            while stack and prec[i] <= prec[stack[-1]]:
                answer+=stack.pop()
            stack.append(i)

    while stack:
        answer+=stack.pop()

    return  answer

print(solution("a+(b+c)"))


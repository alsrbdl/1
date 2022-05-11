def solution(x, n):
    answer = []
    y=x
    for i in range(n):
        answer.append(x)
        x += y     
    return answer
def solution(phone_number):
    a=len(phone_number) - 4
    b='*'*a+phone_number[-4]+phone_number[-3]+phone_number[-2]+phone_number[-1]
    return b
#음성 파일 용량 계산
h,b,c,s=map(int, input().split())
n=(h*b*c*s)/1024/1024/8
print(format(n, ".1f"),'MB')
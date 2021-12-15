n = int(input())
count = 1
count2 = 6
s = 1
while(n>count):
    if(n==1):
      break
    count += count2
    count2 += 6
    s += 1

print(s)
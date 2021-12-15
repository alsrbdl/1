n = int(input())
m = 1

if n<10:
  n *= 10
  
nn = n
a = n//10
b = n%10
n = b*10 + ((a + b)%10)

while(nn != n):
  m += 1
  a = n//10
  b = n%10
  n = b*10 + ((a + b)%10)
  
print(m)
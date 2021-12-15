n = int(input())
a = 1
b = 1
c = 1

while(n>c):
  b += a
  a += 1 
  c += a
  
if(a % 2 == 0):
  print(1+n-b,'/',a-n+b,sep='')
else:
  print(a-n+b,'/',1+n-b,sep='')
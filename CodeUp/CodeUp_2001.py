a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

p = [a, b, c]
j = [d, e]

p.sort()
j.sort()

pp = p[0]
jj = j[0]

sum = round((pp + jj) * 1.1, 1)

print(sum)
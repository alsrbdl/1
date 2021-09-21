s=int(input())
def b() :
	print('*', end='')
def k() :
	print('x', end='')

for j in range(s) :
	for i in range(s) :
		b()
	for i in range(s) :
		k()
	for i in range(s) :
		b()
	print('')
		
for j in range(s) :
	for i in range(s) :
		print(' ', end='')
	for i in range(s) :
		k()
	for i in range(s) :
		k()
	print('')
for j in range(s) :
	for i in range(s) :
		b()
	for i in range(s) :
		print(' ', end='')
	for i in range(s) :
		b()
	print('')
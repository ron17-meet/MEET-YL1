def divisors(n):
	y=1
	while (n>=y):
		if(n%y==0):
			print(y)
		y=(y+1)
x = int(input('Enter a number:'))
divisors(x)
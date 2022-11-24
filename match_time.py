t = int(input())
for i in range(t):
	N,A,B = input().split()
	time = 0
	N = int(N)
	while(N != 1):
		time = time + int(A)
		if (N != 2):
			time = time + int(B)
		N = N//2
	print(time)

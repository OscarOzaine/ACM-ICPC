import math as m

def func(p, a, b, c, d, i):
	return p * (m.sin((a * i + b)) + m.cos(c * i + d) + 2)

while True:
    try:
    	ans = 0.0
    	current = 0.0
    	k = 1
    	p,a,b,c,d,n = map(int, list(input().strip().split(' ')))

    	minimum =  func(p, a, b, c, d, 1)
    	maximum = minimum
    	for k in range(1, n):
    		price = func(p, a, b, c, d, k)
    		if price >= maximum:
    			maximum = price
    			minimum = price
    		elif price < minimum:
    			minimum = price
    			if maximum - minimum > ans:
    				ans = maximum - minimum

    	if maximum - minimum > ans:
    		ans = maximum - minimum

    	print(ans)


    except:
        break


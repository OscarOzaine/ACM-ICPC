import math as m

def amalgamatedAntichokes(p, a, b, c, d, n):
	last_price = 0
	desc = 0
	maxx = 0
	for i in range(1, n+1):
		pr = p * (m.sin((a * i + b)) + m.cos(c * i + d) + 2)
		if pr < last_price:
			desc = last_price - pr
		else:
			desc = 0
			last_price = pr

		if maxx < desc:
			maxx = desc

	return maxx
		
		

while True:
    try:
    	p,a,b,c,d,n = map(int, raw_input().strip().split(' '))

        print amalgamatedAntichokes(p, a, b, c, d, n) 
    except:
        break





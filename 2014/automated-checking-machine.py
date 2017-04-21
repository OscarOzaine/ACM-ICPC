#Regionals 2014 - Latin America
##6821 - Automated Checking Machine

def automatedCheckingMachine(arr1, arr2):
	for i in range(0, len(arr1)):
		if int(arr1[i]) == int(arr2[i]):
			return 'N'
	return 'Y'

while True:
    try:
        n = list(input().strip().split(' '))
        m = list(input().strip().split(' '))
        print(automatedCheckingMachine(n, m)) 
    except:
        break
exit(0)
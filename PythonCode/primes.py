import math



def genprimes():
    count = 3
    primes = []
    
    while count < 1000000:
        isprime = True
        
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0: 
                isprime = False
                break
        
        if isprime:
            primes.append(count)
        
        
        count += 1

    return primes

diff = [2, 4, 6, 8, 14, 10, 12, 18, 20, 22, 34, 24, 16, 26, 28, 30, 32, 36, 44, 42, 40, 52, 48, 38, 72, 50, 62, 54, 60, 58, 46, 56, 64, 68, 86, 66, 70, 78, 76, 82, 96, 112, 100, 74, 90, 84, 114, 80, 88, 98, 92]


def difference(x):
    differences = []
    for i in range(len(x)-1):      
        test = abs(x[i+1] - x[i])
        if test not in differences:
            differences.append(test)
        i += 1
    print(differences)

    

difference(diff)



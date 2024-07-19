primes=[]

for number in range(2,9999):
    for factor in range(2, int(number**0.5)):
        if number % factor ==0:
            break
    else:
        primes.append(number)

print(primes)


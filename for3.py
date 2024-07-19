for number in range(2,100):
    foun_factors=False
    for factor in range(2,int(number**0.5)+1):
        if number%factor==0:
            foun_factors=True
            break
    if not foun_factors:
        print(f'{number} is prime!')
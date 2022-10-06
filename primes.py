
# check if a number is prime
def primetest(potentialprime):
    divisor = 2

    while divisor <= potentialprime:
        if potentialprime == 2:
            return True
        elif potentialprime % divisor == 0:
            return False
        while potentialprime % divisor != 0:
            if potentialprime - divisor > 1:
                divisor += 1
            else:
                return True


def primes(number_of_primes):
    count = 0
    primesList = []
    potentialprime = 2

    # generate prime numbers until count reaches the user input number
    while count < number_of_primes:
        if primetest(potentialprime) == True:
            # add the prime number to the list
            primesList.append(potentialprime)
            count += 1
        potentialprime += 1
    return primesList


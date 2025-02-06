def checkIfPrime(numberCheck):
    for i in range(2, numberCheck):
        if numberCheck % i == 0:
            return False
        else:
            return True


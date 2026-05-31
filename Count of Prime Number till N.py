# Optimal Solution
class Solution:
    def primeUptoN(self, n):

        # Funcrtion to check if tghe given number if prime 
        
        def isprime(num):
            j = 2
            while j * j <= num:
                if num % j == 0:
                    return False
                j += 1
            return True

        number_of_primes = 0

        for i in range(2, n+1):

            if(isprime(i)):
                number_of_primes += 1
        
        return number_of_primes

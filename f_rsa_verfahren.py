import sys
import math


def f_a_n_prime(n_min, n_max):
    a_n_prime = []
    a_n_prime_range = []
    n = 1
    while(n < n_max):
        b_prime = True
        n+=1
        for n_prime in a_n_prime:
            if(n_prime > n**(1./2.)):
                break
            if(n % n_prime == 0):
                b_prime = False
                break
                # not a prime
        
        if(b_prime):
            a_n_prime.append(n)
            if(n > n_min):
                a_n_prime_range.append(n)

    # maybe this is faster than having two separate arrays
    # a_n_prime_range = [n for n in a_n_prime if n > n_min]

    return a_n_prime_range

def f(
): 
    return f_rsa()


def f_rsa():
    n_delta_primes = 10000
    n_min = 100
    n_max = 100000
    a_n_prime = f_a_n_prime(n_min, n_max)

    print(a_n_prime)
if len(sys.argv) > 2:
    n_1 = sys.argv[1]
    n_2 = sys.argv[2]
    #f(int(n_1), int(n_2))
    f()

print("usage:")
print("2^4234")
print("f(2,4234)")
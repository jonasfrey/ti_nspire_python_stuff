import sys
import math

def f(
    n_a
): 
    return f_s_primfaktorenzerlegung(n_a, n_b)

def f_b_prime(n):
    # Corner cases
    if(n <= 1):
        return False
    if(n <= 3):
        return True
     
    # This is checked so that we can skip
    # middle five numbers in below loop
    if(n % 2 == 0 or n % 3 == 0):
        return False
     
    for i in range(5,int(math.sqrt(n) + 1), 6):
        if(n % i == 0 or n % (i + 2) == 0):
            return False
     
    return True

def f_n_prime__next(N):
    # Base case
    if (N <= 1):
        return 2
 
    prime = N
    found = False
 
    # Loop continuously until isPrime returns
    # True for a number greater than n
    while(not found):
        prime = prime + 1
 
        if(f_b_prime(prime) == True):
            found = True
 
    return prime

def f_a_s_primefactors_grouped(
    a_n_primefactor
): 
    a_s_primefactors_grouped = []
    a_n_primefactor__counted = []
    for n_primefactor in a_n_primefactor:
        if(n_primefactor not in a_n_primefactor__counted):
            a_n_primefactor__filtered = [
                n for n in a_n_primefactor if int(n) == int(n_primefactor)
            ]
            a_s_primefactors_grouped.append(
                str(n_primefactor)+"^"+str(len(a_n_primefactor__filtered))
            )
            a_n_primefactor__counted.append(n_primefactor)

    return a_s_primefactors_grouped


def f_s_primfaktorenzerlegung(
    n_a
):
    a_n_primefactor = []
    n_res = n_a
    n_primefactor = 2
    while(True):
        if(f_b_prime(n_res) or n_primefactor > n_a):
            a_n_primefactor.append(int(n_res))
            break
        print(n_primefactor)
        n_res_tmp = n_res / n_primefactor
        if(n_res_tmp % 1 == 0):
            a_n_primefactor.append(n_primefactor)
            n_res = n_res_tmp
        else: 
            n_primefactor = f_n_prime__next(n_primefactor)

    # print("a_n_primefactor: "+str(a_n_primefactor))
    # print(a_n_primefactor)
    a_n_primefactor__sorted = a_n_primefactor
    a_n_primefactor__sorted.sort()
    a_s_primefactors_grouped = f_a_s_primefactors_grouped(a_n_primefactor)
    print(f"{n_a} = {' * '.join([str(n) for n in a_n_primefactor__sorted])} = {' * '.join(a_s_primefactors_grouped)}")

if len(sys.argv) > 1:
    n_1 = sys.argv[1]
    f_s_primfaktorenzerlegung(int(n_1))

print("usage:")
print("f(123)")
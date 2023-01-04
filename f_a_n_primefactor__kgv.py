import sys
import math



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



def f_a_n_primefactor(
    n_a
):
    a_n_primefactor = []
    n_res = n_a
    n_primefactor = 2
    while(True):
        if(f_b_prime(n_res) or n_primefactor > n_a):
            a_n_primefactor.append(int(n_res))
            break
        # print(n_primefactor)
        n_res_tmp = n_res / n_primefactor
        if(n_res_tmp % 1 == 0):
            a_n_primefactor.append(n_primefactor)
            n_res = n_res_tmp
        else: 
            n_primefactor = f_n_prime__next(n_primefactor)
    a_n_primefactor__sorted = a_n_primefactor
    a_n_primefactor__sorted.sort()
    return a_n_primefactor__sorted

def f_a_n_primefactor__kgv(
    n_1, 
    n_2
): 
    a_n_primefactor__n_1 = f_a_n_primefactor(n_1) 
    a_n_primefactor__n_2 = f_a_n_primefactor(n_2) 
    print("---")
    print("f_a_n_primefactor("+str(n_1))
    print(str(n_1)+" = "+str(' * '.join([str(n) for n in a_n_primefactor__n_1])))
    print("---")
    print("f_a_n_primefactor("+str(n_2))
    print(str(n_2)+" = "+str(' * '.join([str(n) for n in a_n_primefactor__n_2])))

    
    a_n_primefactor_kgv = []
    for n_primefactor in a_n_primefactor__n_1 + a_n_primefactor__n_2: 
        if(n_primefactor in a_n_primefactor_kgv):
            continue

        a_n_primefactor__same_in_n_1 = [
                n 
                for 
                n 
                in 
                a_n_primefactor__n_1
                if 
                n == n_primefactor
            ]
        a_n_primefactor__same_in_n_2 = [
                n 
                for 
                n 
                in 
                a_n_primefactor__n_2
                if 
                n == n_primefactor
            ]
        n_len_max = len(a_n_primefactor__same_in_n_2)
        if(
            len(a_n_primefactor__same_in_n_1)
             > len(a_n_primefactor__same_in_n_2)
        ):
            n_len_max = len(a_n_primefactor__same_in_n_1)
        
        # print("max {n_len_max}, pf {n_primefactor}")

        for n_i in range(0, n_len_max):
            a_n_primefactor_kgv.append(
                n_primefactor
            )
    # print(a_n_primefactor_kgv)
    print("---")
    print("f_a_n_primefactor__kgv("+str(n_1)+","+str(n_2)+")")

    print("kgV("+str(n_1)+","+str(n_2)+") = "+str(' * '.join([str(n) for n in a_n_primefactor_kgv])))
    n_product = f_n_product_from_array(a_n_primefactor_kgv)
    print("kgV("+str(n_1)+","+str(n_2)+") = "+str(n_product))

    return a_n_primefactor_kgv
def f_n_product_from_array(a_n):
    n_product = 1
    for n in a_n: 
        n_product = n_product * n
    return n_product
def f_assert(v1, v2):
    if(v1 != v2):
        print('assertion failed:')
        print("v1("+str(v1)+") == v2("+str(v2)+") equals false!")
    else: 
        print('assertion success:')
        print("v1("+str(v1)+") == v2("+str(v2)+") equals true!")




if len(sys.argv) > 2:
    n_1 = int(sys.argv[1])
    n_2 = int(sys.argv[2])

    a_n_primefactor_kgv = f_a_n_primefactor__kgv(
        n_1, 
        n_2
    )

if(len(sys.argv) >= 2):
    if(sys.argv[1] == "test"):
        f_assert(
            180,
            f_n_product_from_array(
                f_a_n_primefactor__kgv(36,90)
            )
        )
        f_assert(
            24,
            f_n_product_from_array(
                f_a_n_primefactor__kgv(12,8)
            )
        )

def f(
    n_a, 
    n_b
): 
    return f_a_n_primefactor__kgv(n_a, n_b)

print("------")
print("usage:")
print("f(123, 233)")
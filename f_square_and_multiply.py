import sys
import math

def f(
    n_a, 
    n_b
): 
    return f_square_and_multiply(n_a, n_b)

def f_s_dec_as_binary(n_dec, s_separator = '_', s_nibblefiller = ' '):
    n_exp = 0
    n_b = 2
    s = ''
    n_term = n_b**n_exp
    while(n_term <= n_dec):
        if(n_dec & n_term):
            s = '1'+s
        else:
            s = '0'+s
        if((n_exp+1) % 4 == 0):
            s = s_separator+s
        n_exp+=1
        n_term = n_b**n_exp

    a_s = [s_nibblefiller for n in range(0,4-(((n_exp-1)%4)+1))]
    s = "".join(a_s)+s

    return s
def f_square_and_multiply(n_basis, n_exponent):
    print("exponent ("+str(n_exponent)+") as binary:")
    print("0d "+str(n_exponent)+" = 0b "+f_s_dec_as_binary(n_exponent)) 
    s_exponent_as_binary = f_s_dec_as_binary(n_exponent, '', '')
    print(s_exponent_as_binary)

    n_exp = 0
    n_prod = 1
    n_index = 0
    n_muls = 0
    while(n_index < len(s_exponent_as_binary)):
        s = s_exponent_as_binary[n_index]
        print("--------------")
        print("bit position: ")
        print(''.join([(s if n == n_index else "x") for n in range(0, len(s_exponent_as_binary))]))
        if(n_index > 0):
            n_prod = n_prod ** 2
            print("n_prod = n_prod ** 2")
            print("n_prod = "+str(n_prod)+" ** 2")
            n_muls+=1
        if(s == '1'):
            n_prod = n_prod * n_basis
            print("n_prod = n_prod * n_basis")
            print("n_prod = "+str(n_prod)+" * "+ str(n_basis))
            n_muls+=1

        n_index += 1


    print("--------------")
    print(str(n_basis)+"^"+str(n_exponent)+" = "+str(n_prod))
    print("amount of multiplication steps: "+str(n_muls))


    return n_prod

if len(sys.argv) > 2:
    n_1 = sys.argv[1]
    n_2 = sys.argv[2]
    f(int(n_1), int(n_2))


print("usage:")
print("2^4234")
print("f(2,4234)")
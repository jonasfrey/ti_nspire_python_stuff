import sys
import math
import random

# -- diophantic equation

n_index__a = 0
n_index__b = 1
n_index__q = 2
n_index__r = 3
n_index__x = 4
n_index__y = 5
a_a_s_column_name = ['a', 'b', 'q', 'r', 'x', 'y']
def f_s_pdl(
    var,
    n_pad = 0, 
    s_pad = ' '
): 
    n_pad = n_pad - len(str(var))
    if(n_pad > 0):
        return ''.join([s_pad]*n_pad) + str(var)
    
    return str(var)
# test padding function
# print(f_s_pdl(2, 10, 'x'))

def f_s_table(a_a_n__table):
    s = ''
    # s = "\n".join([str("|".join([str(n) for n in a_n])) for a_n in a_a_n__table])
    n_index_row = 0
    for a_a_n in a_a_n__table: 
        n_index = 0
        a_s = []
        a_s__row_title = []
        a_s__row_divisor = []
        for n in a_a_n:
            n_pad = 5

            if(
                n_index == n_index__q
                or 
                n_index == n_index__x
                or
                n_index == n_index__y
                ):
                n_pad = 3

            a_s.append(f_s_pdl(str(n), n_pad, ' '))

            if n_index_row == 0:           
                a_s__row_title.append(f_s_pdl(a_a_s_column_name[n_index], n_pad, ' '))
                a_s__row_divisor.append(f_s_pdl('-', n_pad, '-'))
            n_index+=1

        if n_index_row == 0:           
            s+="|".join(a_s__row_title)
            s+='\n'
            s+="|".join(a_s__row_divisor)
            s+='\n'

        s+="|".join(a_s)
        s+='\n'
        n_index_row+=1

    return s
n_ti_nspire_max_chars_per_line = 36



def f_a__solve_diophantic_equation(
    n_a, 
    n_b, 
    n_3
):
    a_a_n__table = []
    n_bigger = max(n_a, n_b)
    n_smaller = min(n_a, n_b)
    b_swap_xy = False

    if(n_b > n_a):
        b_swap_xy = True

    n_last_rest = 0
    a_s_euclidean_algo = []
    while(True):
        n_rest  = (n_bigger - (math.floor(n_bigger/n_smaller) * n_smaller))
        n_factor = math.floor(n_bigger/n_smaller)

        a_s_euclidean_algo.append(f_s_pdl(n_bigger, 4, ' ')+" = "+f_s_pdl(n_factor, 4, ' ')+" * "+f_s_pdl(n_smaller, 4, ' ')+" + "+f_s_pdl(n_rest, 4, ' '))
        
        a_n = [0]*(n_index__y+1)
        a_n[n_index__a] = n_bigger
        a_n[n_index__b] = n_smaller
        a_n[n_index__q] = n_factor
        a_n[n_index__r] = n_rest
        a_a_n__table.append(a_n)

        if(n_rest == 0):
            break

        n_last_rest = n_rest
        n_bigger = n_smaller
        n_smaller = n_rest

    print("euclidean algo: ")
    print("\n".join(a_s_euclidean_algo))
    print(" ")
    n_ggt = n_last_rest
    s_ggt = "ggt("+str(n_a)+", "+str(n_b)+")"
    print(s_ggt+ " is: "+str(n_last_rest))
    n_mod_result = n_3 % n_last_rest
    if n_mod_result != 0:
        print("diophantic equation not possible because ")
        print(s_ggt +" is not teiler von "+str(n_3)+"!")
        print(""+str(n_3)+" mod "+ s_ggt +" = "+str(n_3) +" mod "+str(n_ggt)+" = "+str(n_mod_result))

    # s_table = f_s_table(a_a_n__table)
    # print(s_table)
    n_index = len(a_a_n__table)-1
    while(n_index >= 0):

        if(n_index == len(a_a_n__table)-1):
            # init values
            n_x = 0
            n_y = 1
        else: 
            n_y__last = a_a_n__table[n_index+1][n_index__y]
            n_x__last = a_a_n__table[n_index+1][n_index__x]
            n_q = a_a_n__table[n_index][n_index__q]
            n_x = n_y__last
            n_y = n_x__last - n_q * n_y__last

        a_a_n__table[n_index][n_index__x] = n_x
        a_a_n__table[n_index][n_index__y] = n_y
        
        n_index -=1

    s_table = f_s_table(a_a_n__table)

    n_x = a_a_n__table[0][n_index__x]
    n_y = a_a_n__table[0][n_index__y]
    if(b_swap_xy):
        n_xtmp = n_x
        n_x = n_y 
        n_y = n_xtmp
    
    # print("n_3 / n_ggt = n_factor")
    n_factor = n_3 / n_ggt
    # print(str(n_3)+"/"+str(n_ggt)+" = "+str(n_factor))
    
    print(str(n_x)+"*"+str(n_a)+"+"+str(n_y)+"*"+str(n_b)+"="+s_ggt)

    print(str(n_x)+"*"+str(n_factor)+"*"+str(n_a)+"+"+str(n_y)+"*"+str(n_factor)+"*"+str(n_b)+"="+s_ggt+"*"+str(n_factor))
    print(str(n_x*n_factor)+"*"+str(n_a)+"+"+str(n_y*n_factor)+"*"+str(n_b)+"="+str(n_ggt*n_factor))
    print()
    print(s_table)

    print(str())
    return a_a_n__table[0]
# -- end diophantic equation 

def f_n_en_or_de_crypted(
    n_msg,
    n_potenz, 
    n_mod
):  
    return (n_msg**n_potenz) % n_mod

def f_s__from_a_n(a_n):
    s = ''.join([chr(n) for n in a_n])
    return s

def f_a_n_encrypted__from_ascistring(
    n_e, 
    n_n,
    s_msg_ascii
):
    a_n_char = [ord(s) for s in s_msg_ascii]

    a_n_encrypted = [f_n_en_or_de_crypted(n, n_e, n_n) for n in a_n_char]

    print("encrypted string is")
    print(f_s__from_a_n(a_n_encrypted))

    return a_n_encrypted

def f_s_decrypted__from_a_n(
    n_d, 
    n_n,
    a_n_num_encrypted
):
    a_n_num_decrypted = [f_n_en_or_de_crypted(n, n_d, n_n) for n in a_n_num_encrypted]

    print("decrypted string is")
    s = f_s__from_a_n(a_n_num_decrypted)
    print(s)
    return s 

def f_n__calculate_public_key_e(
    n_d, 
    n_prime__p, 
    n_prime__q
): 
    n_n = n_prime__p * n_prime__q
    print("e * d = 1 mod (p-1)*(q-1)")
    print("e * "+str(n_d)+ " = 1 mod ("+str(n_prime__p)+"-1)*("+str(n_prime__q)+"-1)")
    n_phi_of_n = (n_prime__p-1)*(n_prime__q-1)
    print("e * "+str(n_d)+ " = 1 mod ("+str((n_prime__p -1)* (n_prime__q-1))+"-1)")
    print("e * "+str(n_d)+ " = 1 mod ("+str(n_phi_of_n)+")")

    print("solve diophantic equation:")
    print("x*"+str(n_phi_of_n)+"+ y*"+str(n_d)+"= 1")
    a_diophantic_parts = f_a__solve_diophantic_equation(n_phi_of_n, n_d, 1)
    # print(a_diophantic_parts)
    print("the equal symbol with three lines is repseneted like this '==='")
    n_y = a_diophantic_parts[n_index__y]
    print("1 === "+str(n_y)+" * d mod phi(n)")
    print("1 === "+str(n_y)+" * "+str(n_d)+" mod phi(n)")
    print("1 === "+str(n_y)+" * "+str(n_d)+" mod "+str(n_phi_of_n))

    print("e = "+str(n_y)+" + "+str(n_phi_of_n))
    n_e = n_y + n_phi_of_n
    print("e = "+str(n_e))
    n_factor = 1
    while(n_e < 0):
        # kleinste positivie ladung noch nicht erreicht 
        print("e = "+str(n_y)+" + "+str(n_factor)+"*"+str(n_phi_of_n))
        n_e = n_y + n_factor * n_phi_of_n
        n_factor+=1
    print("kleinste positive ladung")
    print("e = "+str(n_y)+" + "+str(n_factor)+"*"+str(n_phi_of_n))
    n_e = n_y + n_factor * n_phi_of_n

    print("e = "+str(n_e))
    return n_e

def f_n_gget_euclidean_algo(
    n_a, 
    n_b
):
    n_bigger = max(n_a, n_b)
    n_smaller = min(n_a, n_b)
    n_last_rest = 0
    while(True):
        n_rest  = (n_bigger - (math.floor(n_bigger/n_smaller) * n_smaller))
        n_factor = math.floor(n_bigger/n_smaller)

        # print(str(n_bigger)+" = "+str(n_factor)+" * "+str(n_smaller)+" + "+str(n_rest))
        if(n_rest == 0):
            break

        n_last_rest = n_rest
        n_bigger = n_smaller
        n_smaller = n_rest

    n_ggt = n_last_rest
    return n_ggt
    # print("ggt is: "+str(n_last_rest))


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

    print("step 1) generate two random high prime numbers: 'p' and 'q'")

    n_delta_primes = 10000
    n_min = 100
    n_max = 100000
    a_n_prime = f_a_n_prime(n_min, n_max)
    n_index_max = len(a_n_prime)-1
    n_nor = random.uniform(0, 1)
    n_prime__p = a_n_prime[int(n_nor*n_index_max)]

    n_min = n_min + n_delta_primes
    n_max = n_max + n_delta_primes
    a_n_prime = f_a_n_prime(n_min, n_max)
    n_index_max = len(a_n_prime)-1
    n_nor = random.uniform(0, 1)
    n_prime__q = a_n_prime[int(n_nor*n_index_max)]

    print("two random prime numbers are")
    print("p: "+str(n_prime__p))
    print("q: "+str(n_prime__q))


    print("step 2) n = p*q")
    n_prime_product_n = n_prime__p * n_prime__q
    print("n = "+ str(n_prime__p) +" * "+str(n_prime__q))
    print("n = "+ str(n_prime_product_n))

    print("step 3) generate a random high number, which is teilerfremd zu phi('n'), called 'd'")
    n_d_min = 100000
    n_d_factor = 100000
    n_ggt = 0
    n_phi_of_n = (n_prime__p-1)*(n_prime__q-1)
    print("phi(n) = (p-1)*(q-1)")
    print("phi(n) = "+str(n_phi_of_n))
    while(n_ggt != 1):
        n_d = int(random.uniform(0, 1) * n_d_factor + n_d_min)
        n_ggt = f_n_gget_euclidean_algo(n_d, n_phi_of_n)
    
    print("ggT(d, phi(n)) = "+str(n_ggt))
    print("'d': "+str(n_d))

    print("step 4) das multiplikative inverse called 'e' von 'd' bestimmen")
    n_e = f_n__calculate_public_key_e(n_d, n_prime__p, n_prime__q)



if len(sys.argv) > 2:
    n_1 = sys.argv[1]
    n_2 = sys.argv[2]
    #f(int(n_1), int(n_2))
    f()

# example
# f_n__calculate_public_key_e(35, 19, 23)
# f()
n_e__alice = 215 
n_d__alice = 35
n_n__alice = 437

n_e__bob = 15
n_d__bob = 47
n_n__bob = 391

a_n_encrypted = f_a_n_encrypted__from_ascistring(n_e__bob, n_n__bob, '{')
print(a_n_encrypted)

s = f_s_decrypted__from_a_n(n_d__bob, n_n__bob, a_n_encrypted)
print(s)
print("usage:")
print("---")
print("fe(...)")
print("calculate public key 'e', by using:")
def fe(
    n_d, 
    n_prime__p, 
    n_prime__q
):
    n_e = f_n__calculate_public_key_e(
        n_d, 
        n_prime__p, 
        n_prime__q
    )
    print("n_e = "+str(n_e))

print("fe(n_d, n_prime__p, n_prime__q)")
print("n_d = the secret key 'd' (given in the math task)")
print("n_prime__p = a prime number (given in the math task)")
print("n_prime__q = a prime number (given in the math task)")
print("so for example: fe(35, 19, 23)")

print("---")
print("fmen(n_e, n_n, n_msg): fmen = function message encrypted number")
print("fmdn(n_d, n_n, n_msg): fmdn = function message decrypted number")
print("n_e = given in the task, n_n = given in the task, n_msg given in the task, a number which represents the message")
print("fmen(15, 391, 65)")
def fmen(
    n_e,
    n_n,
    n_msg
):
    print("encryption is being done with:")
    print("n_msg_encrypted = [(n_msg ** n_n) mod n_e]")
    n_msg_encrypted = f_n_en_or_de_crypted(n_msg, n_e, n_n)
    print("n_msg_encrypted = "+str(n_msg_encrypted))
    return n_msg_encrypted
def fmdn(
    n_d,
    n_n,
    n_msg
):
    print("decryption is being done with:")
    print("n_msg_decrypted = [(n_msg ** n_n) mod n_d]")
    n_msg_decrypted = f_n_en_or_de_crypted(n_msg, n_e, n_n)
    print("n_msg_decrypted = "+str(n_msg_decrypted))
    return n_msg_decrypted

print("---")
print("fmes(n_e, n_n, n_msg): fmes = function message encrypted string")
print("fmds(n_e, n_n, n_msg): fmds = function message decrypted string")
print("n_e = given in the task, n_n = given in the task, s_msg a character/string of length 1")
print('fmes(15, 391, "a")')
def fmes(
    n_e,
    n_n,
    s_msg
):
    n_msg = ord(s_mgs)
    print("s_mgs ("+str(s_mgs)+") as a number equals to ("+str(n_msg)+")")
    return fmen(n_msg, n_e, n_n)

def fmds(
    n_d,
    n_n,
    s_msg
):
    n_msg = ord(s_mgs)
    print("s_mgs ("+str(s_mgs)+") as a number equals to ("+str(n_msg)+")")
    return fmdn(n_msg, n_d, n_n)

print("---")
print("fsrsah(): f string rsa help")

def fsrsah():
    print("---") 
    print("step 1)") 
    print("select 2 prime numbers (p and q)")
    p = 5
    q = 7 
    print("p = "+str(p))
    print("q = "+str(q))

    print("---") 
    print("step 2)")
    print("caluclate, n = p*q")
    n = p*q
    print("n = "+str(p)+"*"+str(q)+" = " + str(n))
    print("calculate phi(n), which is (p-1)*(q-1)")
    phi_of_n = (p-1)*(q-1)
    print("phi_of_n = ("+str(p)+"-1)*("+str(q)+"-1) = "+str(phi_of_n))
        
    print("---") 
    print("step 3)")
    print("select a number 'e' which satisfies:")
    print(" e < n")
    print("and")
    print(" e hat keinen gemeinsamen teiler mit phi(n)")
    print("zb. e = 11")
    e = 11
    
    print("---") 
    print("step 4)")
    print("select 'd' which satisfies:")
    print(" d != e ")
    print("and")
    print(" d*e = 1 mod (p-1)*(q-1)")
    print("and")
    print(" d hat keinen gemeinsamen teiler mit phi(n)")
    d = 59
    print("---") 
    print("(private information), keep secret!:")
    print("p("+str(p)+"), q("+str(q)+"), d("+str(d)+")")
    print("(public information), the partner needs this to encrypt and send you a message")
    print("e("+str(e)+")")

    print("---") 
    print("---")
    print("en-crypt a number)")
    m = 4
    print("m = "+str(m))
    print("get the public information 'n' and 'e' from the receipient")
    print("n = 35, e = 11")
    print("m_encrypted = m**e mod n")
    print("m_encrypted = "+str(m)+"**"+str(e)+" mod "+str(n)+"")
    m_encrypted = m**e % n
    print("m_encrypted = "+str(m_encrypted))


    print("---") 
    print("---")
    print("de-crypt a number)")
    print("m_encrypted = "+str(m_encrypted))
    print("the private information is:")
    print("d = "+str(d))

    print("m_decrypted = m_encrypted**d mod n")
    print("m_decrypted = "+str(m_encrypted)+"**"+str(d)+" mod "+str(n)+"")
    m_decrypted = m_encrypted**d % n
    print("m_decrypted ="+str(m_decrypted))

# fsrsah()


print("---")
print("fcrsa(n_n): f crack rsa")
print("try to crack the rsa by giving only the public 'n'")

def fcrsa(n_n):
    n_sqrt = math.sqrt(n_n)
    n_sqrt_ceil = math.ceil(n_sqrt)
    print("k = ceil(sqrt("+str(n_n)+")) = ceil("+str(n_sqrt)+") = "+str(n_sqrt_ceil)+"")
    n_k = n_sqrt_ceil
    print("sqrt((k+x)**2 - n) == integer number?")
    n_x = -1
    n_sqrt_n_kpn_x_p2m_n_n = 1.1
    while(n_sqrt_n_kpn_x_p2m_n_n.is_integer() == False):
        n_x += 1
        print("x = "+str(n_x))
        n_kpn_x = n_k + n_x
        n_kpn_x_p2 = n_kpn_x**2
        n_kpn_x_p2m_n_n = n_kpn_x_p2 - n_n
        n_sqrt_n_kpn_x_p2m_n_n = math.sqrt(n_kpn_x_p2m_n_n)
        print("sqrt((k+x)**2 - n) = sqrt(("+str(n_k)+"+"+str(n_x)+")**2 - "+str(n_n)+")")
        print("sqrt((k+x)**2 - n) = sqrt("+str(n_kpn_x)+" - "+str(n_n)+")")
        print("sqrt((k+x)**2 - n) = sqrt("+str(n_kpn_x_p2m_n_n)+")")
        print("sqrt((k+x)**2 - n) = "+str(n_sqrt_n_kpn_x_p2m_n_n))

    print("("+str(n_k+n_x)+"**2-"+str(n_sqrt_n_kpn_x_p2m_n_n)+"**2)")
    print("binomische formel:")
    print("("+str(n_k+n_x)+"-"+str(n_sqrt_n_kpn_x_p2m_n_n)+")*("+str(n_k+n_x)+"+"+str(n_sqrt_n_kpn_x_p2m_n_n)+")")
    n_p = n_k+n_x-n_sqrt_n_kpn_x_p2m_n_n
    n_q = n_k+n_x+n_sqrt_n_kpn_x_p2m_n_n
    print(str(n_k+n_x-n_sqrt_n_kpn_x_p2m_n_n)+"*"+str(n_k+n_x+n_sqrt_n_kpn_x_p2m_n_n))
    print("secret information 'p' and 'q' has been found")
    print("p = ("+str(n_k)+"+"+str(n_x)+"-"+str(n_sqrt_n_kpn_x_p2m_n_n)+") = "+str(n_p))
    print("q = ("+str(n_k)+"+"+str(n_x)+"+"+str(n_sqrt_n_kpn_x_p2m_n_n)+") = "+str(n_q))

# fcrsa(6089*93889)

import sys
import math

def f(
    n_a, 
    n_b, 
    n_c
): 
    return f_solve_diophantic_equation(n_a, n_b, n_c)

n_index__a = 0
n_index__b = 1
n_index__q = 2
n_index__r = 3
n_index__x = 4
n_index__y = 5
a_a_n__table = []
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



def f_solve_diophantic_equation(
    n_a, 
    n_b, 
    n_3
):
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
    
if len(sys.argv) > 2:
    n_1 = sys.argv[1]
    n_2 = sys.argv[2]
    n_3 = sys.argv[3]
    f_solve_diophantic_equation(int(n_1), int(n_2), int(n_3))

print("usage:")
print("example euqation:")
print("168*x + 238*y = 126")
print("pass the params like this:")
print("f(168, 238, 126)")
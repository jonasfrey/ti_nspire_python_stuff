import sys
import math
import random

def f_n_prod(a_n):
    n_prod = 1
    for n in a_n:
        n_prod *= n
    return n_prod
def f_n_factorial(n):
    return f_n_prod(range(1,n+1))


def f_permutation(
    a_n_val
):
    o_n_val_n_count = {}
    for n_val in a_n_val: 
        if((n_val in o_n_val_n_count) == False):
            n_count = len ([
                n2 
                for 
                n2 
                in a_n_val
                if n_val == n2
            ])
            o_n_val_n_count[n_val] = n_count
    print(o_n_val_n_count)
    n_len_a_n_val = len(a_n_val)
    a_s_factorial = [str(n)+"!" for n in o_n_val_n_count.values()]

    n_fact_n_len_a_n_val = f_n_factorial(n_len_a_n_val)
    a_n_fact_counts = [f_n_factorial(n) for n in o_n_val_n_count.values()]
    n_prod = f_n_prod(a_n_fact_counts)
    n_res = n_len_a_n_val / n_prod
    print("("+str(n_len_a_n_val)+"!)/("+'*'.join(a_s_factorial)+")")
    print("("+str(n_len_a_n_val)+"!)/("+'*'.join([str(n) for n in a_n_fact_counts])+") = "+str(n_res))
    

def f_permutation_or_variation(
    a_n_element, 
    n_plaetze = None
):

    if(n_plaetze == len(a_n_element) or n_plaetze == None):
        return f_permutation(a_n_element)


if len(sys.argv) > 2:
    n_1 = sys.argv[1]
    n_2 = sys.argv[2]
    #f(int(n_1), int(n_2))
    f()

def f(
): 
    return f_permutation_or_variation()


print("usage:")
print("---")
print("for example , how many possible different solutions are there for"), 
print("1 = black ball, 2 = red ball, 3 = green ball")
print("f([1,2,3,1])")

print(f_n_factorial(6))
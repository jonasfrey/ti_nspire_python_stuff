import sys
import math

def f(
    n_a, 
    n_b
): 
    return f_n_gget_euclidean_algo(n_a, n_b)

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

        print(str(n_bigger)+" = "+str(n_factor)+" * "+str(n_smaller)+" + "+str(n_rest))
        if(n_rest == 0):
            break

        n_last_rest = n_rest
        n_bigger = n_smaller
        n_smaller = n_rest

    print("ggt is: "+str(n_last_rest))

if len(sys.argv) > 2:
    n_1 = sys.argv[1]
    n_2 = sys.argv[2]
    f_n_gget_euclidean_algo(int(n_1), int(n_2))

print("usage:")
print("f(123,432)")
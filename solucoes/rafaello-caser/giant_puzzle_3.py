""" Giant Sudoku """

# comecei pela linha 127/877 pois são os maiores divisores:

a = 127
b = 877
inf_a = 100000000 // a
sup_a = 1000000000 // a + 1
inf_b = 100000000 // b
sup_b = 1000000000 // b + 1

La = [str(a * i) for i in range(inf_a, sup_a+1)]
La = [x for x in La if len(set(x)) == len(x) and len(x.replace('0', '')) == 9]
Lb = [str(b * i) for i in range(inf_b, sup_b+1)]
Lb = set([x[::-1] for x in La]).intersection(set(Lb))
La = [x[::-1] for x in Lb]

print(len(La))
print(La)
for i in range(9):
    print(set([x[i] for x in La]))

######################################################################
output:
5
['154863927', '168547923', '198476235', '658714329', '741629835']
{'6', '1', '7'}
{'6', '5', '4', '9'}
{'4', '8', '1'}
{'4', '8', '6', '7', '5'}
{'6', '2', '1', '4', '7'}
{'6', '3', '4', '7', '9'}
{'3', '2', '8', '9'}
{'2', '3'}
{'5', '3', '7', '9'}
######################################################################

""" Giant Sudoku """

a = 29
b = 79
inf_a = 100000000 // a
sup_a = 1000000000 // a + 1
inf_b = 100000000 // b
sup_b = 1000000000 // b + 1

La = [str(a * i) for i in range(inf_a, sup_a+1)]
La = [x for x in La if len(set(x)) == len(x) and len(x.replace('0', '')) == 9]
Lb = [str(b * i) for i in range(inf_b, sup_b+1)]
Lb = set([x[::-1] for x in La]).intersection(set(Lb))
La = [x[::-1] for x in Lb]
#### x[4] == '5' pois é cubo mágico; x[6], devido ao output da linha "127/877"
La = [x for x in La if x[4] == '5' and x[6] in ['3', '2', '8', '9']]

print(len(La))
print(La)
for i in range(9):
    print(set([x[i] for x in La]))

######################################################################
output:
4
['932157846', '273951864', '968357241', '127654839']
{'9', '1', '2'}
{'2', '3', '7', '6'}
{'2', '3', '7', '8'}
{'9', '3', '1', '6'}
{'5'}
{'4', '7', '1'}
{'2', '8'}
{'3', '4', '6'}
{'9', '4', '1', '6'}
######################################################################

# e assim por diante até a última linha que calculei via código, que foi a oitava horizontal (divisor 8):

""" Giant Sudoku """

a = 8
#b = 79
inf_a = 100000000 // a
sup_a = 1000000000 // a + 1
#inf_b = 100000000 // b
#sup_b = 1000000000 // b + 1

La = [str(a * i) for i in range(inf_a, sup_a+1)]
La = [x for x in La if len(set(x)) == len(x) and len(x.replace('0', '')) == 9]
#Lb = [str(b * i) for i in range(inf_b, sup_b+1)]
#Lb = set([x[::-1] for x in La]).intersection(set(Lb))
#La = [x[::-1] for x in Lb]
La = [x for x in La if x[0]=='4' and x[5]=='1' and x[6]=='3' and x[8] =='2']
La = [x for x in La if x[1] in ['7','9'] and x[2] in ['5','9'] and x[3] in ['5','6','7','9'] and x[4] in ['7','8'] and x[7] in ['6','9']]

print(len(La))
print(La)

######################################################################
output:
1
['475681392']
######################################################################

# Por fim, cálculo dos fatores primos da diagonal principal:

""" Fatores Primos """

import numpy as np

is_primo = lambda n: not any(n % i == 0 for i in range(2, n))

def menor_primo(n):
    for i in range(2, n + 1):
        if is_primo(i) and n % i == 0:
            return i

def fat_primos(n):
    primo = menor_primo(n)
    result = n // primo
    if result == 1:
        return [primo]
    return [primo, *fat_primos(result)]

n = 219456894
primos = fat_primos(n)
print(primos, np.prod(primos) == n)


######################################################################
output:
[2, 3, 61, 109, 5501] True
######################################################################
#!/bin/python3

# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING brackets as parameter.


def isBalanced(brackets):
    relation = {
        '}':'{',
        ')':'(',
        ']':'[',
    }
    inverted_brackets = ['}', ')', ']']
    stack = []
    for charactere in brackets:
        if charactere in inverted_brackets: # se o caractere for um caractere invertido
            if len(stack) == 0: # situação 1: a pilha está vazia, ou seja, a string está desbalanceada, pois, não tem um par
                return "NO"
            elif relation[charactere] == stack[-1]: # situação 2: o caractere é invertido, porém, tem um par, sendo assim, remove-os e continua
                stack.pop() # elimina o par da pilha
            else: # situação 3: se o caractere é invertido e não possui par, a string está desbalanceada
                return "NO"
        else:
            stack.append(charactere) # caso o caractere não seja invertido, o mesmo é adicionado na pilha até que encontre o seu par, se encontrar, a situação 2 é acionada
    return "YES"


if __name__ == '__main__':

    while True:
        try:
            t = int(input().strip())
        except ValueError:
            print(f"Valor de {t} não é um número. Tente novamente.")
        else:
            if t >= 1 and t <= 10:
                results = []
                for t_itr in range(t):
                    brackets = input()

                    results.append(isBalanced(brackets))

                print(*results, sep='\n')
                break
            else:
                print("Número incorreto. Tente novamente.")

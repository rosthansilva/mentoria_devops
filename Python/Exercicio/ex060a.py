print('Calculo fatorial usando o for')

n = int(input('Digite um numero a ser calculado: '))
f = 1
for c in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c

print(f)
i = 1

while i<=5:
    print('*' * i)
    i += 1

print()

for i in range(1, 5+1):
    print('* ' * i)


print()
n = 5 # number of rows
for i in range(1, n+1):
    for c in range(1, i + 1): # to work with columns
        print('* ', end='')
    print('')


print()
l = 2 * n - 2 # for the spaces
for i in range(0, n):
    for j in range(0, l):
        print(end=" ")
    l -= 2

    for o in range(0, i + 1):
        print('* ', end='')
    print()


print()
u = 2 * (n*2) - 2 # for the spaces
for i in range(n):
    for c in range(0, u): # to work with columns
        print(end=" ")

    u = u - 2

    for j in range(0, i+1):
        print('* ', end="")
    print()


print()
n = 5 # number of rows
for i in range(1, n+1):
    for c in range(1, i + 1): # to work with columns
        print('* ', end='')
    print('')

for t in range(n + 1, 1, -1):
    for c in range(1, t - 1):  # to work with columns
        print('*', end=' ')
    print(' ')


print()
for t in range(n + 1, 1, -1):
    for c in range(1, t - 1):  # to work with columns
        print('*', end=' ')
    print(' ')

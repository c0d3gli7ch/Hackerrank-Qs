def lonelyinteger(x):
    res = [p for p in x if x.count(p) == 1]
    [print(i) for i in res]

if __name__ == '__main__':
    x = []
    f = int(input('ENTER SIZE OF ARRAY : '))
    print(f'ENTER {f} ELEMENTS: ')
    for i in range(0,f):
        q = input()
        x.append(q)

    lonelyinteger(x)



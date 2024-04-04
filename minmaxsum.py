def minmaxsum(x):
    k = []
    i,z = 0,0
    while i < 5:
        print(x[i])
        z = sum(x)-x[i]
        k.append(z)
        i += 1
    res = '{} {}'.format(min(k),max(k))
    print(res)

if __name__ == '__main__':
    x = []
    print('ENTER 5 ELEMENTS IN ARRAY : ')
    for i in range(0,5):
        q = int(input())
        x.append(q)
    minmaxsum(x)

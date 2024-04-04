def flippingBits(x):
    for i in x:
        v = '{:032b}'.format(i)
        k = list(v)
        for j in range(0,32):
            if k[j] == '0':
                k[j] = '1'
            elif k[j] == '1':
                k[j] = '0'
            d = "".join(k)
        print(int(d,2))

if __name__ == '__main__':
    x = [] 
    f = int(input())
    # print(f'ENTER {f} QUERY INTEGERS: ')
    for i in range(0,f):
        q = int(input())
        x.append(q)
# print(x)
    flippingBits(x)

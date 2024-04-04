def plusmin(x):
    a,b,c=0,0,0
    for i in x:
        if i > 0:
            a=a+1
        elif i < 0:
            b=b+1
        elif i == 0:
            c=c+1
    print(a/f,'\n',b/f,'\n',c/f)

if __name__ == '__main__':
    x = []
    f = int(input('ENTER SIZE OF ARRAY : '))
    print(f'ENTER {f} ELEMENTS'.format(f))
    for i in range(0,f):
        q = int(input())
        x.append(q)
    print(x)
    plusmin(x)

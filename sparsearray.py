def matchstring(strings,queries):
    res = [strings.count(p) for p in list(queries)]
    for i in res:
        print(i)

if __name__ == '__main__':
    strings = []
    # f = int(input('ENTER THE SIZE OF THE ARRAY : '))
    f = int(input())
    # print(f'ENTER {f} ELEMENTS: ')
    for i in range(0,f):
        q = input()
        strings.append(q)
    queries = []
    # k = int(input('ENTER SIZE OF QUERY ARRAY : '))
    k = int(input())
    # print(f'ENTER {k} ELEMENTS: ')
    for i in range(0,k):
        v = input()
        queries.append(v)

    matchstring(strings, queries)



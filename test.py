def findMedian(arr):
    v = sorted(x)
    z = (len(v)-1) // 2
    print(v[z])

if __name__ == '__main__':
    x = []
    f = int(input())
    for i in range(0,f):
        q = int(input())
        x.append(q)

    findMedian(x)
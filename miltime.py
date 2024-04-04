def timeconv(s):
    if 'PM' in s:
        f = s.replace('PM', '')
        q = f.split(':')
        k = []
        for i in q:
            z = int(i)
            k.append(z)
        if k[0] < 12:
            k[0] = k[0] + 12
        print(':'.join(str(i).zfill(2) for i in k))
    else:
        f = s.replace('AM', '')
        q = f.split(':')
        k = []
        for i in q:
            z = int(i)
            k.append(z)
        if k[0] == 12:
            k[0] = 00
        print(':'.join(str(i).zfill(2) for i in k))

if __name__ == '__main__':

    s = input('ENTER TIME: ')
    timeconv(s)
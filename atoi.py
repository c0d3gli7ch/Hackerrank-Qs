import re
def atoi(s: str) -> int:
    s = s.strip()
    k = []
    if re.match(r'^[A-z]+', s):
        return 0

    for i in s:
        if i == '+' or i == '-':
            k.append(i)
    for i in s:
        if i.isdigit():
            k.append(i)
        if i == '.':
            break
    k = ''.join(k)
    print(k)
    if k == '':
        k = 0
    k = int(k)
    if k < (-2 ** 31):
        k = -2 ** 31
    return k

print(atoi("+-12"))


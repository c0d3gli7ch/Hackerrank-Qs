import snoop
@snoop
def med(n1: list[int], n2: list[int]) -> float:
    z = n1 + n2
    if len(z) % 2 != 0:
        output = int((len(z) + 1) / 2)
        output = float(z[output])
        return output

    else:
        a = int(len(z) / 2)
        b = int((len(z) / 2) + 1)
        output = float(z[a-1] + z[b-1]) / 2
        return output

print(med([2,3,4], [4,5,6]))



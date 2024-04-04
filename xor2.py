x = int(input())
c = 0
# for i in range(0,x+1):
#     if x + i == x ^ i:
#         c += 1
print(len([c+1 for i in range(0,x+1) if x + i == x^i]))

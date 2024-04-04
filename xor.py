x = list(input())
y = list(input())
for i in range(len(x)):
    if x[i] == y[i]:
        print(0,end='')
    else:
        print(1,end='')

# def strings_xor(s, t):
#     res = ""
#     for i in range(len(s)):
#         if s[i] == t[i]:
#             res += '0';
#         else:
#             res += '1';

#     return res

# s = input()
# t = input()
# print(strings_xor(s, t))


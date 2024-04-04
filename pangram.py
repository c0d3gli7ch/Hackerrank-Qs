import string
def pangram(x):
    x = x.replace(' ', '')
    x = list(x)
    z = list(string.ascii_letters[:26])
    res = all(i in x for i in z)
    if res is True:
        print('pangram')
    else:
        print('not pangram')
if __name__ == '__main__':
    x = input().lower()
    pangram(x)
    
def pageCount(n, p):
    k = 1
    if p == 1:
        return 0
    if abs(n - p) >= 1:        
        if abs(k - p) < abs(n - p):
            ans = int(math.ceil(((p - k) - 0) / 2))
            # if ans == 0:
            #     ans += 1
            #     return ans
            # else:
            #     return ans
            return ans
        else:
            ans = int(math.ceil(((n - p) - 1) / 2))
            if (n % 2 == 0) & (ans == 0):
                ans += 1
                return ans
            else:
                return ans
            # return ans
    else:
        return 0


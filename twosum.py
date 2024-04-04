
# def twosum(nums: list[int], target: int) -> list[int]:
#     for i in range(0, len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return i,j

# x = [5,1,6,2,4,9]
# target = 8

# print(twosum(x,target))

def twosum(l1: list[int], l2: list[int]) -> list[int]:
    a = ''
    b = ''
    for i in l1:
        a += str(i)
    
    for i in l2:
        b += str(i)
    
    a = a[::-1]
    b = b[::-1]
    c = int(a) + int(b)
    c = str(c)
    c = c[::-1]
    c = [int(i) for i in str(c)]
    return c

x = [9,9,9,9,9,9,9]
y = [9,9,9,9]
print(twosum(x,y))
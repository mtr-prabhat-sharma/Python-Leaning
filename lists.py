# a = []
# b = list((1,2,3,4))
# c = [11,22,33,44] 

# # print(a)
# # print(b)
# c[2] = 900
# c.append(1000)
# #c.insert(1,222)
# c.extend([8,9])
# print(c)

# nums = [2,4,6,8,10]
# #nums.remove(10)
# nums.pop()
# nums.pop(1)
# nums.clear()
# print(nums)


# d = [4,7,1,2,5]
# d.sort()
# d.reverse()
# print(d)

# e = [7,3,9,1]
# #f = e                                          #shalow copy / reference copy
# g = e.copy()                                    #deep copy
# #f[1] = 33
# #print(f)
# g[1] = 444
# print(g)
# print(e)

#looping
nums = [5,6,7,8,9]
print(len(nums))
for item in nums:
    print(item*item)

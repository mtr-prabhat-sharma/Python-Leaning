# nums = [1, 2, 2, 3, 4, 4, 5]

# new_nums = list(set(nums))

# print(new_nums)


nums1 = [1, 2, 2, 3, 4, 4, 5, 3]

res = []

for num in nums1:
    if num not in res:
        res.append(num)
print(res)
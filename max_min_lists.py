nums = [45, 12, 89, 23]

max = nums[0]
min = nums[0]

for num in nums:
    if num > max:
        max = num
    elif num < min:
        min = num
print("max = ", max)
print("min = ", min)
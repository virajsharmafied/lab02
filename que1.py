n = int(input("how many numbers: "))
nums = []
for _ in range(n):
    num = int(input("enter a number: "))
    nums.append(num)

print("Original list:", nums)
print("\nUsing built-in functions:")
max_num = max(nums)
min_num = min(nums)
print("Max:", max_num)
print("Min:", min_num)
sorted_nums = sorted(nums)
print("Sorted list:", sorted_nums)
unique_nums = list(set(nums))
print("List without duplicates:", unique_nums)
print("\nWithout using built-in functions:")
max_num = nums[0]
min_num = nums[0]
for num in nums:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
print("Max:", max_num)
print("Min:", min_num)
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
print("Sorted list:", nums)

unique_nums = []
for num in nums:
    if num not in unique_nums:
        unique_nums.append(num)
print("List without duplicates:", unique_nums)
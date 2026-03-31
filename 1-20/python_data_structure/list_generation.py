#强烈建议用生成式语法来创建列表


'''
创建一个取值范围在1到99且能被3或者5整除的数字构成的列表。
items = []
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        items.append(i)
print(items)
'''
items = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print(items)



'''
有一个整数列表nums1，
创建一个新的列表nums2，
nums2中的元素是nums1中对应元素的平方。
nums1 = [35, 12, 97, 64, 55]
nums2 = []
for num in nums1:
    nums2.append(num ** 2)
print(nums2)
'''
nums1 = [35, 12, 97, 64, 55]
nums2 = [num ** 2 for num in nums1]
print(nums2)



'''
有一个整数列表nums1，创建一个新的列表nums2，
将nums1中大于50的元素放到nums2中。
nums1 = [35, 12, 97, 64, 55]
nums2 = []
for num in nums1:
    if num > 50:
        nums2.append(num)
print(nums2)
'''
nums1 = [35, 12, 97, 64, 55]
nums2 = [num for num in nums1 if num > 50]
print(nums2)
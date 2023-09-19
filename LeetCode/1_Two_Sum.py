"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]
"""

# 暴力
def twoSum(nums,target):
    result = []
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                result.append(i)
                result.append(j)
                return result

# print(twoSum([2,7,11,15],9))
# print(twoSum([3,2,4],6))

# 哈希
def twoSum2(nums,target):
    result = []
    # 建立哈希表
    mapping = {}
    for i in range(0,len(nums)):
        mapping[nums[i]] = i
    # 遍历哈希表
    for j in range(0,len(nums)):
        diff = target - nums[j]
        if(diff in mapping and mapping[diff] != j):
            result.append(j)
            result.append(mapping[diff])
            return result


print(twoSum2([2,7,11,15],9))
print(twoSum2([3,2,4],6))
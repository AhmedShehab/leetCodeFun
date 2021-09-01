from math import floor


def searchInsert(nums, target):
    start = 0
    end = len(nums) - 1
    while end > start:
        index = floor((end + start) / 2)
        if nums[index] == target:
            return index
        elif nums[index] > target:
            end = index
        elif nums[index] < target:
            start = index + 1

    if end == start:
        if nums[end] == target:
            return end
        elif nums[end] > target:
            return end
        else:
            return end + 1


# Testing Data
nums1 = [1, 3]
target1 = 0
print(searchInsert(nums1, target1))

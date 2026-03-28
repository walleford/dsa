def binary_search(nums, target):
    left, right = 0, len(nums) -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1 # if the mid value is less than the target, the target has to be to the right.
        else: # if mid is bigger than target, tarrget has to be left of the mid point
            right = mid - 1
    return -1
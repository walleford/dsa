def search_insert_position(nums, target):
    # return index if target is found
    # if target not found, return the index where it 
    # should be. 
    # O(log n) -> binary search 
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    # left will be where it needs to be inserted at end
    return left

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        
        [5,7,7,8,8,10], target = 8
        
        mid = 8
        
        check if t == mid
        
        check left update if TRUE
        
        check right update if TURE
        '''
        
        def binarySearch(nums, target, leftBias):
            l, r = 0 ,len(nums)-1
            i = -1
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] == target:
                    i = mid
                    if leftBias:
                        r = mid - 1
                    else:
                        l = mid + 1

                elif nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
            return i
        l = binarySearch(nums, target, True)
        r = binarySearch(nums, target, False)
        return [l, r]
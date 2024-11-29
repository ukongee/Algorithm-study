def solution(nums):
    answer = 0
    length = len(nums) // 2
    nums = set(nums)
    answer = min(len(nums), length)
    return answer
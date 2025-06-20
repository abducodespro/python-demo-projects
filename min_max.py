def analyze_numbers(nums):
    if not nums:
        return None, None, []
    maxVal = max(nums)
    minval = min(nums)
    evens = [num for num in nums if num % 2 == 0]

    return maxVal, minval, evens

nums = [3,2,5,7,4,7,9,3]
maxVal, minval, evens = analyze_numbers(nums)

print(f"max value: {maxVal}")
print(f"min value: {minval}")
print(f"even numbers: {evens}")
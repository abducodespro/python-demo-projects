def sum_average(nums):
    total = sum(nums)
    avg = total / len(nums) if nums else 0
    return total, avg
nums = [2,4,5,6,7]
total, avg = sum_average(nums)

print(f"total: {total}")
print(f"average: {avg}")
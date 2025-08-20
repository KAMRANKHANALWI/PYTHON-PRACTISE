def findUniqueNumber(nums):
    # Your implementation here
    count_map = {}
    for num in nums:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1

    for num, freq in count_map.items():
        if freq == 1:
            return num


if __name__ == "__main__":
    nums = [2, 2, 1]
    result = findUniqueNumber(nums)
    print(result)

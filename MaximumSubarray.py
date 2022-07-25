def maximumSubarray(nums):
    sumsArray = []

    for x in range(len(nums)):
        sum += nums[x]
        sumsArray[x] = sum
    
    highestIndex = 0
    maxValue = max(sumsArray)

    for index, item in enumerate(sumsArray):
        if (item == maxValue):
            highestIndex = index

    sumsArrayTwo = []

    for y in range(len(nums)):
        sumTwo += nums[highestIndex - y]
        sumsArrayTwo[y] = sumTwo
    
    return max(sumsArrayTwo)

# wrongggg
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    output=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            tot = nums[i] + nums[j]
            print ('i = ' + str(i) + ', j = ' + str(j) + ' total = ' + str(tot))
            if tot == target:
                output.append(i)
                output.append(j)
    return output

print (twoSum([3,2,4],6))

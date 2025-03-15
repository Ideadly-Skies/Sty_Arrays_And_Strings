def five_sort(nums):
    """
    sort the number so that all five appears at the back of nums    
    """
    # define front and back pointer
    front = 0
    back = len(nums) - 1

    # make swap all the way until the back
    while front < back:
        if (nums[back] == 5):
            back -= 1
        elif (nums[front] == 5):
            nums[front], nums[back] = nums[back], nums[front]
            front += 1
        else:
            front += 1

    # return nums
    return nums 

print(five_sort([12, 5, 1, 5, 12, 7]))
print(five_sort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5]))
print(five_sort([5, 5, 5, 1, 1, 1, 4]))
print(five_sort([5, 5, 6, 5, 5, 5, 5]))
print(five_sort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5]))
fours = [4] * 20000
fives = [5] * 20000
nums = fours + fives
print(five_sort(nums))
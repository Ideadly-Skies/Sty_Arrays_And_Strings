def subarray_sum_count(numbers, target_sum):
    # counter to count the number of subarray
    counter = 0
    
    for i in range(len(numbers)):
        # set total temporarily to numbers[i] 
        total = numbers[i]

        # total is the sole element in the list 
        if total == target_sum:
            return True

        # sum up total with numbers[j]
        for j in range(i+1, len(numbers)):
            total += numbers[j]

            # sub-array found
            if total == target_sum:
                counter += 1 

    # sub-array not found
    return counter 
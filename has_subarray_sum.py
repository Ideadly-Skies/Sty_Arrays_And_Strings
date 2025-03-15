def has_subarray_sum(numbers, target_sum):
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
                return True

    # sub-array not found
    return False

if __name__ == "__main__":
    print(has_subarray_sum([1, 3, 1, 4, 3], 8)) # -> True
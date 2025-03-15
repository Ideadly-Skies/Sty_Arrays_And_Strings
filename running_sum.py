def running_sum(numbers):
    if not numbers:
        return [] 
    
    running_sum = numbers[0] 
    for i in range(1, len(numbers)):
        running_sum += numbers[i]
        numbers[i] = running_sum

    return numbers
def compress(s):
    """
    i represent the start of a char streak.
    j represent the pointer that increments forward
    until it encounter a different character. 
    """
    # i and j point to the same characters 
    i = j = 0
    char_count = 1

    # variable to store compressed string
    compressed_str = "" 

    while i < len(s):
        print("i = {}, j = {}, char = {}, count = {}".format(i, j, s[i], char_count))

        # if j becomes out of bounds append the last character
        if j == len(s)-1:
            # add to compressed_str
            if (char_count) > 1:
                compressed_str += str(char_count) + s[i]
            else:
                compressed_str += s[i] 

            # add the last distinct character
            if s[j] != s[i]:
                compressed_str += s[j] 
            break;  

        elif s[j] != s[i]:
            # add to compressed_str
            if (char_count) > 1:
                compressed_str += str(char_count) + s[i]
            else:
                compressed_str += s[i]

            # reset i to j
            i = j

            # reset count
            char_count = 1
        else: 
            # increment j forward
            j += 1

            if (s[i] == s[j]):
                # increment char_count
                char_count += 1

    # return compressed_str
    return compressed_str

if __name__ == "__main__":
    print(compress('ccaaatsss'))
    print(compress('ssssbbz'))
    print(compress('ppoppppp'))
    print(compress('nnneeeeeeeeeeeezz'))
    print(compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'))
    print(compress('abcccaddda'))
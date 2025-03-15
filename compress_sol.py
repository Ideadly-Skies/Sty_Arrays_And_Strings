def compress(s):
    # set both pointer initially to 0 
    i = j = 0

    # var to store compressed output
    compressed_str = "" 

    while j < len(s):
        if s[j] != s[i]:
            # compute count as index difference
            count = j - i

            # update compressed_str
            if count > 1:
                compressed_str += str(count) + s[i]
            else:
                compressed_str += s[i]

            # append last unique string
            if (j == len(s)-1):
                compressed_str += s[j]  

            # update i to j
            i = j
        elif (s[j] == s[i] and (j+1) == len(s)):
            # compute count as index difference 
            count = (j+1) - i 
            
            # update compressed_str
            if count > 1:
                compressed_str += str(count) + s[i]
            else:
                compressed_str += s[i] 
        
        # increment counter j 
        j += 1

    # return compressed_str
    return compressed_str

if __name__ == "__main__":
    print(compress('ccaaatsss'))
    print(compress('ssssbbz'))
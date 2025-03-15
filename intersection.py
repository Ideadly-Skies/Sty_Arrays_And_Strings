# two pointers
def intersection(a, b):
    # sort both arrays
    a.sort()
    b.sort()

    # convert a into a dictionary
    a_dict = {k: 0 for k in a}

    # find intersection
    intersection_ls = []
    for num in b:
        if num in a_dict:
            intersection_ls.append(num)

    # return intersection
    return intersection_ls

if __name__ == "__main__":
    # print the intersection
    print(intersection([4,2,1,6], [3,6,9,2,10])) # -> [2,6]
    print(intersection([2,4,6], [4,2]))          # -> [2,6]
    print(intersection([4,2,1], [1,2,4,6]))      # -> [1,2,4]
    print(intersection([0,1,2], [10,11]))        # -> [1,2,4]
    a = [ i for i in range(0, 50000) ]
    b = [ i for i in range(0, 50000) ]
    print(intersection(a, b)) # -> [0,1,2,3,..., 49999]
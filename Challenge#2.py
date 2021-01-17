def FindIntersection(strArr):
    # splitting strings into arrays
    arr1 = strArr[0].split(", ")
    arr2 = strArr[1].split(", ")

    intersections = ""

    a = b = 0
    while a < len(arr1) and b < len(arr2):
        if int(arr1[a]) == int(arr2[b]):
            intersections += "{},".format(arr1[a])
            a += 1
            b += 1
        elif int(arr1[a]) > int(arr2[b]):
            b += 1
        else:
            a += 1

    if not intersections:
        return "false"

    return intersections[:-1]


# keep this function call here
print(FindIntersection(input()))
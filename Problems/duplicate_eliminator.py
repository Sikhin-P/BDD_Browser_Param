def duplicate_eliminator(array):
    unique_array = []
    i = 0
    for ar in array:
        i += 1
        if ar in array[i::]:
            continue
        unique_array.append(ar)
    return unique_array


print(duplicate_eliminator([1,1,1,2,4,5]))

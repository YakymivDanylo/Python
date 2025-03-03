def modified_array(arr):
    positive_set = {num for num in arr if num>0}

    for i in range(len(arr)):
        if arr[i]<0 and abs(arr[i]) in positive_set:
            arr[i] = -arr[i]

    return arr

arr = [-3, 1, 2, -2, 5, -5, 3, -7]
modified_arr = modified_array(arr)
print(modified_arr)
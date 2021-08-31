import math
arr = [5, 8, 3, 2, 0, 1]
global_new_arr = []
def selection_sort(arr):
    smallest_number = math.inf
    index = 0
    old_arr = arr
    tuple1 = ()
    for x in range(0, len(arr)):
        if x == len(arr)-1:
            continue
        elif arr[x] > arr[x+1]:
            if smallest_number > arr[x+1]:
                smallest_number = arr[x+1]
                index = x+1
        elif smallest_number > arr[x]:
                smallest_number = arr[x+1]
                index = x+1
        else:
            print('line19break')
            break
    print(index)
    print("small", smallest_number)
    # print('newarr', global_new_arr)
    old_arr.pop(index)
    global_new_arr.append(smallest_number)
    for x in range(0, (len(old_arr)-1)):
        print(tuple1)
        if len(old_arr) <= 2:
            print('newarr', global_new_arr)
            print('oldarr', old_arr)
            if old_arr[0] > old_arr[1]:
                global_new_arr.append(old_arr[1])
                global_new_arr.append(old_arr[0])
                tuple1 = global_new_arr
                return tuple1
            elif old_arr[1] > old_arr[0]:
                global_new_arr.append(old_arr[0])
                global_new_arr.append(old_arr[1])
                tuple1 = global_new_arr
                return tuple1
        if old_arr[x] > old_arr[x+1]:
            selection_sort(old_arr)
    return tuple1

print1 = selection_sort(arr)
print(print1)
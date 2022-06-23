# Implementing a selection sort algorithm that is sorting in descending order:

def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    return my_list

list = [4, 2, 6, 5, 1, 3]
print('Selection Sort')
print(list)
print(selection_sort(list))


# Implementing bubble sort algorithm that is sorting in descending order:

def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0,-1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list

list = [47, 12, 6, 5, 11, 3]
print('Bubble Sort')
print(list)
print(bubble_sort(list))


# Implement the insertion sort algorithm that is sorting in descending order:

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list

list = [41, 22, 6, 57, 0, 3]
print('Insertion Sort')
print(list)
print(insertion_sort((list)))


# Implement the merge sort algorithm that is sorting in descending order:


def merge_sort(list):
    if len(list) <= 1:
        return list
    middle = len(list) // 2
    return merge_lists(merge_sort(list[:middle]), merge_sort(list[middle:]))

def merge_lists(list1, list2):
    combined = []
    i = j = 0

    while i < len(list1) or j < len(list2):
        if i == len(list1):
            combined.append(list2[j])
            j += 1
            continue
        if j == len(list1):
            combined.append(list1[i])
            i += 1
            continue

        if list1[i] <= list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    return combined

ex_list = [11, 2, 77, 8, 3, 41, 50, 6]
print('Merge')
print(ex_list)
print(merge_sort(ex_list))

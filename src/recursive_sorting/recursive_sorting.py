# TO-DO: complete the helpe function below to merge 2 sorted arrays
# def merge(arrA, arrB):
#     elements = len(arrA) + len(arrB)
#     merged_arr = [0] * elements
#     # TO-DO

#     return merged_arr


# def merge(left, right, data):
#     mid_index = (len(data)//2)
#     left = data[:mid_index]
#     right = data[mid_index:]
#     i = 0
#     j = 0
#     k = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             data[k] = left[i]
#             i += 1
#         else:
#             data[k] = right[j]
#             j += 1
#         k += 1
#     while i < len(left):
#         data[k] = left[i]
#         i += 1
#         k += 1
#     while j < len(right):

#         data[k] = right[j]
#         j += 1
#         k += 1
#     return data


# merge([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])


# def merge_sort(data):
#     n = len(data)
#     if (n < 2):
#         return data
#     mid = n//2
#     left = data[:mid]
#     right = data[mid:]
#     for i in range(0, mid-1):
#         left[i] = data[i]
#     for i in range(mid, n-1):
#         right[i-mid] = data[i]
#     merge_sort(left)
#     merge_sort(right)
#     merge(left, right, data)

# # TO-DO: implement the Merge Sort function below USING RECURSION


# # def merge_sort(arr):
# #     # TO-DO

# #     return arr


# # STRETCH: implement an in-place merge sort algorithm
# # def merge_in_place(arr, start, mid, end):
# #     # TO-DO

# #     return arr


# def merge_sort_in_place(arr, l, r):
#     # TO-DO

#     return arr
def merge(arr, left, right):
	temp = None
	global temp
	mid = (left + right) // 2
	for i in range(left, right + 1):
		temp[i] = arr[i]
	k, L, R = left, left, mid + 1
    while L <= mid and R <= right:
        if temp[L] <= temp[R]:
            arr[k] = temp[L]
            L += 1
        else:
            arr[k] = temp[R]
            R += 1
        k += 1
    while L <= mid:
        arr[k] = temp[L]
        L += 1
        k += 1
    while R <= right:
        arr[k] = temp[R]
        R += 1
        k += 1


def merge_sort(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge(arr, left, right)


arr = [1, 6, 3, 1, 8, 4, 2, 9, 3, 4, 7, 3, 0]
merge_sort(arr, 0, len(arr) - 1)
print(arr)


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr

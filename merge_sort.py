import numpy as np

def generate_random_list():
    sampl = np.random.randint(100, size=10)
    print(sampl.tolist())
    return sampl.tolist()

def initiate_mergesort():
    random_list = generate_random_list()
    print("Sorted List", merge_sort(random_list))

def merge_sort(list):
    if len(list) == 1 :
        print("one element ", list)
        return list
    else:
        mid = len(list) // 2
        print("splitting ", list)
        left = merge_sort(list[:mid])
        right = merge_sort(list[mid:])
        print("merging", left, " and ", right)
        return merge(left, right)


def merge(left, right):
    sorted_list = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            sorted_list.append(left[0])
            left.remove(left[0])
        else:
            sorted_list.append(right[0])
            right.remove(right[0])

    if len(left) == 0:
        sorted_list += right
    else:
        sorted_list += left

    return sorted_list



initiate_mergesort()

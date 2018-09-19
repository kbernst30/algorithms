import random


def quick_sort(lst, low, high):
    if low < high:

        pivot_idx = random.randint(low, high)
        pivot = lst[pivot_idx]

        # Make pivot last element
        lst[pivot_idx], lst[high] = lst[high], lst[pivot_idx]

        c = low
        for i in range(low, high):
            if lst[i] <= pivot:
                lst[c], lst[i] = lst[i], lst[c]
                c += 1

        lst[c], lst[high] = lst[high], lst[c]

        quick_sort(lst, low, c - 1)
        quick_sort(lst, c + 1, high)


def bubble_sort(lst):

    did_swap = True

    while did_swap:
        did_swap = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                did_swap = True


if __name__ == '__main__':
    lst = []
    for i in range(20):
        lst.append(random.randint(-100, 101))

    print("QUICK SORT")
    print(lst)
    quick_sort(lst, 0, len(lst) - 1)
    print(lst)

    lst = []
    for i in range(20):
        lst.append(random.randint(-100, 101))

    print("BUBBLE SORT")
    print(lst)
    bubble_sort(lst)
    print(lst)

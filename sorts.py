def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    midpoint = int(len(lst) / 2)

    left_list = merge_sort(lst[0:midpoint])
    right_list = merge_sort(lst[midpoint:])

    output_list = []
    while len(left_list) > 0 or len(right_list) > 0:
        left_item = left_list[0] if len(left_list) > 0 else None
        right_item = right_list[0] if len(right_list) > 0 else None

        if left_item is not None and (right_item is None or left_item <= right_item):
            output_list.append(left_list.pop(0))
        elif right_item is not None and (left_item is None or right_item <= left_item):
            output_list.append(right_list.pop(0))

    return output_list

if __name__ == '__main__':
    l = [1,6,3,45,32,2,0,-5,22,11]

    print(l)
    l = merge_sort(l)
    print(l)

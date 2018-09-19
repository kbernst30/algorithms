def binary_search(lst, val):
    if len(lst) == 0:
        return False;
    elif len(lst) == 1:
        return lst[0] == val
    else:
        mid_point = int(len(lst) / 2)
        return binary_search(lst[0:mid_point], val) or binary_search(lst[mid_point:], 
val) 

if __name__ == '__main__':
    
    lst = [4,0,8,9,23,6,5,11,3]

    print(binary_search(lst, 5))
    print(binary_search(lst, 10))
    print(binary_search(lst, 1))
    print(binary_search(lst, 9))

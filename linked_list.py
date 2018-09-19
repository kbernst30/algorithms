class LinkedList(object):

    def __init__(self, val):
        self.val = val
        self.next = None

    def print(self):
        to_print = str(self.val)
        next = self.next
        while next:
            to_print += "->" + str(next.val)
            next = next.next

        print(to_print)


def reverse_linked_list(ll):

    ll_next = ll
    new_ll = None
    while ll_next:
        new_ll_next = new_ll
        new_ll = LinkedList(ll_next.val)
        new_ll.next = new_ll_next
        ll_next = ll_next.next

    return new_ll

if __name__ == '__main__':
    ll = LinkedList(0)

    next = ll
    for i in range(1, 10):
        next.next = LinkedList(i)
        next = next.next

    ll.print()
    reverse_linked_list(ll).print()

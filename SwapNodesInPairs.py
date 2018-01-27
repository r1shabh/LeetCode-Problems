__author__ = 'rishabh anand'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def printListNode(head):
    while head is not None:
        print head.val, " ",
        head = head.next
    print '\n'


def swapPairs(head):
    output = head
    current = head
    while current.next and current.next.next:
        temp = current.next
        current.next.val = current.val
        current.val = temp.val
        current = current.next.next
    return output


a = ListNode(2)
b = ListNode(3)
c = ListNode(5)
d = ListNode(6)
a.next = b
b.next = c
c.next = d
printListNode(a)
a = swapPairs(a)
printListNode(a)
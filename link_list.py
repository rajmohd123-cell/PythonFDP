class LLNode:
     def __init__(self, val, next=None):
        self.val = val
        self.next = next


def create_linked_list(nums):
# """ Assumes the list has atleast one element """
    head = LLNode(nums[0])
    tail = head
    for i in range(1, len(nums)):
        tail.next = LLNode(nums[i])
        tail = tail.next 
        return head


def print_in_reverse(head):
 # terminating condition
    if head == None:
        return
# # combining the sub-solutions
    print_in_reverse(head.next)
    print(head.val)


elements = [55, 44, 22]
ll = create_linked_list(elements)
# elements = None

print_in_reverse(ll)


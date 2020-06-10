class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def create_linked_list(nums):
 """ Assumes the list has atleast one element """
     head = LLNode(nums[0])
    current = head
        for i in range(1, len(nums)):
            new_node = LLNode(nums[i])
            current.next = new_node
            current = new_node
            return head




 def print_all_integers(head):
        while head != None:
            if type(head.val).__name__ == "int":
                print(head.val)
                head = head.next


def print_all_integers(head):
# # terminating condition
    if head == None:
        return
# breaking the problem into smaller sub-problems
# solving the first node and calling for the remaining problem
    if type(head.val).__name__ == "int":
        print(head.val)


elements = [55, 33, 22, 11]
ll = create_linked_list(elements)
class TNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_node(root, num):
    if num > root.val:
        # insert to the right sub-tree
        if (root.right != None): 
            insert_node(root.right, num)
        else: 
            root.right = TNode(num)
    else:
    # insert into the left sub-tree
        if (root.left != None):
            insert_node(root.left, num)
        else:
            root.left = TNode(num)


def create_tree(nums):
    root = TNode(nums[0])
    for i in range(1, len(nums)):
        insert_node(root, nums[i])
        return root


nums = [10, 5, 23, 11, 1, 15]

my_tree = create_tree(nums)


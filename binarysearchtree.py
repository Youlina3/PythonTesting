# Binary search tree (BST) is a binary tree where the value of each node is larger or equal to the values in all the nodes in that node's left subtree and is smaller than the values in all the nodes in that node's right subtree.

# Write a function that checks if a given binary search tree contains a given value.

# For example, for the following tree:

# n1 (Value: 1, Left: null, Right: null)
# n2 (Value: 2, Left: n1, Right: n3)
# n3 (Value: 3, Left: null, Right: null)
# Call to contains(n2, 3) should return True since a tree with root at n2 contains number 3.
import collections

# class BinarySearchTree:

#     Node = collections.namedtuple('Node', ['left', 'right', 'value']) #like struct
    
#     @staticmethod
#     def contains(root, value):
#         curr = root
#         while curr.left or curr.right :
#             if value == curr.value:
#                 return True
#             if value > curr.value:
#                 curr = curr.right
#             if value < curr.value:
#                 curr = curr.left
#         if value == curr.value:
#                 return True
#         return False

n1 = BinarySearchTree.Node(value=1, left=None, right=None)
n3 = BinarySearchTree.Node(value=3, left=None, right=None)
n2 = BinarySearchTree.Node(value=2, left=n1, right=n3)

print(BinarySearchTree.contains(n2, 3))


#Thoughts: 1. None: doesn't have attributes so always need to determine whether the object is "None" using 'while' or 'if'
#          2. elif: when comparing three cases for a same event in logic, it's better to use elif; In this situation, curr is updated when entering one case so in the second if, the value of curr is not what we expect

class BinarySearchTree:

    Node = collections.namedtuple('Node', ['left', 'right', 'value']) #like struct
    
    @staticmethod
    def contains(root, value):
        curr = root
        while curr: #while curr;idea:  compare curr and the node that we looking for
            if value == curr.value:
                return True
            elif value > curr.value: #elif 三种情况elif不要用三个if 因为curr更新了
                curr = curr.right
            elif value < curr.value:
                curr = curr.left
        return False


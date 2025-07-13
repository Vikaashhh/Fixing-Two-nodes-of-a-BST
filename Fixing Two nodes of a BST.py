'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def correctBST(self, root):
        # Variables ko self ke through define kiya hai taaki recursive function use kar sake
        self.first = None
        self.middle = None
        self.last = None
        self.prev = None

        # Inorder traversal se BST ke violation detect karenge
        def inorder(node):
            if not node:
                return

            # Left subtree pe jao
            inorder(node.left)

            # Current node ko prev ke sath compare karo
            if self.prev and node.data < self.prev.data:
                # Violation mila
                if not self.first:
                    self.first = self.prev
                    self.middle = node
                else:
                    self.last = node

            # Prev ko update karo
            self.prev = node

            # Right subtree pe jao
            inorder(node.right)

        # Inorder traversal call karo
        inorder(root)

        # Ab nodes ko swap karo
        if self.first and self.last:
            self.first.data, self.last.data = self.last.data, self.first.data
        elif self.first and self.middle:
            self.first.data, self.middle.data = self.middle.data, self.first.data

        return root

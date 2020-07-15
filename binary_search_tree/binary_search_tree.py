"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.

* Should have the methods `insert`, `contains`, `get_max`.
  * `insert` adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.
  * `contains` searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.
  * `get_max` returns the maximum value in the binary search tree.
  * `for_each` performs a traversal of _every_ node in the tree, executing the passed-in callback function on each tree node value.
     There is a myriad of ways to perform tree traversal; in this case any of them should work. 
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Instantiate new_node w/ value
        new_node = BSTNode(value=value)
        # If value is less than root value
        if self.value > value:
            # If self.left doesn't exist make, set it to the new node
            if self.left is None:
                self.left = new_node
                return
            # Else, use recursion on self.left
            else:
                self.left.insert(value)
        # If value is greater than root value
        else:
            # If self.right doesn't exist make, set it to the new node
            if self.right is None:
                self.right = new_node
                return
            # Else, use recursion on self.right
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: self.value equals target
        if self.value == target:
            return True
        # Case 2: self.value is greater than target
        if self.value > target:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # Case 3: self.value is less than target
        if self.value < target:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        current = self
        if current is None:
            return 0
        while current is not None:
            max_val = current.value
            current = current.right
        return max_val

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        self.value = fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

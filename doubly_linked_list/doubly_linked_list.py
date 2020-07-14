"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_head = ListNode(value=value, next=self.head)
        if self.head == None:
            self.head = new_head
            self.tail = new_head
            self.length += 1
            return None
        self.head.prev = new_head
        self.head = new_head
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head == None:
            return None
        temp = self.head.value
        if (self.head is self.tail) or (self.head.next == None):
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        new_head = self.head.next
        new_head.prev = None
        self.head = new_head
        self.length -= 1

        return temp
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_tail = ListNode(value=value, prev=self.tail)
        if (self.head == None):
            self.head = new_tail
            self.tail = new_tail
            self.length += 1
            return None
        self.tail.next = new_tail
        self.tail = new_tail
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail is None:
            return None
        temp = self.tail.value
        if self.tail is self.head:
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        new_tail = self.tail.prev
        new_tail.next = None
        self.tail = new_tail
        self.length -= 1

        return temp
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.head is node:
            return None
        if self.length >= 2:
            current = self.head.next
            while current is not node:
                current = current.next
            # Connect the two nodes around the inputted node
            if node is not self.head:
                current.prev.next = current.next
            if node is not self.tail:
                current.next.prev = current.prev
            if node is self.tail:
                self.remove_from_tail()
                self.length += 1
            # Make the current node the new head
            node.next = self.head
            self.head.prev = node
            self.head = node
        return None
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.tail is node:
            return None
        if self.length >= 2:
            current = self.head
            while current is not node:
                current = current.next
            # Connect the two nodes around the input node
            if node is not self.head:
                current.prev.next = current.next
            if node is not self.tail:
                current.next.prev = current.prev
            if node is self.head:
                self.remove_from_head()
                self.length += 1
            # Make the current node the new tail
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        return None

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head is self.tail:
            self.head = None
            self.tail = None
            self.length = 0
            return None
        if node is self.head:
            self.remove_from_head()
            return None
        if node is self.tail:
            self.remove_from_tail()
            return None
        if self.length != 0:
            current = self.head
            while current is not node:
                current = current.next
                if current is node:
                    # Connect the two nodes around the inputted node
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.length -= 1
                    # Don't have to do explicit garbage collection in Python
        return None

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.value
        # reference to our current node as we traverse the list
        current = self.head.next
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.value > max_value:
                # if so, update our max_value variable
                max_value = current.value
            # update the current node to the next node in the list
            current = current.next
        return max_value
class Deque:
    
    def __init__(self):
        self.items = []

    def add_front(self, item):
        """Takes in an item and inserts that item into the 0th index of the list
        that is representing the Deque.
        
        The runtime is O(n), or linear time, because inserting into the 0th index
        of a list forces the other items in the list to move one index to the right.
        """

        self.items.insert(0, item)

    def add_rear(self, item):
        """Accepts an item as parameter and appends it to the end of the list.
        Returns nothing.

        The runtime for this method is O(1) or constant time, because appending
        to the end of a list happens in constant time.
        """

        self.items.append(item)

    def remove_front(self):
        """Removes and returns the item in the 0th index of the list, which 
        represents the front of the Dequq.

        The runtime is linear, O(n), because when we remove an item from the
        0th index, all the other items have to shift one index to the left.
        
        """

        if self.items:
            return self.items.pop(0)
        return None

    def remove_rear(self):
        """Removes and returns the last item of the list, which represents the
        rear of the Dequq.

        The runtime is constant because all we are doing is indexing to the end
        of the list.
        """

        if self.items:
            return self.items.pop()
        return None

    def peek_front(self):
        """Returns the 0th index item of the list, which represents the
        front of the Dequq.

        The runtime is constant because all we are doing is indexing to the front
        of the list.
        """

        if self.items:
            return self.items[0]
        return None

    def peek_rear(self):
        """Returns the last item of the list, which represents the
        rear of the Dequq.

        The runtime is constant because all we are doing is indexing to the end
        of the list.
        """

        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """Returns the size of the list that is representing the Deque.

        The runtime here is contant time, because finding the size of list happens
        in constant time.
        """

        return len(self.items)

    def is_empty(self):
        """Returns if the Deque is empty or not.

        The runtime here is contant time, because testing for equality happens in constant time.
        """

        return self.items == []
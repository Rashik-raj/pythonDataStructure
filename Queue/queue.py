class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Takes in an item and inserts that item into the 0th index of the list
        that is representing the Queue.
        
        The runtime is O(n), or linear time, because inserting into the 0th index
        of a list forces the other items in the list to move one index to the right.
        """

        self.items.insert(0, item)

    def dequeue(self):
        """Returns and removes the front-most item of the Queue, which is representesd
        by the last item in the list.

        The runtime is O(1), or constant time, because indexing to the end of a
        list happens in constant time.
        
        """

        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """Returns the front-most item of the Queue, which is representesd
        by the last item in the list.

        The runtime is O(1), or constant time, because indexing to the end of a
        list happens in constant time.
        
        """

        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """Returns the size of the list that is representing the Queue.

        The runtime here is contant time, because finding the size of list happens
        in constant time.
        """

        return len(self.items)

    def is_empty(self):
        """Returns if the Queue is empty or not.

        The runtime here is contant time, because testing for equality happens in constant time.
        """

        return self.items == []
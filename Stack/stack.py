class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        """Accepts an item as aparameter and appends it to the end of the list.
        Returns nothing.

        The runtime for this method is O(1) or constant time, because appending
        to the end of a list happens in constant time.
        """

        self.items.append(item)

    def pop(self):
        """Removes and returns the last item from the list, which is also the
        top item of the Stack.

        The runtime here is contant time, because all it does is index to the
        last item of the list.
        """

        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """Returns the last item from the list, which is also the
        top item of the Stack.

        The runtime here is contant time, because all it does is index to the
        last item of the list.
        """

        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """Returns the size of the list that is representing the Stack.

        The runtime here is contant time, because finding the size of list happens
        in constant time.
        """

        return len(self.items)

    def is_empty(self):
        """Returns if the Stack is empty or not.

        The runtime here is contant time, because testing for equality happens in constant time.
        """

        return self.items == []
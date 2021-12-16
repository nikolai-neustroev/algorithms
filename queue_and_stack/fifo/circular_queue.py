class MyCircularQueue:
    def __init__(self, k: int):
        """Initializes the object with the size of the queue to be k."""
        self.data = [0] * k
        self.maxSize = k
        self.head = 0
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        """Inserts an element into the circular queue. 
        Return true if the operation is successful."""
        if self.isFull(): 
            return False
        self.tail = (self.tail + 1) % self.maxSize
        self.data[self.tail] = value
        return True

    def deQueue(self) -> bool:
        """Deletes an element from the circular queue. 
        Return true if the operation is successful."""
        if self.isEmpty(): 
            return False
        if self.head == self.tail: 
            self.head, self.tail = 0, -1
        else: 
            self.head = (self.head + 1) % self.maxSize
        return True

    def Front(self) -> int:
        """Gets the front item from the queue. 
        If the queue is empty, return -1."""
        return -1 if self.isEmpty() else self.data[self.head]

    def Rear(self) -> int:
        """Gets the last item from the queue. 
        If the queue is empty, return -1."""
        return -1 if self.isEmpty() else self.data[self.tail]

    def isEmpty(self) -> bool:
        """Checks whether the circular queue is empty or not."""
        return self.tail == -1

    def isFull(self) -> bool:
        """Checks whether the circular queue is full or not."""
        return not self.isEmpty() and (self.tail + 1) % self.maxSize == self.head


if __name__ == "__main__":
    from pprint import pprint
    my_circular_queue = MyCircularQueue(3)
    pprint(vars(my_circular_queue))
    assert my_circular_queue.enQueue(1) is True
    pprint(vars(my_circular_queue))
    assert my_circular_queue.enQueue(2) is True
    pprint(vars(my_circular_queue))
    assert my_circular_queue.enQueue(3) is True
    pprint(vars(my_circular_queue))
    assert my_circular_queue.enQueue(4) is False
    assert my_circular_queue.Rear() == 3
    assert my_circular_queue.isFull() is True
    assert my_circular_queue.deQueue() is True
    assert my_circular_queue.enQueue(4) is True
    assert my_circular_queue.Rear() == 4

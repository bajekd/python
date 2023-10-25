class MaxHeap:
    def __init__(self, items=[]):
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__float_up(len(self.heap)-1)

    def __swap(self, index_1, index_2):
        # it
        self.heap[index_1], self.heap[index_2] = self.heap[index_2], self.heap[index_1]
        # works, see variable expansion mechanism

    def __float_up(self, index):
        index_of_parent_node = index // 2

        if index <= 1:
            return
        elif self.heap[index] > self.heap[index_of_parent_node]:
            self.__swap(index, index_of_parent_node)
            self.__float_up(index_of_parent_node)

    def __bubble_down(self, index):
        index_of_left_child_node = index * 2
        index_of_right_child_node = (index * 2) + 1
        index_of_largest_value = index

        if len(self.heap) > index_of_left_child_node and \
           self.heap[index_of_largest_value] < self.heap[index_of_left_child_node]:
            index_of_largest_value = index_of_left_child_node

        if len(self.heap) > index_of_right_child_node and \
           self.heap[index_of_largest_value] < self.heap[index_of_right_child_node]:
            index_of_largest_value = index_of_right_child_node

        if index_of_largest_value != index:
            self.__swap(index, index_of_largest_value)
            self.__bubble_down(index_of_largest_value)

    def push(self, data):
        self.heap.append(data)
        self.__float_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap)-1)
            max_value = self.heap.pop()
            self.__bubble_down(1)

        elif len(self.heap) == 2:
            max_value = self.heap.pop()
            self.__bubble_down(1)
        else:
            raise AttributeError("Heap is empty!")

        return max_value

    def peek(self):
        """Return largest value from heap (value with index = 1"""
        if self.heap[1]:
            return self.heap[1]
        else:
            raise AttributeError("Heap is empty!")

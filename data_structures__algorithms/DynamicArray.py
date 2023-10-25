class DynamicArray:
    """Simulating behavior of dynamic array"""

    def __init__(self, capacity=1):
        """Create dynamic array of given capacity

        Args:
            capacity (int, optional): actual size of initializing array . Defaults to 1.

        Raises:
            TypeError: Given capacity need to be positive integer
        """
        try:  # isinstance(capacity, int) and capacity > 0:
            self.capacity = capacity
            self.len = 0  # count number of elements (None is not count)
            self.arr = [None] * self.capacity
        except:
            raise TypeError(
                "Capacity of array need to be: 1) a number 2) greater than 0"
            )

    def __len__(self):
        """Return length of DynamicArray"""
        return self.len

    def __getitem__(self, index):
        """Return item with given index from DynamicArray"""
        self._is_out_of_index(index)
        return self.arr[index]

    def _resize(self):
        """Auxiliary function - create new DynamicArray with 2x more capacity, and rewrite old one"""
        self.capacity *= 2
        new_arr = [None] * self.capacity
        for i in range(self.len):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def _is_out_of_index(self, index):
        """Auxiliary function - check if given index is not out of DynamicArray capacity. If it is raise
        IndexError, if not just pass"""
        if isinstance(index, int):
            if index < 0 or (index >= self.capacity):
                raise IndexError("Out of array index!")
        else:
            raise IndexError("Given argument is not a number!")

    def clear(self):
        """Clear all values from DynamicArray"""
        for i in range(self.capacity):
            self.arr[i] = None
        self.len = 0

    def append_element(self, *elements):
        """Append elements to DynamicArray"""
        for element in elements:
            if self.len >= self.capacity:
                self._resize()
                self.arr[self.len] = element
                if element is not None:
                    self.len += 1
            else:
                self.arr[self.len] = element
                if element is not None:
                    self.len += 1

    def set_element(self, index, element):
        """Replace element with given index in DynamicArray """
        self._is_out_of_index(index)

        if self[index] is None and element is not None:
            """Change from None to something -> len of array +1"""
            self.len += 1
        if self[index] is not None and element is None:
            """Change from something to None -> len of array -1"""
            self.len -= 1

        self.arr[index] = element

    def remove_at(self, index):
        """Remove element with given index from DynamicArray (also rewrite current DynamicArray to new -
        shorter one)"""
        self._is_out_of_index(index)
        self.capacity -= 1
        self.len -= 1
        new_arr = [None] * self.capacity
        i, j = 0, 0
        while i < self.capacity:
            if i == index:
                j -= 1
            else:
                new_arr[j] = self.arr[i]
            i += 1
            j += 1
        self.arr = new_arr

    def remove(self, element):
        """Remove given element from DynamicArray"""
        index = self.contains(element)
        if index == -1:
            raise ValueError(
                "Array does not contain element you want to delete!")
        else:
            self.remove_at(index)

    def contains(self, element):
        """Check if given element is in DynamicArray and returns it's index. If there is no such element
        function returns -1"""
        for i in range(self.capacity):
            if self.arr[i] == element:
                return i
        return -1

class Node:
    """Elements in LinkedList -> data and pointer to next node"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """LinkedList with head and tail"""

    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        length = 0
        current_node = self.head

        if current_node is None:
            return length

        while current_node != self.tail:
            length += 1
            current_node = current_node.next

        length += 1
        return length

    def clear(self):
        self.head = None
        self.tail = None

    def print_list(self):
        list_of_nodes = []
        current_node = self.head

        if self.head is None:
            print(list_of_nodes)
            return

        while current_node:
            list_of_nodes.append(current_node.data)
            current_node = current_node.next

        print(list_of_nodes)

    def _contains_node(self, node):
        """Return index (start from 0 - like in array) if Node is in LinkedList, return -1 if not"""
        index = 0
        current_node = self.head

        if current_node is None:
            return -1
        elif current_node == node:
            return index
        else:
            while current_node != self.tail:
                if current_node == node:
                    return index
                index += 1
                current_node = current_node.next
            else:
                if current_node == node:  # check self.tail
                    return index
                return -1

    def contains(self, data):
        """Return index (start from 0 - like in array) if data is in LinkedList, return -1 if not"""
        index = 0
        current_node = self.head

        if current_node is None:
            return -1
        elif current_node.data == data:
            return index
        else:
            while current_node != self.tail:
                if current_node.data == data:
                    return index
                else:
                    index += 1
                    current_node = current_node.next

        if current_node.data == data:  # check self.tail
            return index
        else:
            return -1

    def append(self, *elements):
        for element in elements:
            new_node = Node(element)

            if self.head is None:
                self.head = new_node
                self.tail = new_node

            else:
                last_node = self.head
                while last_node.next:
                    last_node = last_node.next

                last_node.next = new_node
                self.tail = new_node

    def prepend(self, *elements):
        for element in reversed(elements):
            """iterate in reverse order, because want to achieve last in first out order"""
            new_node = Node(element)

            if self.tail is None:
                self.tail = new_node

            new_node.next = self.head
            self.head = new_node

    def insert_after_node(self, previous_node, data):
        if hasattr(previous_node, "next") and hasattr(previous_node, "data"):
            index = self.contains(previous_node)
            if index == -1:
                raise ValueError(
                    f"Given argument ({previous_node}) is not in the list!"
                )
            new_node = Node(data)
            new_node.next = previous_node.next
            previous_node.next = new_node
        else:
            raise ValueError(f"Given argument ({previous_node}) is not a Node!")

    def delete_node(self, node):
        if hasattr(node, "next") and hasattr(
            node, "data"
        ):  # Check if given argument is actually a Node
            index = self._contains_node(node)
            if index == -1:
                raise ValueError(f"Given argument ({node}) is not in list!")
            self.delete_node_at_index(index)
        else:
            raise ValueError(f"Given argument ({node}) is not a Node!")

    def delete_node_at_index(self, index):
        if isinstance(index, int) and (0 <= index < len(self)):
            if index == 0:  # delete head of LinkedList
                self.head = self.head.next

            elif index == len(self) - 1:  # delete tail of LinkedList
                node_previous_to_current_tail = self.head
                for i in range(index - 1):
                    node_previous_to_current_tail = node_previous_to_current_tail.next

                node_previous_to_current_tail.next = None
                self.tail = node_previous_to_current_tail

            else:
                node_previous_to_node_to_delete = self.head
                for i in range(index - 1):
                    node_previous_to_node_to_delete = (
                        node_previous_to_node_to_delete.next
                    )

                node_to_delete = node_previous_to_node_to_delete.next
                node_previous_to_node_to_delete.next = node_to_delete.next

        else:
            raise IndexError(
                "Given index need to be number and contains in LinkedList index!"
            )

    def delete(self, data):
        index = self.contains(data)
        if index == -1:
            raise ValueError(f"Given argument ({data}) is not in list!")
        else:
            self.delete_node_at_index(index)


a = LinkedList()
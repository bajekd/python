class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert(self, value):
        if self.value == value:  # Duplicates are not allowed
            return False

        elif self.value > value:
            if self.left_child:
                return self.left_child.insert(value)
            else:
                self.left_child = Node(value)
                return True

        else:
            if self.right_child:
                return self.right_child.insert(value)
            else:
                self.right_child = Node(value)
                return True

    def find(self, value):
        if self.value == value:
            return True

        elif self.value > value:
            if self.left_child:
                return self.left_child.find(value)
            else:
                return False

        else:
            if self.right_child:
                return self.right_child.find(value)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.value))
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

    def inorder(self):
        if self.left_child:
            self.left_child.inorder()
        if self:
            print(str(self.value))
        if self.right_child:
            self.right_child.inorder()

    def postorder(self):
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.posorder()
        if self:
            print(str(self.value))


class Tree:
    def __init__(self, value):
        self.value = value
        self.root = None

    def insert(self, value):
        if self.root:
            return self.root.insert(value)
        else:
            self.root = Node(value)
            return True

    def find(self, value):
        if self.root:
            return self.root.find(value)
        else:
            return False

    def preorder(self):
        print("Preorder")
        self.root.preorder()

    def inorder(self):
        print("Inorder")
        self.root.inorder()

    def postorder(self):
        print("Postorder")
        self.root.postorder()

    def remove(self, value_to_delete):
        if self.root is None:  # Tree is empty
            return False

        elif self.root.value == value_to_delete:  # Value is in root of tree
            if self.root.left_child is None and self.root.right_child is None:
                self.root = None
                return True

            elif self.root.left_child and self.root.right_child is None:
                self.root = self.root.left_child
                return True

            elif self.root.left_child is None and self.root.right_child:
                self.root = self.root.right_child
                return True

            elif self.root.left_child and self.root.right_child:
                parent_of_tmp = self.root
                tmp_node = (
                    self.root.right_child
                )  # could select to replace biggest value from left children
                #  node_to_delete.left_child and then go right to the bottom / smallest value from right children
                # (node_to_delete.right_child and then go left to the bottom)
                while tmp_node.left_child:
                    parent_of_tmp = tmp_node
                    tmp_node = tmp_node.left_child

                self.root.value = tmp_node.value
                if tmp_node.right_child:
                    if tmp_node.value < parent_of_tmp.value:
                        parent_of_tmp.left_child = tmp_node.right_child
                        return True
                    else:
                        parent_of_tmp.right_child = tmp_node.right_child
                        return True
                else:
                    if tmp_node.value < parent_of_tmp.value:
                        parent_of_tmp.left_child = None
                        return True
                    else:
                        parent_of_tmp.right_child = None
                        return True

        parent_node = None  # Find node to remove
        node_to_delete = self.root
        while node_to_delete and node_to_delete.value != value_to_delete:
            parent_node = node_to_delete
            if value_to_delete < parent_node:
                node_to_delete = node_to_delete.left_child
            elif value_to_delete > parent_node:
                node_to_delete = node_to_delete.right_child

        if (
            node_to_delete is None or node_to_delete.value != value_to_delete
        ):  # value not find
            return False

        elif (
            node_to_delete.left_child is None and node_to_delete.right_child is None
        ):  # node_to_delete
            # has no children
            if value_to_delete < parent_node.value:
                parent_node.left_child = None
            else:
                parent_node.right_child = None
            return True

        elif (
            node_to_delete.left_child and node_to_delete.right_child is None
        ):  # node_to_delete has
            # only left_child
            if value_to_delete < parent_node.value:
                parent_node.left_child = node_to_delete.left_child
            else:
                parent_node.right_child = node_to_delete.left_child
            return True

        elif (
            node_to_delete.left_child is None and node_to_delete.right_child
        ):  # node_to_delete has
            # only right_child
            if value_to_delete < parent_node.value:
                parent_node.left_child = node_to_delete.right_child
            else:
                parent_node.right_child = node_to_delete.right_child
            return True

        else:  # node_to_delete has two children
            parent_of_tmp = node_to_delete
            tmp_node = (
                node_to_delete.left_child
            )  # could select to replace biggest value from left children
            #  node_to_delete.left_child and then go right to the bottom / smallest value from right children
            # (node_to_delete.right_child and then go left to the bottom)

            while tmp_node.right_child:
                parent_of_tmp = tmp_node
                tmp_node = tmp_node.right_child

            node_to_delete.value = tmp_node.value
            if tmp_node.left_child:
                if (
                    tmp_node.value < parent_of_tmp.value
                ):  # need to ensure - simulate what is going to
                    # happen if above while loop is instantly false
                    parent_of_tmp.left_child = tmp_node.left_child
                else:
                    parent_of_tmp.right_child = tmp_node.left_child
            else:
                if tmp_node.value < parent_of_tmp.value:
                    parent_of_tmp.left_child = None
                else:
                    parent_of_tmp.right_child = None

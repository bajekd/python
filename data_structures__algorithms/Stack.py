class Stack:
    """Emulate stack with python built-in list data type"""

    def __init__(self, element_on_top_of_stack=None):
        """Create empty stack, or stack with one element"""
        self.items = []
        if element_on_top_of_stack is not None:
            self.items.append(element_on_top_of_stack)

    def __len__(self):
        """Implement len() function"""
        return len(self.items)

    def push(self, *elements_on_stack):
        """Append given arguments to stack"""
        for element in elements_on_stack:
            self.items.append(element)

    def pop(self):
        """Return last element from stack"""
        return self.items.pop()

    def print_stack(self):
        """Print all elements in stack (as a list)"""
        print(self.items)

    """Optional three functions with auxiliary functions to solve three example problems - 1) reverse given
    string, 2) convert decimal int into its binary representation 3) check if parentheses in given string
    are valid """

    def _is_empty(
        self,
    ):  # Auxiliary function to: reverse_string() and is_brackets_balanced()
        """Return True if stack is empty, False otherwise"""
        if len(self) == 0:
            return True
        else:
            return False

    def reverse_string(self, input_string):
        """Reverse given string using implemented stack data structure."""
        if isinstance(input_string, str):
            for char in input_string:
                self.push(char)

            reversed_string = ""
            while not self._is_empty():
                reversed_string += self.pop()

            return reversed_string
        else:
            raise AttributeError(f"Given argument ({input_string}) is not a string!")

    def converter_from_decimal_to_binary(self, input_int):
        """Convert given int to it's representation in binary (as a string)"""
        if isinstance(input_int, int):
            while input_int > 0:
                reminder = input_int % 2
                self.push(reminder)
                input_int = input_int // 2

            binary_representation = ""
            for element in self.items:
                binary_representation += str(self.pop())

            return binary_representation

        else:
            raise AttributeError(f"Given argument ({input_int})is not a integer!")

    def _is_match(
        self, top_bracket, current_bracket
    ):  # Auxiliary function to is_brackets_balanced()
        """Return True if two brackets are match, return False otherwise"""
        if top_bracket == "(" and current_bracket == ")":
            return True
        elif top_bracket == "[" and current_bracket == "]":
            return True
        elif top_bracket == "{" and current_bracket == "}":
            return True
        else:
            return False

    def is_brackets_balanced(self, input_string):
        """Check if brackets are valid in given input - if so return True, otherwise - return False"""
        if isinstance(input_string, str):
            is_balanced = True
            index = 0

            while index < len(input_string) and is_balanced:
                current_char = input_string[index]
                if current_char in "([{":
                    self.push(current_char)
                elif current_char in ")]}":
                    if self._is_empty():
                        is_balanced = False
                    else:
                        top_bracket = self.pop()
                        if not self._is_match(top_bracket, current_char):
                            is_balanced = False
                else:
                    pass
                index += 1

            if self._is_empty() and is_balanced:
                return True
            else:
                return False

        else:
            raise AttributeError(f"Given argument ({input_string}) is not a string!")
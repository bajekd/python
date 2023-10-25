from abc import ABC, abstractmethod


class Abstraction:
    def __init__(self, implementation):
        self.implementation = implementation

    def operation(self):
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}")


class ExtendedAbstraction(Abstraction):
    def operation(self):
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")


class Implementation(ABC):

    @abstractmethod
    def operation_implementation(self):
        pass


class ConcreteImplementationA(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationA: Here's the result on the platform A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationB: Here's the result on the platform B."


def client_code(abstraction: Abstraction):
    print(abstraction.operation(), end="")


if __name__ == "__main__":
    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)

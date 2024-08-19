from __future__ import annotations
from abc import ABC, abstractmethod


class Shape:
    """
        Một lớp hình học là một lớp cơ sở chứa các phương thức ban đầu
    """

    def __init__(self, color: Color) -> None:
        self.color = color

    def operation(self) -> str:
        return (f"Abstraction: Base operation with:\n"
                f"{self.color.operation_implementation()}")


class Circle(Shape):
    """
    Lớp Circle kế thừa lớp Shape và
    """

    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.color.operation_implementation()}")


class Square(Shape):
    """
    You can extend the Abstraction without changing the Implementation classes.
    """

    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.color.operation_implementation()}")


class Color(ABC):
    """
    The Implementation defines the interface for all implementation classes. It
    doesn't have to match the Abstraction's interface. In fact, the two
    interfaces can be entirely different. Typically the Implementation interface
    provides only primitive operations, while the Abstraction defines higher-
    level operations based on those primitives.
    """

    @abstractmethod
    def operation_implementation(self) -> str:
        pass


"""
Each Concrete Implementation corresponds to a specific platform and implements
the Implementation interface using that platform's API.
"""


class Red(Color):
    def operation_implementation(self) -> str:
        return "Red: Here's the result on the platform."


class Blue(Color):
    def operation_implementation(self) -> str:
        return "Blue: Here's the result on the platform."


def client_code(shape: Shape) -> None:
    """
    Except for the initialization phase, where an Abstraction object gets linked
    with a specific Implementation object, the client code should only depend on
    the Abstraction class. This way the client code can support any abstraction-
    implementation combination.
    """

    # ...

    print(shape.operation(), end="")

    # ...


if __name__ == "__main__":
    """
    The client code should be able to work with any pre-configured abstraction-
    implementation combination.
    """

    red = Red()
    red_circle = Shape(red)
    client_code(red_circle)

    print("\n")

    blue = Blue()
    circle_blue = Circle(blue)
    client_code(circle_blue)

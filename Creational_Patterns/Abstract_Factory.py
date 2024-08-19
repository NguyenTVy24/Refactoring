from __future__ import annotations
from abc import ABC, abstractmethod


class GUIFactory(ABC):
    """
    GUI Factory Abstract Class sở hữu 2 phương thức là tạo Button và tạo
    CheckBox và sẽ được định nghĩa ở lớp kế thừa, 2 phương thức này được
    định nghĩa sẽ trả về một Abstract Class khác sẽ được xác định ở lớp kế thừa.
    """
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> CheckBox:
        pass


class WinFactory(GUIFactory):
    """
    WinFactory là lớp kế thừa của GUIFactory ghi lại 2 phương thức tạo buttom và tạo checkbox
    2 phương thức này ra trả về lớp kế thừa của lớp trừu tượng đã được xác định sẽ trả về trước đó.
    """

    def create_button(self) -> Button:
        return ButtonWin()

    def create_checkbox(self) -> CheckBox:
        return CheckboxWin()


class MacFactory(GUIFactory):
    """
    Để thể hiện rỏ hơn ta tạo thêm một lớp MacFactory kế thừa lớp trừu tượng,
    thể hiện rỏ khả năng phát triển đa đạng của lớp trừu tượng.
    """

    def create_button(self) -> Button:
        return ButtonMac()

    def create_checkbox(self) -> CheckBox:
        return CheckboxMac()


class Button(ABC):
    """
    Là một lớp trừu tượng có một phương thức
    """

    @abstractmethod
    def click(self) -> str:
        pass


class ButtonWin(Button):
    def click(self) -> str:
        return "Click Win Button."


class ButtonMac(Button):
    def click(self) -> str:
        return "Click Mac Button."


class CheckBox(ABC):
    """
    Các lớp trừu tượng được tạo ra có thể tương tác với nhau nhưng nó sẽ mang ý nghĩa
    tuy thuộc vào lớp kế thừa được xác định trước đó.
    """
    @abstractmethod
    def click(self) -> None:
        pass

    @abstractmethod
    def unclick(self, collaborator: Button) -> None:
        pass


class CheckboxWin(CheckBox):
    def click(self) -> str:
        return "Click Win CheckBox."

    def unclick(self, collaborator: Button) -> str:
        result = collaborator.click()
        return f"Unclick Win CheckBox, ({result})"


class CheckboxMac(CheckBox):
    def click(self) -> str:
        return "Click Mac CheckBox."

    def unclick(self, collaborator: Button):
        result = collaborator.click()
        return f"Unclick Mac CheckBox, ({result})"


def client_code(factory: GUIFactory) -> None:
    product_a = factory.create_button()
    product_b = factory.create_checkbox()

    print(f"{product_b.click()}")
    print(f"{product_b.unclick(product_a)}", end="")


if __name__ == "__main__":
    print("Client: Testing client code with the Win factory type:")
    client_code(WinFactory())

    print("\n")

    print("Client: Testing the same client code with the Mac factory type:")
    client_code(MacFactory())

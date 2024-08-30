from __future__ import annotations
from abc import ABC


class Mediator(ABC):
    """
    Giao diện Mediator khai báo một phương thức để các thành phần (components)
    có thể thông báo cho mediator về các sự kiện khác nhau.
    Mediator có thể phản ứng với các sự kiện này và truyền việc thực hiện
    cho các thành phần khác.
    """

    def notify(self, sender: object, event: str) -> None:
        pass


class ConcreteMediator(Mediator):
    """
    Mediator cụ thể điều phối việc giao tiếp giữa các thành phần.
    """

    def __init__(self, component1: Component1, component2: Component2) -> None:
        # Thiết lập mối quan hệ giữa các thành phần và mediator
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        """
        Phương thức này được gọi khi một thành phần kích hoạt một sự kiện.
        Mediator sẽ quyết định cách phản ứng lại dựa trên sự kiện đó.
        """
        if event == "A":
            print("Mediator phản ứng với sự kiện A và kích hoạt các hoạt động sau:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator phản ứng với sự kiện D và kích hoạt các hoạt động sau:")
            self._component1.do_b()
            self._component2.do_c()


class BaseComponent:
    """
    Lớp thành phần cơ sở cung cấp chức năng cơ bản là lưu trữ một đối tượng
    mediator bên trong các thành phần.
    """

    def __init__(self, _mediator: Mediator = None) -> None:
        self._mediator = _mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, _mediator: Mediator) -> None:
        self._mediator = _mediator


"""
Các thành phần cụ thể triển khai các chức năng khác nhau.
Chúng không phụ thuộc vào các thành phần khác hoặc lớp mediator cụ thể.
"""


class Component1(BaseComponent):
    def do_a(self) -> None:
        """
        Phương thức này kích hoạt sự kiện A.
        """
        print("Thành phần 1 thực hiện hành động A.")
        self.mediator.notify(self, "A")

    def do_b(self) -> None:
        """
        Phương thức này kích hoạt sự kiện B.
        """
        print("Thành phần 1 thực hiện hành động B.")
        self.mediator.notify(self, "B")


class Component2(BaseComponent):
    def do_c(self) -> None:
        """
        Phương thức này kích hoạt sự kiện C.
        """
        print("Thành phần 2 thực hiện hành động C.")
        self.mediator.notify(self, "C")

    def do_d(self) -> None:
        """
        Phương thức này kích hoạt sự kiện D.
        """
        print("Thành phần 2 thực hiện hành động D.")
        self.mediator.notify(self, "D")


if __name__ == "__main__":
    # Mã của client.
    # Tạo các thành phần và mediator
    c1 = Component1()
    c2 = Component2()
    mediator = ConcreteMediator(c1, c2)

    # Kích hoạt sự kiện A thông qua Component1
    print("Client kích hoạt hành động A.")
    c1.do_a()

    print("\n", end="")

    # Kích hoạt sự kiện D thông qua Component2
    print("Client kích hoạt hành động D.")
    c2.do_d()

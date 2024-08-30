from __future__ import annotations
from abc import ABC, abstractmethod


# Giao diện Command tuyên bố một phương thức để thực thi lệnh.
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


# Lớp SimpleCommand thực thi các lệnh đơn giản.
class SimpleCommand(Command):
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: Thực hiện một hành động đơn giản như in"
              f"({self._payload})")


# Lớp ComplexCommand thực hiện các lệnh phức tạp hơn và có thể ủy nhiệm
# công việc cho các đối tượng khác, gọi là "receiver".
class ComplexCommand(Command):
    def __init__(self, _receiver: Receiver, a: str, b: str) -> None:
        """
        Lệnh phức tạp có thể chấp nhận một hoặc nhiều đối tượng receiver cùng với
        bất kỳ dữ liệu ngữ cảnh nào thông qua constructor.
        """
        self._receiver = _receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        """
        Lệnh có thể ủy nhiệm cho bất kỳ phương thức nào của receiver.
        """
        print("ComplexCommand: Công việc phức tạp nên được thực hiện bởi một đối tượng receiver", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


# Lớp Receiver chứa logic nghiệp vụ quan trọng. Chúng biết cách thực hiện
# các loại thao tác khác nhau, liên quan đến việc thực hiện một yêu cầu.
# Thực tế, bất kỳ lớp nào cũng có thể phục vụ như một Receiver.
class Receiver:
    @staticmethod
    def do_something(a: str) -> None:
        print(f"\nReceiver: Đang xử lý ({a}.)", end="")

    @staticmethod
    def do_something_else(b: str) -> None:
        print(f"\nReceiver: Cũng đang xử lý ({b}.)", end="")


# Lớp Invoker liên kết với một hoặc nhiều lệnh. Nó gửi yêu cầu tới lệnh.
class Invoker:
    _on_start = None
    _on_finish = None

    # Khởi tạo lệnh bắt đầu.
    def set_on_start(self, command: Command):
        self._on_start = command

    # Khởi tạo lệnh kết thúc.
    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        """
        Invoker không phụ thuộc vào các lớp lệnh hoặc receiver cụ thể.
        Invoker chuyển yêu cầu tới receiver gián tiếp bằng cách thực thi lệnh.
        """
        print("Invoker: Có ai muốn làm gì trước khi tôi bắt đầu không?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...đang làm một việc rất quan trọng...")

        print("Invoker: Có ai muốn làm gì sau khi tôi kết thúc không?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    """
    Mã client có thể tham số hóa invoker với bất kỳ lệnh nào.
    """

    # Tạo một đối tượng Invoker
    invoker = Invoker()

    # Gán lệnh đơn giản cho invoker để thực thi khi bắt đầu
    invoker.set_on_start(SimpleCommand("Chào bạn!"))

    # Tạo một đối tượng receiver
    receiver = Receiver()

    # Gán lệnh phức tạp cho invoker để thực thi khi kết thúc
    invoker.set_on_finish(ComplexCommand(receiver, "Gửi email", "Lưu báo cáo"))

    # Thực hiện một công việc quan trọng bởi invoker
    invoker.do_something_important()

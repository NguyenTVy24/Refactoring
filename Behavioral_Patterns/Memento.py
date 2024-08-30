from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters


class Originator:
    """
    Originator lưu giữ trạng thái quan trọng mà có thể thay đổi theo thời gian.
    Nó cũng định nghĩa phương thức để lưu trạng thái vào một đối tượng memento
    và một phương thức khác để khôi phục trạng thái từ đó.
    """

    _state = None
    """
    Để đơn giản, trạng thái của originator được lưu trữ trong một biến duy nhất.
    """

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: Trạng thái ban đầu của tôi là: {self._state}")

    def do_something(self) -> None:
        """
        Logic xử lý của Originator có thể ảnh hưởng đến trạng thái nội bộ của nó.
        Do đó, client nên sao lưu trạng thái trước khi gọi các phương thức
        của logic xử lý thông qua phương thức save().
        """

        print("Originator: Tôi đang làm một việc quan trọng.")
        self._state = self._generate_random_string(30)
        print(f"Originator: và trạng thái của tôi đã thay đổi thành: {self._state}")

    @staticmethod
    def _generate_random_string(length: int = 10) -> str:
        """
        Tạo một chuỗi ngẫu nhiên để minh họa cho sự thay đổi trạng thái.
        """
        return "".join(sample(ascii_letters, length))

    def save(self) -> Memento:
        """
        Lưu trạng thái hiện tại vào một đối tượng memento.
        """
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        """
        Khôi phục trạng thái của Originator từ đối tượng memento.
        """
        self._state = memento.get_state()
        print(f"Originator: Trạng thái của tôi đã thay đổi thành: {self._state}")


class Memento(ABC):
    """
    Giao diện Memento cung cấp cách để truy xuất các thông tin metadata của memento,
    như ngày tạo hoặc tên. Tuy nhiên, nó không tiết lộ trạng thái của Originator.
    """

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


class ConcreteMemento(Memento):
    """
    Lớp Memento cụ thể, lưu trữ trạng thái của Originator và ngày tạo memento.
    """

    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        """
        Originator sử dụng phương thức này để khôi phục trạng thái của mình.
        """
        return self._state

    def get_name(self) -> str:
        """
        Các phương thức này được Caretaker sử dụng để hiển thị thông tin metadata.
        """
        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self) -> str:
        return self._date


class Caretaker:
    """
    Caretaker không phụ thuộc vào lớp Memento cụ thể.
    Do đó, nó không có quyền truy cập vào trạng thái của Originator được lưu trữ
    bên trong memento. Nó làm việc với tất cả mementos thông qua giao diện Memento.
    """

    def __init__(self, _originator: Originator) -> None:
        self._mementos = []
        self._originator = _originator

    def backup(self) -> None:
        """
        Sao lưu trạng thái hiện tại của Originator.
        """
        print("\nCaretaker: Đang lưu trạng thái của Originator...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        """
        Khôi phục trạng thái cuối cùng từ danh sách mementos.
        """
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Khôi phục trạng thái đến: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception as e:
            print(e)
            self.undo()

    def show_history(self) -> None:
        """
        Hiển thị lịch sử các trạng thái đã được lưu.
        """
        print("Caretaker: Đây là danh sách các mementos:")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":
    # Tạo một Originator với trạng thái ban đầu
    originator = Originator("Trạng thái-ban-đầu-siêu-khủng.")

    # Tạo một Caretaker để quản lý các mementos
    caretaker = Caretaker(originator)

    # Lưu trạng thái và thay đổi trạng thái của Originator
    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    print()
    caretaker.show_history()

    # Khôi phục lại trạng thái trước đó
    print("\nClient: Bây giờ, chúng ta sẽ quay lại trạng thái trước!\n")
    caretaker.undo()

    print("\nClient: Quay lại một lần nữa!\n")
    caretaker.undo()

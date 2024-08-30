from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any


"""
Để tạo một iterator trong Python, có hai lớp trừu tượng từ mô-đun tích hợp
`collections`: Iterable và Iterator. Chúng ta cần triển khai phương thức 
`__iter__()` trong đối tượng sẽ được duyệt qua (tập hợp), và phương thức 
`__next__()` trong iterator.
"""


class NumberIterator(Iterator):
    """
    (Concrete Iterator) triển khai các thuật toán duyệt khác nhau.
    Các lớp này lưu trữ vị trí duyệt hiện tại mọi lúc.
    """

    """
    Thuộc tính `_position` lưu trữ vị trí duyệt hiện tại. Một iterator có thể có
    nhiều thuộc tính khác để lưu trữ trạng thái của việc duyệt, đặc biệt khi nó
    được thiết kế để làm việc với một loại tập hợp cụ thể.
    """
    _position: int = None

    """
    Thuộc tính này chỉ ra hướng duyệt.
    """
    _reverse: bool = False

    def __init__(self, _collection: NumberCollection, reverse: bool = False) -> None:
        self._collection = _collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self) -> Any:
        """
        Phương thức __next__() phải trả về phần tử tiếp theo trong dãy. Khi đạt
        đến cuối dãy, và trong các lần gọi tiếp theo, nó phải ném ra ngoại lệ
        StopIteration.
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class NumberCollection(Iterable):
    """
    Tập hợp cụ thể (Concrete Collection) cung cấp một hoặc nhiều phương thức
    để lấy các thể hiện iterator mới, tương thích với lớp tập hợp.
    """

    def __init__(self, _collection: list[int] | None = None) -> None:
        self._collection = _collection or []

    def __getitem__(self, index: int) -> int:
        return self._collection[index]

    def __iter__(self) -> NumberIterator:
        """
        Phương thức __iter__() trả về chính đối tượng iterator, mặc định chúng ta
        trả về iterator theo thứ tự tăng dần.
        """
        return NumberIterator(self)

    def get_reverse_iterator(self) -> NumberIterator:
        return NumberIterator(self, True)

    def add_item(self, item: int) -> None:
        self._collection.append(item)


if __name__ == "__main__":
    # Mã phía client có thể hoặc không biết về các lớp Iterator hoặc Collection
    # cụ thể, tùy thuộc vào mức độ gián tiếp bạn muốn giữ trong chương trình.
    collection = NumberCollection()
    collection.add_item(1)
    collection.add_item(2)
    collection.add_item(3)

    print("Duyệt theo thứ tự tăng dần:")
    for number in collection:
        print(number)
    print("")

    print("Duyệt theo thứ tự giảm dần:")
    for number in collection.get_reverse_iterator():
        print(number)

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Context:
    """
    Lớp Context định nghĩa giao diện mà các client quan tâm.
    """

    def __init__(self, strategy: Strategy) -> None:
        """
        Context thường nhận một strategy thông qua constructor, nhưng cũng cung cấp
        một setter để thay đổi nó trong thời gian chạy.
        """
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        Context duy trì tham chiếu đến một trong các đối tượng Strategy.
        Context không biết lớp cụ thể của strategy. Nó chỉ làm việc với tất cả
        các chiến lược thông qua giao diện Strategy.
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Context cho phép thay thế đối tượng Strategy trong thời gian chạy.
        """
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        """
        Context ủy thác một số công việc cho đối tượng Strategy thay vì triển khai
        nhiều phiên bản của thuật toán trên chính nó.
        """
        print("Context: Sắp xếp dữ liệu bằng strategy (không biết cách nó sẽ thực hiện)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))


class Strategy(ABC):
    """
    Giao diện Strategy tuyên bố các phương thức chung cho tất cả các phiên bản
    thuật toán được hỗ trợ.

    Context sử dụng giao diện này để gọi thuật toán được định nghĩa bởi các
    Concrete Strategy.
    """

    @abstractmethod
    def do_algorithm(self, data: List) -> List:
        pass


class ConcreteStrategyA(Strategy):
    """
    Concrete Strategy A triển khai thuật toán sắp xếp theo thứ tự tăng dần.
    """

    def do_algorithm(self, data: List) -> List:
        return sorted(data)


class ConcreteStrategyB(Strategy):
    """
    Concrete Strategy B triển khai thuật toán sắp xếp theo thứ tự giảm dần.
    """

    def do_algorithm(self, data: List) -> List:
        return list(reversed(sorted(data)))


if __name__ == "__main__":
    # Client chọn một chiến lược cụ thể và truyền nó vào Context.
    # Client cần biết sự khác biệt giữa các chiến lược để đưa ra lựa chọn đúng đắn.

    context = Context(ConcreteStrategyA())
    print("Client: Chiến lược được đặt thành sắp xếp thông thường.")
    context.do_some_business_logic()
    print()

    print("Client: Chiến lược được đặt thành sắp xếp ngược.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()

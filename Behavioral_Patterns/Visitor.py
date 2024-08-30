from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


# Giao diện Component định nghĩa phương thức `accept` mà sẽ nhận đối tượng visitor làm đối số.
class ThanhPhan(ABC):
    @abstractmethod
    def chap_nhan(self, visitor: KhachThamQuan) -> None:
        pass


# Lớp thành phần cụ thể A triển khai phương thức `chap_nhan` để gọi đúng phương thức của visitor tương ứng.
class ThanhPhanCuTheA(ThanhPhan):
    def chap_nhan(self, visitor: KhachThamQuan) -> None:
        """
        Chú ý rằng ở đây chúng ta gọi phương thức `tham_quan_thanh_phan_cu_the_a`,
        giúp visitor biết rằng nó đang làm việc với lớp cụ thể nào.
        """
        visitor.tham_quan_thanh_phan_cu_the_a(self)

    def phuong_thuc_rieng_cua_thanh_phan_a(self) -> str:
        """
        Các thành phần cụ thể có thể có những phương thức đặc biệt mà không có trong
        lớp cơ bản hoặc giao diện. Visitor vẫn có thể sử dụng những phương thức này
        nhờ biết lớp cụ thể của thành phần.
        """
        return "A"


# Lớp thành phần cụ thể B tương tự, triển khai phương thức `chap_nhan` và gọi đúng phương thức của visitor tương ứng.
class ThanhPhanCuTheB(ThanhPhan):
    def chap_nhan(self, visitor: KhachThamQuan) -> None:
        visitor.tham_quan_thanh_phan_cu_the_b(self)

    def phuong_thuc_rieng_cua_thanh_phan_b(self) -> str:
        return "B"


# Giao diện Khách Tham Quan (Visitor) định nghĩa các phương thức thăm quan, tương ứng với các lớp thành phần cụ thể.
class KhachThamQuan(ABC):
    @abstractmethod
    def tham_quan_thanh_phan_cu_the_a(self, element: ThanhPhanCuTheA) -> None:
        pass

    @abstractmethod
    def tham_quan_thanh_phan_cu_the_b(self, element: ThanhPhanCuTheB) -> None:
        pass


# Các lớp Khách Tham Quan cụ thể triển khai các phiên bản của phương thức thăm quan để xử lý từng loại thành phần cụ thể.
class KhachThamQuanCuThe1(KhachThamQuan):
    def tham_quan_thanh_phan_cu_the_a(self, element: ThanhPhanCuTheA) -> None:
        print(f"{element.phuong_thuc_rieng_cua_thanh_phan_a()} + KhachThamQuanCuThe1")

    def tham_quan_thanh_phan_cu_the_b(self, element: ThanhPhanCuTheB) -> None:
        print(f"{element.phuong_thuc_rieng_cua_thanh_phan_b()} + KhachThamQuanCuThe1")


class KhachThamQuanCuThe2(KhachThamQuan):
    def tham_quan_thanh_phan_cu_the_a(self, element: ThanhPhanCuTheA) -> None:
        print(f"{element.phuong_thuc_rieng_cua_thanh_phan_a()} + KhachThamQuanCuThe2")

    def tham_quan_thanh_phan_cu_the_b(self, element: ThanhPhanCuTheB) -> None:
        print(f"{element.phuong_thuc_rieng_cua_thanh_phan_b()} + KhachThamQuanCuThe2")


# Mã client có thể chạy các thao tác của visitor trên bất kỳ tập hợp thành phần nào mà không cần biết lớp cụ thể của chúng.
def ma_client(thanh_phan: List[ThanhPhan], visitor: KhachThamQuan) -> None:
    for tp in thanh_phan:
        tp.chap_nhan(visitor)


if __name__ == "__main__":
    thanh_phan = [ThanhPhanCuTheA(), ThanhPhanCuTheB()]

    print("Mã client hoạt động với tất cả các khách thăm quan qua giao diện KhachThamQuan:")
    visitor1 = KhachThamQuanCuThe1()
    ma_client(thanh_phan, visitor1)

    print("Điều này cho phép mã client hoạt động với các loại khách thăm quan khác nhau:")
    visitor2 = KhachThamQuanCuThe2()
    ma_client(thanh_phan, visitor2)

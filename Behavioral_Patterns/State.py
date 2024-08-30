from __future__ import annotations
from abc import ABC, abstractmethod


class NguCanh:
    """
    Lớp NguCanh định nghĩa giao diện mà các đối tượng khác quan tâm.
    Nó cũng duy trì một tham chiếu đến một đối tượng trạng thái,
    đại diện cho trạng thái hiện tại của NguCanh.
    """

    _trang_thai = None  # Tham chiếu đến trạng thái hiện tại của NgữCảnh.

    def __init__(self, trang_thai: TrangThai) -> None:
        self.chuyen_sang_trang_thai(trang_thai)

    def chuyen_sang_trang_thai(self, trang_thai: TrangThai):
        """
        Phương thức này cho phép thay đổi đối tượng trạng thái trong quá trình chạy.
        """
        print(f"NgữCảnh: Chuyển sang {type(trang_thai).__name__}")
        self._trang_thai = trang_thai
        self._trang_thai.ngu_canh = self

    def yeu_cau1(self):
        """
        NguCanh ủy quyền một phần hành vi của nó cho đối tượng trạng thái hiện tại.
        """
        self._trang_thai.xu_ly1()

    def yeu_cau2(self):
        self._trang_thai.xu_ly2()


class TrangThai(ABC):
    """
    Lớp cơ sở TrangThai khai báo các phương thức mà tất cả các trạng thái cụ thể
    cần triển khai. Nó cũng cung cấp một tham chiếu ngược đến đối tượng NguCanh,
    có thể được sử dụng bởi các trạng thái để chuyển đổi NgữCảnh sang trạng thái khác.
    """

    @property
    def ngu_canh(self) -> NguCanh:
        return self._ngu_canh

    @ngu_canh.setter
    def ngu_canh(self, _ngu_canh: NguCanh) -> None:
        self._ngu_canh = _ngu_canh

    @abstractmethod
    def xu_ly1(self) -> None:
        pass

    @abstractmethod
    def xu_ly2(self) -> None:
        pass


class TrangThaiCuTheA(TrangThai):
    """
    Lớp TrangThaiCuTheA triển khai các hành vi cụ thể liên quan đến trạng thái này.
    """

    def xu_ly1(self) -> None:
        print("TrangThaiCuTheA xử lý yêu cầu 1.")
        print("TrangThaiCuTheA muốn chuyển trạng thái của NgữCảnh.")
        self.ngu_canh.chuyen_sang_trang_thai(TrangThaiCuTheB())

    def xu_ly2(self) -> None:
        print("TrangThaiCuTheA xử lý yêu cầu 2.")


class TrangThaiCuTheB(TrangThai):
    """
    Lớp TrangThaiCuTheB triển khai các hành vi cụ thể liên quan đến trạng thái này.
    """

    def xu_ly1(self) -> None:
        print("TrangThaiCuTheB xử lý yêu cầu 1.")

    def xu_ly2(self) -> None:
        print("TrangThaiCuTheB xử lý yêu cầu 2.")
        print("TrangThaiCuTheB muốn chuyển trạng thái của NgữCảnh.")
        self.ngu_canh.chuyen_sang_trang_thai(TrangThaiCuTheA())


if __name__ == "__main__":
    # Mã client.

    ngu_canh = NguCanh(TrangThaiCuTheA())
    ngu_canh.yeu_cau1()  # NguCanh sẽ chuyển từ trạng thái A sang trạng thái B
    ngu_canh.yeu_cau2()  # NguCanh sẽ chuyển từ trạng thái B sang trạng thái A

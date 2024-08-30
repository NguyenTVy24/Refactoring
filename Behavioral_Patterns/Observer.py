from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class ChuDe(ABC):
    """
    Giao diện ChuDe khai báo các phương thức để quản lý các người quan sát (observer).
    """

    @abstractmethod
    def gan_ket(self, nguoi_quan_sat: NguoiQuanSat) -> None:
        """
        Gắn kết một người quan sát vào chủ đề.
        """
        pass

    @abstractmethod
    def go_bo(self, nguoi_quan_sat: NguoiQuanSat) -> None:
        """
        Gỡ bỏ một người quan sát khỏi chủ đề.
        """
        pass

    @abstractmethod
    def thong_bao(self) -> None:
        """
        Thông báo tất cả người quan sát về một sự kiện.
        """
        pass


class ChuDeCuThe(ChuDe):
    """
    Lớp ChuDeCuThe nắm giữ trạng thái quan trọng và thông báo cho người quan sát
    khi trạng thái thay đổi.
    """

    _trang_thai: int = None  # Trạng thái của chủ đề, có thể là bất kỳ thông tin quan trọng nào.

    _nguoi_quan_sat: List[NguoiQuanSat] = []  # Danh sách các người quan sát đã đăng ký.

    def gan_ket(self, nguoi_quan_sat: NguoiQuanSat) -> None:
        """
        Gắn kết một người quan sát vào danh sách.
        """
        print("ChuDe: Đã gắn kết một người quan sát.")
        self._nguoi_quan_sat.append(nguoi_quan_sat)

    def go_bo(self, nguoi_quan_sat: NguoiQuanSat) -> None:
        """
        Gỡ bỏ một người quan sát khỏi danh sách.
        """
        self._nguoi_quan_sat.remove(nguoi_quan_sat)

    def thong_bao(self) -> None:
        """
        Kích hoạt việc cập nhật cho tất cả người quan sát đã đăng ký.
        """
        print("ChuDe: Đang thông báo cho các người quan sát...")
        for nguoi_quan_sat in self._nguoi_quan_sat:
            nguoi_quan_sat.cap_nhat(self)

    def thuc_hien_cong_viec_quan_trong(self) -> None:
        """
        Chủ đề có thể thực hiện một số logic quan trọng và thay đổi trạng thái.
        Sau đó, nó sẽ thông báo cho các người quan sát về sự thay đổi.
        """
        print("\nChuDe: Tôi đang thực hiện một công việc quan trọng.")
        self._trang_thai = randrange(0, 10)

        print(f"ChuDe: Trạng thái của tôi vừa thay đổi thành: {self._trang_thai}")
        self.thong_bao()


class NguoiQuanSat(ABC):
    """
    Giao diện NguoiQuanSat khai báo phương thức cập nhật, được chủ đề gọi khi có sự thay đổi.
    """

    @abstractmethod
    def cap_nhat(self, _chu_de: ChuDe) -> None:
        """
        Nhận thông tin cập nhật từ chủ đề.
        """
        pass


class NguoiQuanSatCuTheA(NguoiQuanSat):
    """
    Lớp NguoiQuanSatCuTheA phản ứng khi trạng thái của chủ đề nhỏ hơn 3.
    """
    def cap_nhat(self, _chu_de: ChuDe) -> None:
        if _chu_de._trang_thai < 3:
            print("NguoiQuanSatCuTheA: Đã phản ứng với sự kiện")


class NguoiQuanSatCuTheB(NguoiQuanSat):
    """
    Lớp NguoiQuanSatCuTheB phản ứng khi trạng thái của chủ đề bằng 0 hoặc lớn hơn hoặc bằng 2.
    """
    def cap_nhat(self, _chu_de: ChuDe) -> None:
        if _chu_de._trang_thai == 0 or _chu_de._trang_thai >= 2:
            print("NguoiQuanSatCuTheB: Đã phản ứng với sự kiện")


if __name__ == "__main__":
    # Mã client.

    chu_de = ChuDeCuThe()

    nguoi_quan_sat_a = NguoiQuanSatCuTheA()
    chu_de.gan_ket(nguoi_quan_sat_a)

    nguoi_quan_sat_b = NguoiQuanSatCuTheB()
    chu_de.gan_ket(nguoi_quan_sat_b)

    chu_de.thuc_hien_cong_viec_quan_trong()
    chu_de.thuc_hien_cong_viec_quan_trong()

    chu_de.go_bo(nguoi_quan_sat_a)

    chu_de.thuc_hien_cong_viec_quan_trong()

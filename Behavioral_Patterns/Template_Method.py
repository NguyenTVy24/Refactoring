from abc import ABC, abstractmethod


class LopTruuTuong(ABC):
    """
    Lớp trừu tượng định nghĩa một phương thức khung (template method) mà chứa bộ khung của
    một số thuật toán, được tạo thành từ các lời gọi đến các phương thức trừu tượng.

    Các lớp con cụ thể sẽ triển khai những phương thức này, nhưng để lại phương thức khung không thay đổi.
    """

    def phuong_thuc_khung(self) -> None:
        """
        Phương thức khung định nghĩa bộ khung của một thuật toán.
        """

        self.kiem_tra_dau_vao()
        self.thuc_hien_buoc1()
        self.kiem_tra_dieu_kien1()
        self.thuc_hien_buoc2()
        self.kiem_tra_dieu_kien2()
        self.ket_thuc()

    # Các phương thức này đã có sẵn phần triển khai.

    def kiem_tra_dau_vao(self) -> None:
        print("LopTruuTuong: Đang kiểm tra đầu vào")

    def kiem_tra_dieu_kien1(self) -> None:
        print("LopTruuTuong: Đang kiểm tra điều kiện 1")

    def ket_thuc(self) -> None:
        print("LopTruuTuong: Kết thúc quá trình")

    # Các phương thức này cần phải được triển khai trong các lớp con.

    @abstractmethod
    def thuc_hien_buoc1(self) -> None:
        pass

    @abstractmethod
    def thuc_hien_buoc2(self) -> None:
        pass

    # Đây là các "hook" (móc nối). Các lớp con có thể ghi đè, nhưng không bắt buộc.
    # Các móc nối này cung cấp thêm các điểm mở rộng ở một số nơi quan trọng trong
    # thuật toán.

    def kiem_tra_dieu_kien2(self) -> None:
        pass


class LopCaiTien1(LopTruuTuong):
    """
    Lớp cụ thể phải triển khai tất cả các phương thức trừu tượng của lớp cơ bản.
    Chúng cũng có thể ghi đè một số phương thức với phần triển khai mặc định.
    """

    def thuc_hien_buoc1(self) -> None:
        print("LopCaiTien1: Đã triển khai Bước 1")

    def thuc_hien_buoc2(self) -> None:
        print("LopCaiTien1: Đã triển khai Bước 2")


class LopCaiTien2(LopTruuTuong):
    """
    Thông thường, các lớp cụ thể chỉ ghi đè một phần các phương thức của lớp cơ bản.
    """

    def thuc_hien_buoc1(self) -> None:
        print("LopCaiTien2: Đã triển khai Bước 1")

    def thuc_hien_buoc2(self) -> None:
        print("LopCaiTien2: Đã triển khai Bước 2")

    def kiem_tra_dieu_kien2(self) -> None:
        print("LopCaiTien2: Đã ghi đè Kiểm tra Điều kiện 2")


def client_code(lop_truu_tuong: LopTruuTuong) -> None:
    """
    Mã client gọi phương thức khung để thực hiện thuật toán. Mã client không cần
    phải biết lớp cụ thể của đối tượng mà nó đang làm việc, miễn là nó làm việc
    với các đối tượng thông qua giao diện của lớp cơ bản.
    """

    # ...
    lop_truu_tuong.phuong_thuc_khung()
    # ...


if __name__ == "__main__":
    print("Mã client có thể làm việc với các lớp con khác nhau:")
    client_code(LopCaiTien1())
    print("")

    print("Mã client có thể làm việc với các lớp con khác nhau:")
    client_code(LopCaiTien2())

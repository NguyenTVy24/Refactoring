class HeThongTimChuyenBay:
    @staticmethod
    def tim_chuyen_bay(diem_di: str, diem_den: str) -> str:
        # Giả sử logic phức tạp để tìm chuyến bay
        return f"Đã tìm thấy chuyến bay từ {diem_di} đến {diem_den}"


class HeThongDatVe:
    @staticmethod
    def dat_ve(thong_tin_chuyen_bay: str) -> str:
        # Giả sử logic phức tạp để đặt vé
        return f"Đã đặt vé thành công: {thong_tin_chuyen_bay}"


class HeThongThanhToan:
    @staticmethod
    def thanh_toan(so_tien: float) -> str:
        # Giả sử logic phức tạp để thanh toán
        return f"Đã thanh toán số tiền: {so_tien} VND"


class HeThongEmail:
    @staticmethod
    def gui_email_xac_nhan(thong_tin_ve: str) -> str:
        # Giả sử logic phức tạp để gửi email xác nhận
        return f"Đã gửi email xác nhận: {thong_tin_ve}"


class DatVe:
    def __init__(self):
        self.he_thong_tim_chuyen_bay = HeThongTimChuyenBay()
        self.he_thong_dat_ve = HeThongDatVe()
        self.he_thong_thanh_toan = HeThongThanhToan()
        self.he_thong_email = HeThongEmail()

    def dat_ve_may_bay(self, diem_di: str, diem_den: str, so_tien: float) -> str:
        # Sử dụng các hệ thống con thông qua Mặt Tiền để thực hiện toàn bộ quy trình

        ket_qua = list()
        ket_qua.append(self.he_thong_tim_chuyen_bay.tim_chuyen_bay(diem_di, diem_den))
        ket_qua.append(self.he_thong_dat_ve.dat_ve(ket_qua[-1]))
        ket_qua.append(self.he_thong_thanh_toan.thanh_toan(so_tien))
        ket_qua.append(self.he_thong_email.gui_email_xac_nhan(ket_qua[-2]))
        return "\n".join(ket_qua)


def ma_khach_hang():
    mat_tien = DatVe()
    ket_qua = mat_tien.dat_ve_may_bay("Hà Nội", "TP.HCM", 2000000)
    print(ket_qua)


if __name__ == "__main__":
    ma_khach_hang()

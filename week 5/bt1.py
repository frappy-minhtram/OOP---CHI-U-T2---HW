import math

class HangHoa:
    def __init__(self, san_pham, ma_sp, so_luong, don_gia):
        self.san_pham = san_pham
        self.ma_sp = ma_sp
        self.so_luong = so_luong
        self.don_gia = don_gia

    @property
    def san_pham(self):
        return self.__san_pham
    
    @san_pham.setter
    def san_pham(self, value):
        if not value or value.strip() == "":
            print("Tên sản phẩm không được để trống!")
        self.__san_pham = value

    @property
    def ma_sp(self):
        return self.__ma_sp
    
    @ma_sp.setter
    def ma_sp(self, value):
        if not value or value.strip() == "":
            print("Mã sản phẩm không được để trống!")
        self.__ma_sp = value

    @property
    def so_luong(self):
        return self.__so_luong
    
    @so_luong.setter
    def so_luong(self, value):
        if value < 0:
            print("Số lượng không được âm!")
        self.__so_luong = value

    @property
    def don_gia(self):
        return self.__don_gia
    
    @don_gia.setter
    def don_gia(self, value):
        if value <= 0:
            print("Đơn giá phải lớn hơn 0!")
        self.__don_gia = value

    def tinh_tien(self):
        return self.__so_luong * self.__don_gia

    def __str__(self):
        return f"Tên: {self.__san_pham:15} | Mã: {self.__ma_sp:5} | SL: {self.__so_luong:3} | Đơn giá: {self.__don_gia:10,.0f} VNĐ"

class HangDienMay(HangHoa):
    def __init__(self, san_pham, ma_sp, so_luong, don_gia, bao_hanh, dien_ap, cong_suat):
        super().__init__(san_pham, ma_sp, so_luong, don_gia)
        self.__bao_hanh = bao_hanh
        self.__dien_ap = dien_ap
        self.__cong_suat = cong_suat

    def __str__(self):
        return super().__str__() + f" | BH: {self.__bao_hanh}T | Áp: {self.__dien_ap}V | CS: {self.__cong_suat}W"

class HangSanhSu(HangHoa):
    def __init__(self, san_pham, ma_sp, so_luong, don_gia, nguyen_lieu):
        super().__init__(san_pham, ma_sp, so_luong, don_gia)
        self.__nguyen_lieu = nguyen_lieu

    def __str__(self):
        return super().__str__() + f" | Nguyên liệu: {self.__nguyen_lieu}"

class HangThucPham(HangHoa):
    def __init__(self, san_pham, ma_sp, so_luong, don_gia, ngay_sx, ngay_hh):
        super().__init__(san_pham, ma_sp, so_luong, don_gia)
        self.__ngay_sx = ngay_sx
        self.__ngay_hh = ngay_hh

    def __str__(self):
        return super().__str__() + f" | NSX: {self.__ngay_sx} | HSD: {self.__ngay_hh}"

if __name__ == "__main__":
    print("                                 *** HỆ THỐNG QUẢN LÝ HÀNG HÓA ***           ")
    
    try:
        khoHang = [
            HangDienMay("Tủ Lạnh LG", "DM01", 10, 15000000, 24, 220, 150),
            HangSanhSu("Bình Hoa Cổ", "SS05", 2, 5000000, "Gốm Chu Đậu"),
            HangThucPham("Sữa Tươi", "TP12", 100, 25000, "01/10/2023", "10/10/2023")
        ]

        for item in khoHang:
            print(item)
            print(f"   => Tổng tiền: {item.tinh_tien()} VNĐ")

    except ValueError as e:
        print(f"Lỗi nhập liệu: {e}")

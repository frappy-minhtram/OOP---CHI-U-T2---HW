class Hero:
    def __init__(self,ten,vu_khi,mau_sac):
            self.ten = ten
            self.vu_khi = vu_khi
            self.mau_sac = mau_sac
    def the_hien(self):
         return f"{self.ten} - {self.vu_khi} - {self.mau_sac}"
A = Hero("sieu_nhan_A","kiem","red")
B = Hero("sieu_nhan_B","khien","blue")
print(A.the_hien())
print(B.the_hien())


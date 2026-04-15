class Hero:
    def __init__(self, name, power, weapon):
        self.name = name
        self.power = power
        self.weapon = weapon

    def __str__(self):
        return f"Tên: {self.name} | SM: {self.power} | Vũ khí: {self.weapon}"

list_sn = []

try:
    total = int(input("** Nhập số lượng siêu nhân : ** "))
    for i in range(total):
        print(f"Nhập siêu nhân thứ {i+1}:")
        name = input(" - Tên: ")
        power = input(" - Sức mạnh: ")
        weapon = input(" - Vũ khí: ")
        hero = Hero(name, power, weapon)
        list_sn.append(hero)
except ValueError:
    print("Nhập số nguyên cho số lượng!")

while True:
    print("DANH SÁCH QUẢN LÝ SIÊU NHÂN")
    print("1. Hiển thị danh sách")
    print("2. Thêm siêu nhân mới")
    print("3. Xóa siêu nhân")
    print("4. Thoát")
    
    try:
        choices = int(input("Nhập yêu cầu của bạn: "))
    except ValueError:
        print("Nhập từ 1 đến 4!")
        continue
    
    if choices == 1:
        print("Danh sách hiện tại")
        if not list_sn:
            print("Danh sách đang trống!")
        else:
            for sn in list_sn:
                print(sn) 
    elif choices == 2:
        name = input("- Tên siêu nhân: ")
        power = input("- Sức mạnh: ")
        weapon = input("- Vũ khí: ")
        list_sn.append(Hero(name, power, weapon))
        print("Đã thêm thành công!")

    elif choices == 3:
        ten_xoa = input("Nhập tên siêu nhân muốn xóa: ")
        truoc_khi_xoa = len(list_sn)
        list_sn = [sn for sn in list_sn if sn.name.lower() != ten_xoa.lower()]
        
        if len(list_sn) < truoc_khi_xoa:
            print(f"Đã xóa siêu nhân '{ten_xoa}' thành công!")
        else:
            print("Không tìm thấy siêu nhân có tên này.")

    elif choices == 4:
        print("Chương trình kết thúc. Chào cậu!")
        break
    else:
        print("Lựa chọn không hợp lệ!")

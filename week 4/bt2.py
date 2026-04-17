import math
import copy

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self): return self.__x
    @x.setter
    def x(self, value):self.__x = value 

    @property
    def y(self): return self.__y
    @y.setter
    def y(self, value): self.__y = value

class LineSegment:
    def __init__(self, d1=None, d2=None):
        if isinstance(d1, Point) and isinstance(d2, Point):
            self.__d1 = copy.deepcopy(d1)
            self.__d2 = copy.deepcopy(d2)
        elif d1 is None and d2 is None:   
            self.__d1 = Point(8, 0)
            self.__d2 = Point(1, 0)
        else:
            self.__d1 = Point(0, 0)
            self.__d2 = Point(0, 0)

    def length(self):
        return math.sqrt((self.__d2.x - self.__d1.x)**2 + (self.__d2.y - self.__d1.y)**2)

def input_data():
    lines = []
    try:
        num_str = input("Nhap so doan thang: ")
        if not num_str: return lines
        num = int(num_str)
        
        for i in range(num):
            print(f"Nhap doan thang thu {i+1} ")
            x1, y1 = map(int, input("Nhap x1, y1 (cach nhau bang dau phay): ").split(','))
            x2, y2 = map(int, input("Nhap x2, y2 (cach nhau bang dau phay): ").split(','))
            
            lines.append(LineSegment(Point(x1, y1), Point(x2, y2)))
    except (ValueError, IndexError):
        print("Nhap dung dinh dang (so,so)!")
    return lines

def find_max_length(lines):
    if not lines: return 0
    return max(line.length() for line in lines)

if __name__ == "__main__":
    list_line = input_data()
    if list_line:
        max_l = find_max_length(list_line)
        print(f"\n=> Do dai doan thang dai nhat la: {max_l:.2f}")
    else:
        print("Khong ton tai!")

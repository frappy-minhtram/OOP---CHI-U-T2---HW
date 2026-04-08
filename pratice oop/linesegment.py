from point import Point 
import copy

class LineSegment: 
    def __init__(self, *args): 
        if len(args) == 0: 
            self.__d1 = Point(8,5)
            self.__d2 = Point(1,0) 

        elif len(args) == 2: 
            if isinstance(args[0], Point) and isinstance(args[1], Point): 
                self.__d1 = args[0]
                self.__d2 = args[1]

        elif len(args) == 4: 
            if isinstance(args[0], int): 
                self.__d1 = Point(args[0], args[1])
                self.__d2 = Point(args[2], args[3]) 

        elif len(args) == 1: 
            if isinstance(args[0], LineSegment): 
                self.__d1 = copy.deepcopy(args[0].__d1)
                self.__d2 = copy.deepcopy(args[0].__d2)

    def __str__(self): 
        return "[(%d,%d), (%d,%d)]" % (self.__d1.x, self.__d1.y, self.__d2.x, self.__d2.y)

    def getD1(self):
        return self.__d1

    def getD2(self): 
        return self.__d2

    def setD1D2(self, point1, point2): 
        self.__d1 = point1
        self.__d2 = point2

from prettytable import PrettyTable


class Room:
    def __init__(self, x, y, z):
        self.square = 2 * z * (x + y)
        self.wd = []

    def add_wd(self, w, h, name='unk'):
        """for adding doors and windows """
        self.wd.append(WinDoor(w, h, name))

    def work_surface(self):
        """ for calculating "working" squares """
        new_square = self.square
        for i in self.wd:
            new_square -= i.square
        return new_square


class WinDoor:
    def __init__(self, x, y, name="unk"):
        self.x = x
        self.y = y
        self.name = name
        self.square = x * y

    def __repr__(self):
        return f'{self.name} {self.x}x{self.y}'


class WallPaper:
    """" To calculate the square of wallpaper """

    def __init__(self, wwp, lwp):
        self.wwp = wwp
        self.lwp = lwp

    def square_wp(self) -> float:
        summwp = 0
        summwp += self.wwp * self.lwp
        return summwp


class Calculate:
    """ for calculating the number of wallpaper rolls for an object """

    def __init__(self, calc):
        self.calc = calc

    def division(self) -> float:
        self.calc += room_1.work_surface() / wp.square_wp()
        return self.calc


room_1 = Room(3, 3, 2.5)
room_1.add_wd(1.5, 1.5, 'big_win')
room_1.add_wd(1, 2, 'Fiodoor')
room_1.add_wd(0.20, 0.40, 'schel')
wp = WallPaper(0.50, 10)
cl = Calculate(0)

myTable = PrettyTable(["Name WinDoor", "Square Room", "WorkSurface", "WallPaper Square", "Calculate"])
myTable.add_row([room_1.wd, room_1.square, room_1.work_surface(), wp.square_wp(), cl.division()])
print(myTable)

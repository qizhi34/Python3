# Defines two classes, Point() and Triangle().
# An object for the second class is created by passing named arguments,
# point_1, point_2 and point_3, to its constructor.
# Such an object can be modified by changing one point, two or three points
# thanks to the method change_point_or_points().
# At any stage, the object maintains correct values
# for perimeter and area.
#
# Written by *** and Eric Martin for COMP9021


from math import sqrt


class PointError(Exception):
    def __init__(self, message):
        self.message = message


class Point():
    def __init__(self, x=None, y=None):
        if x is None and y is None:
            self.x = 0
            self.y = 0
        elif x is None or y is None:
            raise PointError('Need two coordinates, point not created.')
        else:
            self.x = x
            self.y = y

    # Possibly define other methods


class TriangleError(Exception):
    def __init__(self, message):
        self.message = message


class Triangle:
    def __init__(self, *, point_1, point_2, point_3):

        if self.on_one_line(point_1, point_2, point_3):
            raise TriangleError('Incorrect input, triangle not created.')
        else:
            self.point_1 = point_1
            self.point_2 = point_2
            self.point_3 = point_3

        # Replace pass above with your code

    def change_point_or_points(self, *, point_1=None, point_2=None, point_3=None):
        if point_1 is not None:
            point_1_tmp = point_1
        else:
            point_1_tmp = self.point_1
        if point_2 is not None:
            point_2_tmp = point_2
        else:
            point_2_tmp = self.point_2
        if point_3 is not None:
            point_3_tmp = point_3
        else:
            point_3_tmp = self.point_3
        if self.on_one_line(point_1_tmp, point_2_tmp, point_3_tmp):
            print('Incorrect input, triangle not modified.')
        else:
            self.point_1 = point_1_tmp
            self.point_2 = point_2_tmp
            self.point_3 = point_3_tmp

    # Possibly define other methods
    @property
    def perimeter(self):
        return self.side_length(self.point_2, self.point_1) + self.side_length(self.point_3,
                                                                               self.point_1) + self.side_length(
            self.point_3, self.point_2)

    @property
    def area(self):
        return sqrt(self.perimeter / 2 * (self.perimeter / 2 - self.side_length(self.point_2, self.point_1))
                    * (self.perimeter / 2 - self.side_length(self.point_3, self.point_1))
                    * (self.perimeter / 2 - self.side_length(self.point_3, self.point_2)))

    def side_length(self, point_1, point_2):
        return sqrt(pow(point_2.x - point_1.x, 2) + pow(point_2.y - point_1.y, 2))

    def on_one_line(self, point_1, point_2, point_3):
        return (point_2.y - point_1.y) * (point_3.x - point_2.x) == \
               (point_3.y - point_2.y) * (point_2.x - point_1.x) \
               and (point_2.y - point_1.y) * (point_3.x - point_1.x) == \
               (point_3.y - point_1.y) * (point_2.x - point_1.x)

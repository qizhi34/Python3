#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# QQ:707573223 有问题可以联系我

from quiz_6 import *

p1=Point(1,2)
p2=Point(4,8)
p3=Point(3,5)
triangle = Triangle(point_1 = p1, point_2 = p2, point_3 = p3)
p0=Point(0,0)
p3=Point(0,4)
triangle.change_point_or_points(point_3=p3,point_1=p0)
triangle.change_point_or_points(point_2=Point(4,0))
triangle.change_point_or_points(point_3=Point(4,0))
print(triangle.perimeter)
# p1 = Point(1,2)
# p2 = Point(4,8)
# p3 = Point(2,4)
#
# # triangle = Triangle(point_1 = p1, point_2 = p2, point_3 = p3)
#
# p3 = Point(3,5)
# triangle = Triangle(point_1 = p1, point_2 = p2, point_3 = p3)
# print(triangle.perimeter)
# print(triangle.area)
# p3 = Point(2,4)
# triangle.change_point_or_points(point_3 = p3)
# print(triangle.perimeter)
# print(triangle.area)
#
# p0 = Point(0,0)
# p3 = Point(0,4)
# triangle.change_point_or_points(point_3 = p3, point_1 = p0)
# print(triangle.perimeter)
# print(triangle.area)
# triangle.change_point_or_points(point_2 = Point(4,0))
# print(triangle.area)
# # triangle.change_point_or_points(point_3 = Point(4,0))
# triangle.change_point_or_points(point_3 = Point(4,8))
# print(triangle.area)
# print(triangle.perimeter)
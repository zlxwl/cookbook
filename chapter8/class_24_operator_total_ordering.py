# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : class_24_operator_total_ordering.py
# Time       ：2022/4/9 22:00
# Author     ：Zhong Lei
"""
from functools import total_ordering


class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.square_feet = self.length * self.width

@total_ordering
class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    @property
    def living_space_footage(self):
        return sum([room.square_feet for room in self.rooms])

    def __eq__(self, other):
        return self.living_space_footage == other.living_space_footage

    def __lt__(self, other):
        return self.living_space_footage < other.living_space_footage

    def __str__(self):
        return '{}: {} square foot {}'.format(self.name, self.living_space_footage, self.style)


if __name__ == '__main__':
    h1 = House('h1', 'Cape')
    h1.add_room(Room('Master Bedroom', 14, 21))
    h1.add_room(Room('Living Room', 18, 20))
    h1.add_room(Room('Kitchen', 12, 16))
    h1.add_room(Room('Office', 12, 12))
    print(h1.living_space_footage)

    h2 = House('h2', 'Ranch')
    h2.add_room(Room('Master Bedroom', 14, 21))
    h2.add_room(Room('Living Room', 18, 20))
    h2.add_room(Room('Kitchen', 12, 16))

    h3 = House('h3', 'Split')
    h3.add_room(Room('Master Bedroom', 14, 21))
    h3.add_room(Room('Living Room', 18, 20))
    h3.add_room(Room('Office', 12, 16))
    h3.add_room(Room('Kitchen', 15, 17))

    houses = [h1, h2, h3]

    print('Is h1 bigger than h2?', h1 > h2)
    print('Is h2 smaller than h3?', h2 < h3)
    print('Is h2 greater than h1?', h2 > h1)

    print('which one is biggest?', max(houses))
    print('which one is smallest?', min(houses))

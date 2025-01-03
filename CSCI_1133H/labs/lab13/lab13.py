# Lab 13
# Rohit Poduval
from turtle import *


class Shape:
    def __init__(self, x=0, y=0, color="#000000"):
        self.x = x
        self.x = y
        self._color = color
    
    def set_fill_color(self, str_color):
        self._color = str_color
    
    def set_filled(self, is_filled):
        self.__is_filled = is_filled
    
    def is_filled(self):
        return self.__is_filled


class Circle(Shape):
    def __init__(self, x=0, y=0, radius=1, color="#000000"):
        super().__init__(x, y, color)
        self.__radius = radius
    
    def draw(self, turtle_object):
        if self.__is_filled:
            turtle_object.fillcolor(self._color)
            turtle_object.begin_fill()
            turtle_object.circle(self.__radius)
            turtle_object.end_fill()
        else:
            # Works?
            turtle_object.penup()
            turtle_object.goto(self.x, self.y)
            turtle_object.circle(self.__radius)  # Necessary?
            turtle_object.pendown()
            turtle_object.circle(self.__radius)  


def main():
    T = turtle.Turtle()
    C = Circle(0, 0, 100, "red")

    C.draw()


if __name__ == "__main__":
    main()


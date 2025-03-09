from graphics import Line, Point

class Cell():
    def __init__(self, top_left, bottom_right, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = top_left.x
        self.__x2 = bottom_right.x
        self.__y1 = top_left.y
        self.__y2 = bottom_right.y
        self.__win = window
        self.center = Point((self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) / 2)


    def draw(self):
        if self.has_left_wall:
            left_wall = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(left_wall)
        if self.has_right_wall:
            right_wall = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(right_wall)
        if self.has_top_wall:
            top_wall = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(top_wall)
        if self.has_bottom_wall:
            bottom_wall = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(bottom_wall)

    def draw_move(self, to_cell, undo=False):
        line = Line(self.center, to_cell.center)
        if not undo:
            self.__win.draw_line(line, 'red')
        else:
            self.__win.draw_line(line, 'gray')

        pass
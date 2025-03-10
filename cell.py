from graphics import Line, Point

class Cell():
    def __init__(self, top_left, bottom_right, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = top_left.x
        self._x2 = bottom_right.x
        self._y1 = top_left.y
        self._y2 = bottom_right.y
        self._win = window
        self.center = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        self.visited = False

    def draw(self):
        left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))

        if self._win is None:
            return
        if self.has_left_wall:
            self._win.draw_line(left_wall)
        else:
            self._win.draw_line(left_wall, 'white')
        if self.has_right_wall:
            self._win.draw_line(right_wall)
        else:
            self._win.draw_line(right_wall, 'white')
        if self.has_top_wall:
            self._win.draw_line(top_wall)
        else:
            self._win.draw_line(top_wall, 'white')
        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall)
        else:
            self._win.draw_line(bottom_wall, 'white')

    def draw_move(self, to_cell, undo=False):
        line = Line(self.center, to_cell.center)
        if not undo:
            self._win.draw_line(line, 'red')
        else:
            self._win.draw_line(line, 'gray')

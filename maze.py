from cell import Cell
from graphics import Point
from time import sleep

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x = x1
        self.y = y1
        self.rows = num_rows
        self.columns = num_cols
        self.col_width = cell_size_x
        self.row_height = cell_size_y
        self.window = win
        self._cells = []

        if (self.x + self.columns * self.col_width) > self.window._width or (self.y + self.rows * self.row_height) > self.window._height:
            raise Exception("Maze with given dimensions is too large for the current window.")

        self._create_cells()

    def _create_cells(self):
        for i in range(self.columns):
            column = []
            for j in range(self.rows):
                top_left = Point(self.x + (i * self.col_width), self.y + (j * self.row_height))
                bottom_right = Point(self.x + ((i + 1) * self.col_width), self.y + ((j + 1) * self.row_height))
                cell = Cell(top_left, bottom_right, self.window)
                column.append(cell)
            self._cells.append(column)
        
        for i in range(self.columns):
            for j in range(self.rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self.window.redraw()
        sleep(0.02)
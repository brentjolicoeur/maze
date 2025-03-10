from cell import Cell
from graphics import Point, Line
from time import sleep
import random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x = x1
        self._y = y1
        self._rows = num_rows
        self._columns = num_cols
        self._col_width = cell_size_x
        self._row_height = cell_size_y
        self._window = win
        self._cells = []
        if seed:
            random.seed(seed)

        if self._window:
            if (self._x + self._columns * self._col_width) > self._window._width or (self._y + self._rows * self._row_height) > self._window._height:
                raise Exception("Maze with given dimensions is too large for the current window.")

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._columns):
            column = []
            for j in range(self._rows):
                top_left = Point(self._x + (i * self._col_width), self._y + (j * self._row_height))
                bottom_right = Point(self._x + ((i + 1) * self._col_width), self._y + ((j + 1) * self._row_height))
                cell = Cell(top_left, bottom_right, self._window)
                column.append(cell)
            self._cells.append(column)
        
        for i in range(self._columns):
            for j in range(self._rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._window is None:
            return
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self._window.redraw()
        sleep(0.02)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._columns - 1][self._rows - 1].has_bottom_wall = False
        self._draw_cell(self._columns - 1, self._rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            possible_visits = []
            #check if cell to left has been visited
            if i - 1 > 0 and not self._cells[i-1][j].visited:
                possible_visits.append(self._cells[i-1][j])
            #check if cell to right has been visited
            if i + 1 < self._columns and not self._cells[i+1][j].visited:
                possible_visits.append(self._cells[i+1][j])
            #check if cell above has been visited
            if j - 1 > 0 and not self._cells[i][j-1].visited:
                possible_visits.append(self._cells[i][j-1])
            #check if cell below has been visited
            if j + 1 < self._rows and not self._cells[i][j+1].visited:
                possible_visits.append(self._cells[i][j+1])
            
            if possible_visits == []:
                self._draw_cell(i, j)
                return
            
            next = random.choice(possible_visits)

            if i - 1 > 0 and next == self._cells[i-1][j]:
                #break right wall of west cell, left wall of current cell, and move to it
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
                self._break_walls_r(i -1, j)
            if i + 1 < self._columns and next == self._cells[i+1][j]:
                #break left walll of east cell, right wall of current cell, and move to it
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
                self._break_walls_r(i + 1, j)
            if j - 1 > 0 and next == self._cells[i][j-1]:
                #break bottom wall of north cell, top wall of current cell, and move to it
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
                self._break_walls_r(i, j - 1)
            if j + 1 < self._rows and next == self._cells[i][j+1]:
                #break top wall of south cell, bottom wall of current cell, and move to it
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
                self._break_walls_r(i, j + 1)

    def _reset_cells_visited(self):
        for i in range(self._columns):
            for j in range(self._rows):
                self._cells[i][j].visited = False

    def solve(self):
        solved = self._solve_r(0, 0)
        return solved

    def _solve_r(self, i, j):
        goal = self._cells[self._columns - 1][self._rows -1]

        self._animate()
        self._cells[i][j].visited = True

        if self._cells[i][j] == goal:
            return True
        
        #check west
        if i - 1 > 0 and not self._cells[i][j].has_left_wall and not self._cells[i-1][j].visited:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            on_path = self._solve_r(i - 1, j)
            if on_path:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)
        #check east
        if i + 1 < self._columns and not self._cells[i][j].has_right_wall and not self._cells[i+1][j].visited:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            on_path = self._solve_r(i + 1, j)
            if on_path:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)
        #check north
        if j - 1 > 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j-1].visited:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            on_path = self._solve_r(i, j - 1)
            if on_path:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)
        #check south
        if j + 1 < self._rows and not self._cells[i][j].has_bottom_wall and not self._cells[i][j+1].visited:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            on_path = self._solve_r(i, j+1)
            if on_path:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)
        
        return False
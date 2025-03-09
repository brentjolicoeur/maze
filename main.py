from graphics import Window, Point, Line
from cell import Cell

def main():
    win = Window(800, 600)
    
    cell1 = Cell(Point(10, 10), Point(50, 50), win)
    cell2 = Cell(Point(50, 10), Point(90, 50), win)
    cell3 = Cell(Point(100, 100), Point(500, 500), win)
    cell3.has_bottom_wall = False
    cell4 = Cell(Point(250, 200), Point(400, 400), win)
    cell4.has_top_wall = False
    cell4.has_left_wall = False



    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell4.draw()

    cell1.draw_move(cell2)
    cell2.draw_move(cell3, True)

    win.wait_for_close()

if __name__ == "__main__":
    main()
from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    point1 = Point(5, 5)
    point2 = Point(50,50)
    point3 = Point(200, 100)
    point4 = Point(100, 350)
    line1 = Line(point1, point2)
    line2 = Line(point3, point4)
    line3 = Line(point1, point3)
    line4 = Line(point2, point4)

    win.draw_line(line1, "blue")
    win.draw_line(line2, "green")
    win.draw_line(line3, "red")
    win.draw_line(line4, "black")

    win.wait_for_close()

if __name__ == "__main__":
    main()
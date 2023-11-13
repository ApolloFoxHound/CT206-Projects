# Working With Functions (simple)
# URL: https://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/04_Functions1/Tesselations/
# Tessellations

import turtle
import time
import math

turtle.speed(10)

SIZE = 500
HALF_SIZE = SIZE / 2

# Colors choice for user
COLOR_MENU = ("Blue", "Green", "Orange", "Pink", "Purple", "Red", "Yellow")


def get_num_hexagons():
    # Ask user for # Hexagons between 4 and 20
    num_str = input("Please enter a number of hexagons per row: ")
    while not num_str.isdigit() or not (4 <= int(num_str) <= 20):
        num_str = input("It should be between 4 and 20.  Please try again: ")
    return int(num_str)


def even(num):
    # If Number is Even
    if num % 2 == 0:
        return True
    else:
        return False


def get_color_choice():
    choice = input("Please enter your choice: ").lower()
    while True:
        n = len(choice)
        if choice:
            if choice == "red"[:n]:
                return "red"
            elif choice == "blue"[:n]:
                return "blue"
            elif choice == "green"[:n]:
                return "green"
            elif choice == "yellow"[:n]:
                return "yellow"
            elif choice == "orange"[:n]:
                return "orange"
            elif choice == "purple"[:n]:
                return "purple"
            elif choice == "pink"[:n]:
                return "pink"
        prompt = "'{}' is not a legal choice.  Please try again: ".format(choice)
        choice = input(prompt).lower()


def draw_hexagon(x, y, side_len, pen, color):
    # Draws Hexagon
    pen.fillcolor(color)
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.begin_fill()
    hding = 30
    for n in range(6):
        pen.setheading(hding)
        pen.forward(side_len)
        hding += 60
    pen.end_fill()


def hex_color(r, c, c1, c2):
    # Tile Colors
    # r : row number
    # c : column number
    # c1, c2 : colors

    if r % 4 == 0:
        if even(c):
            return c1
        else:
            return c2
    elif r % 4 == 1:
        if even(c):
            return c1
        else:
            return c2
    elif r % 4 == 3:
        if even(c):
            return c2
        else:
            return c1
    else:
        if even(c):
            return c2
        else:
            return c1


def hexa_color(r, c, c1, c2):
    if even(r + c):
        return c1
    else:
        return c2


def main():
    # shape = get_choice("sdt", SHAPE_PRMT)
    print(COLOR_MENU)
    color1 = get_color_choice()
    color2 = get_color_choice()
    num = get_num_hexagons()
    x_spacing = SIZE / num
    slen = x_spacing / (2 * math.cos(math.pi / 6))
    y_spacing = slen + math.sin(math.pi / 6) * slen

    y = -HALF_SIZE
    for row in range(num):

        if even(row):
            x = -HALF_SIZE + (x_spacing / 2)
        else:
            x = -HALF_SIZE + x_spacing

        for col in range(num):
            # print(x, y)              # debugging
            color = hexa_color(row, col, color1, color2)
            draw_hexagon(x, y, slen, turtle, color)
            x += x_spacing

        y += y_spacing

    time.sleep(10)
    turtle.bye()


main()

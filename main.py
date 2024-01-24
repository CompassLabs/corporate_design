# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# from pysvg.builders import *
# from pysvg.parser import parse

import svgwrite
import math


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press ⌘F8 to toggle the breakpoint.


def create_compass_gradient(dwg, dir="horizontal"):
    gradient = dwg.linearGradient((0, 0), (1, 0), id="my_gradient")
    gradient.add_stop_color(offset=0, color="#FFD75F")
    gradient.add_stop_color(offset=0.5, color="#FF67C3")
    gradient.add_stop_color(offset=1, color="#6BD6E3")
    return gradient


def create_circles(circle_center, circle_radius, stroke_width):
    # Circles
    outer_circle = dwg.circle(
        center=circle_center, r=circle_radius, fill=gradient.get_paint_server()
    )
    inner_circle = dwg.circle(
        center=circle_center, r=circle_radius - stroke_width, fill="red"
    )
    return outer_circle, inner_circle

def create_compass_needle(
    center, length, width_ratio=6 / 16, stroke_width=50, angle=45
):
    # Diamonds
    # Calculate the coordinates of the diamond's vertices
    x_center, ycenter = center
    height = length
    width = height * width_ratio

    a = height / 2
    b = width / 2

    points1 = [
        (x_center, ycenter - a),  # Top point
        (x_center + b, ycenter),  # Right point
        (x_center, ycenter + a),  # Bottom point
        (x_center - b, ycenter),  # Left point
    ]
    polygon1 = dwg.polygon(points1, fill="green")
    polygon1.rotate(angle, center=center)

    print(a, b)

    h = math.cos(math.atan(b / a)) * b
    print("h", h)

    cosalpha = h / b
    tanalpha = b / a
    bnew = (h - stroke_width) / cosalpha
    anew = bnew / tanalpha
    print("new", anew, bnew)

    deltax = 60
    deltay = 160
    points2 = [
        (x_center, ycenter - anew),  # Top point
        (x_center + bnew, ycenter),  # Right point
        (x_center - bnew, ycenter),  # Left point
        # (points1[0][0], points1[0][1]+deltay),  # Top point
        # (points1[1][0]-deltax, points1[1][1]),    # Right point
        # (points1[3][0]+deltax, points1[3][1]),    # Left point
    ]
    polygon2 = dwg.polygon(points2, fill="yellow")
    polygon2.rotate(angle, center=center)

    return polygon1, polygon2


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    dwg = svgwrite.Drawing("CompassLogo.svg", size=(1000, 1000))

    gradient = create_compass_gradient(dwg)
    dwg.add(gradient)

    # Define outer circle attributes
    circle_radius = 500
    circle_center = (500, 500)
    stroke_width = 60
    needle_length_factor = 5 / 6.5
    needle_width_ration = 4.5 / 12
    needle_angle = 45


    outer_circle, inner_circle = create_circles(circle_center, circle_radius, stroke_width)
    dwg.add(outer_circle)
    dwg.add(inner_circle)

    polygon1, polygon2 = create_compass_needle(
        center=circle_center,
        length=(circle_radius - stroke_width) * 2 * needle_length_factor,
        width_ratio=needle_width_ration,
        stroke_width=stroke_width,
        angle=needle_angle,
    )
    dwg.add(polygon1)
    dwg.add(polygon2)

    # Save the SVG file
    dwg.save()

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# from pysvg.builders import *
# from pysvg.parser import parse

import svgwrite



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.




# def filled_gradient_circle(svg, cx, cy, r):
    # d = Defs()
    #
    # lg = LinearGradient()
    # lg.set_id("compass_gradient")
    # s = Stop(offset="0%")
    # s.set_stop_color('#FFD75F')
    # s.set_stop_opacity(1)
    # lg.addElement(s)
    #
    # s = Stop(offset="50%")
    # s.set_stop_color('#FF67C3')
    # s.set_stop_opacity(1)
    # lg.addElement(s)
    #
    # s = Stop(offset="100%")
    # s.set_stop_color('#6BD6E3')
    # s.set_stop_opacity(1)
    # lg.addElement(s)
    # d.addElement(lg)
    #
    # oh = ShapeBuilder()
    # # oh.createCircle()
    # e = oh.createCircle(cx=cx, cy=cy, r=r, fill="url(#compass_gradient)", stroke=None)
    #
    # svg.addElement(d)
    # svg.addElement(e)




def create_compass_gradient(dwg, dir="horizontal"):
    gradient = dwg.linearGradient((0, 0), (1, 0), id="my_gradient")
    gradient.add_stop_color(offset=0, color='#FFD75F')
    gradient.add_stop_color(offset=0.5, color='#FF67C3')
    gradient.add_stop_color(offset=1, color='#6BD6E3')
    return gradient



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dwg = svgwrite.Drawing('output.svg')

    gradient = create_compass_gradient(dwg)
    dwg.add(gradient)

    #dwg = svgwrite.Drawing('ring.svg', profile='tiny')

    # Define outer circle attributes
    circle_radius = 500
    circle_center = (500, 500)
    width=50


    #Circles
    outer_circle = dwg.circle(center=circle_center, r=circle_radius, fill=gradient.get_paint_server())
    inner_circle = dwg.circle(center=circle_center, r=circle_radius-width, fill='red')
    dwg.add(outer_circle)
    dwg.add(inner_circle)


    #Diamonds
    # Calculate the coordinates of the diamond's vertices
    x_center, ycenter = circle_center
    height=(circle_radius-3*width)*2
    width=height*6/16

    points1 = [
        (x_center, ycenter - height / 2),  # Top point
        (x_center + width / 2, ycenter),    # Right point
        (x_center, ycenter + height / 2),   # Bottom point
        (x_center - width / 2, ycenter),    # Left point
    ]
    polygon1 = dwg.polygon(points1, fill='green')
    polygon1.rotate(45, center=(500, 500))
    dwg.add(polygon1)


    deltax=60
    deltay=160
    points2 = [
        (points1[0][0], points1[0][1]+deltay),  # Top point
        (points1[1][0]-deltax, points1[1][1]),    # Right point
        # (points1[2][0], points1[2][1]-deltay),   # Bottom point
        (points1[3][0]+deltax, points1[3][1]),    # Left point
    ]
    polygon2=dwg.polygon(points2, fill='yellow')
    polygon2.rotate(45, center=(500, 500))
    dwg.add(polygon2)


    # Save the SVG file
    dwg.save()

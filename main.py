import svgwrite
import math

def create_compass_gradient(dwg, dir="horizontal"):
    gradient = dwg.linearGradient((0, 0), (1, 0), id="my_gradient")
    gradient.add_stop_color(offset=0, color="#FFD75F")
    gradient.add_stop_color(offset=0.5, color="#FF67C3")
    gradient.add_stop_color(offset=1, color="#6BD6E3")
    return gradient


def create_circles(circle_center, circle_radius, stroke_width):
    outer_circle = dwg.circle(
        center=circle_center, r=circle_radius, fill=gradient.get_paint_server()
    )
    inner_circle = dwg.circle(
        center=circle_center, r=circle_radius - stroke_width, fill="#1e1c2d"
    )
    return outer_circle, inner_circle

def create_compass_needle(
    center, length, width_ratio=6 / 16, stroke_width=50, angle=45
):
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



    h = math.cos(math.atan(b / a)) * b
    cosalpha = h / b
    tanalpha = b / a
    bnew = (h - stroke_width) / cosalpha
    anew = bnew / tanalpha
    points2 = [
        (x_center, ycenter - anew),  # Top point
        (x_center + bnew, ycenter),  # Right point
        (x_center - bnew, ycenter),  # Left point
    ]
    polygon2 = dwg.polygon(points2, fill="yellow")

    polygon1.rotate(angle, center=center)
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
    stroke_width = 50
    needle_length_factor = 5 / 6.5
    needle_width_ration = 4.5 / 12
    needle_angle = 45


    outer_circle, inner_circle = create_circles(circle_center, circle_radius, stroke_width)
    mask = dwg.mask(id="myMask", maskUnits="userSpaceOnUse", maskContentUnits="userSpaceOnUse")
    mask.add(inner_circle)
    # Apply the mask to the rectangle
    outer_circle['mask'] = mask.get_funciri()
    dwg.add(outer_circle)

    # dwg.add(outer_circle)
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

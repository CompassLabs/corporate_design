import svgwrite


def create_mask(drawing):
    mask = drawing.mask(id="myMask", maskUnits="objectBoundingBox")

    # Create a white rectangle as the mask shape
    mask.add(drawing.rect(insert=(0, 0), size=("100%", "100%"), fill="white"))

    return mask


def main():
    # Create an SVG drawing
    drawing = svgwrite.Drawing("output.svg")

    # Create a rectangle to be masked
    rect = drawing.rect(insert=(10, 10), size=(50, 50), fill="blue")

    # Create the mask
    mask = create_mask(drawing)

    # Apply the mask to the rectangle
    rect['mask'] = mask.get_funciri()

    # Add the masked rectangle to the drawing
    drawing.add(rect)

    # Save the SVG file
    drawing.save()


if __name__ == "__main__":
    main()

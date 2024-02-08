import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask, SquareGradiantColorMask, VerticalGradiantColorMask

from dataclasses import dataclass


@dataclass
class QRcode:
    name: str
    url: str


def create_code(URL, destination, mode=qrcode.constants.ERROR_CORRECT_Q):
    qr = qrcode.QRCode(
        error_correction=mode,
        box_size=20,  # Adjust this value to make the QR code bigger or smaller
        border=2,
    )
    qr.add_data(URL)

    img_2 = qr.make_image(
        image_factory=StyledPilImage,
        color_mask=VerticalGradiantColorMask(
            # back_color=(255, 255, 255),
            # center_color=(255, 103, 195),
            # edge_color=(30, 28, 45)
            back_color = (100,100, 100),
            #center_color = (255, 255, 255),
            #edge_color = (238, 150, 201),
            top_color=(248, 221, 243),
            bottom_color=(255, 255, 255)
        ))
    with open(destination, "wb") as f:
        img_2.save(f)


codes = [
    QRcode(name="ethdenvermerch5", url="https://link.compasslabs.ai/ethdenvermerch")
]

for code in codes:
    create_code(code.url, f"output/{code.name}_q.png", mode=qrcode.constants.ERROR_CORRECT_Q)
    create_code(code.url, f"output/{code.name}_h.png", mode=qrcode.constants.ERROR_CORRECT_H)
    create_code(code.url, f"output/{code.name}_m.png", mode=qrcode.constants.ERROR_CORRECT_M)
    create_code(code.url, f"output/{code.name}_l.png", mode=qrcode.constants.ERROR_CORRECT_L)
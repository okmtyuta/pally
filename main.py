from Hex import Hex
from RGB import RGB

from colr import color

h = "#28a745"
percents = [-1, -0.5, -0.2, -0.1, 0, 0.1, 0.2, 0.5, 1]

if __name__ == "__main__":
    hex = Hex(h)

    def _lighter(percent):
        return hex.lightness(percent)._hex

    for hexcolor in list(map(_lighter, percents)):
        print(hexcolor, color("       ", back=hexcolor))

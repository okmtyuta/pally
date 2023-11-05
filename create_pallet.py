from Hex import Hex
from colr import color

h = "#28a745"
p = [-1, -0.5, -0.2, -0.1, 0, 0.1, 0.2, 0.5, 1]

def create_pallet(hex, percents):
  _hex = Hex(hex)
  def _lighter(percent):
    return _hex.lightness(percent)._hex

  return list(map(_lighter, percents))

def show_pallet(pallet):
    for hexcolor in pallet:
      print(hexcolor, color("     ", back=hexcolor))

if __name__ == "__main__":
  show_pallet(create_pallet(h, p))
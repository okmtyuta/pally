from Hex import Hex
from RGB import RGB
from colr import color

h = "#28a745"
r = (40, 167, 69)
amounts = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

hex_colors = {
  "success": "#28a745",
  "danger": "#dc3545",
  "warning": "#ffc107",
  "info": "#17a2b8"
}

def create_pallet(hex_colors, amounts):
  pallet = {}
  for hex_color_name, hex_color_code in hex_colors.items():
    _hex = Hex(hex_color_code)
    def _hex_lighter(amount):
      return _hex.lighten(amount)._hex
    def _rgb_lighter(amount):
      return _hex.lighten(amount)._rgb
    
    _lighten_hexes = list(map(_hex_lighter, amounts))
    lighten_hexes = {
      f"--hex-color-{hex_color_name}": _lighten_hexes[0],
      f"--hex-color-{hex_color_name}-lighten1": _lighten_hexes[1],
      f"--hex-color-{hex_color_name}-lighten2": _lighten_hexes[2],
      f"--hex-color-{hex_color_name}-lighten3": _lighten_hexes[3],
      f"--hex-color-{hex_color_name}-lighten4": _lighten_hexes[4],
      f"--hex-color-{hex_color_name}-lighten5": _lighten_hexes[5],
      f"--hex-color-{hex_color_name}-lighten6": _lighten_hexes[6],
      f"--hex-color-{hex_color_name}-lighten7": _lighten_hexes[7],
      f"--hex-color-{hex_color_name}-lighten8": _lighten_hexes[8],
      f"--hex-color-{hex_color_name}-lighten9": _lighten_hexes[9],
      f"--hex-color-{hex_color_name}-lighten10": _lighten_hexes[10],
    }

    _lighten_rgbs = list(map(_rgb_lighter, amounts))
    lighten_rgbs = {
      f"--rgb-color-{hex_color_name}": _lighten_rgbs[0],
      f"--rgb-color-{hex_color_name}-lighten1": _lighten_rgbs[1],
      f"--rgb-color-{hex_color_name}-lighten2": _lighten_rgbs[2],
      f"--rgb-color-{hex_color_name}-lighten3": _lighten_rgbs[3],
      f"--rgb-color-{hex_color_name}-lighten4": _lighten_rgbs[4],
      f"--rgb-color-{hex_color_name}-lighten5": _lighten_rgbs[5],
      f"--rgb-color-{hex_color_name}-lighten6": _lighten_rgbs[6],
      f"--rgb-color-{hex_color_name}-lighten7": _lighten_rgbs[7],
      f"--rgb-color-{hex_color_name}-lighten8": _lighten_rgbs[8],
      f"--rgb-color-{hex_color_name}-lighten9": _lighten_rgbs[9],
      f"--rgb-color-{hex_color_name}-lighten10":_lighten_rgbs[10],
    }

    pallet[hex_color_name] = {
      "hex": lighten_hexes,
      "rgb": lighten_rgbs
    }

  return pallet

def write_pallet(pallet):
  with open("color.css", mode="w") as f:
    f.write(":root {\n")
    for color_name in pallet.keys():
      f.write(f"\t/* {color_name} */\n")

      _hexes = pallet[color_name]["hex"]
      for prefixed_color_name, color_code in _hexes.items():
        f.write(f"\t{prefixed_color_name}: {color_code};\n")
      _rgbs = pallet[color_name]["rgb"]
      for prefixed_color_name, color_code in _rgbs.items():
        f.write(f"\t{prefixed_color_name}: {color_code[0]}, {color_code[1]}, {color_code[2]};\n")
    f.write("}")
if __name__ == "__main__":
  pallet = create_pallet(hex_colors, amounts)
  write_pallet(pallet)
import re
from RGB import RGB


def is_hex(hex: str) -> bool:
    hex_regexp = re.compile(r"^#[0-9a-fA-F]{6}$")
    if not hex_regexp.match(hex):
        return False

    return True


class NotHexError(Exception):
    pass


class Hex:
    def __init__(self, hex: str) -> None:
        if not is_hex(hex):
            raise NotHexError(hex)
        self._hex = hex
        self._rgb = self.to_rgb_tuple()

    def to_rgb_tuple(self):
        red = int(self._hex[1:3], 16)
        green = int(self._hex[3:5], 16)
        blue = int(self._hex[5:7], 16)

        return (red, green, blue)
    
    def lighten(self, amount: float):
        return Hex(RGB(self._rgb).lighten(amount).to_hex_string())

    def darken(self, amount: float):
        return Hex(RGB(self._rgb).darken(amount).to_hex_string())
    
    def saturate(self, amount):
        return Hex(RGB(self._rgb).saturate(amount).to_hex_string())

def is_rgb(rgb: tuple[int, int, int]) -> bool:
    if not len(rgb) == 3:
        return False

    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]

    if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
        return False

    return True


class NotRGBError(Exception):
    pass

class TooLongTargetError(Exception):
    pass


def complement_zero(target: str):
    if len(target) > 2:
        raise TooLongTargetError()
    
    if len(target) == 2 :
        return target
    
    return f"0{target}"

class RGB:
    def __init__(self, rgb: tuple[int, int, int]) -> None:
        if not is_rgb(rgb):
            raise NotRGBError()
        self._rgb = rgb
        self._hex_string = self.to_hex_string()

    def to_hex_string(self):
        red, green, blue = self._rgb

        _hex_red = complement_zero(format(red, "x"))
        _hex_blue = complement_zero(format(blue, "x"))
        _hex_green = complement_zero(format(green, "x"))

        hex_string = f"#{_hex_red}{_hex_green}{_hex_blue}"

        return hex_string
    
    def darken(self, amount: float):
        def _darken(color: int) -> int:
            _color = int(color * (1 - amount))
            if _color > 255:
                return 255
            elif _color < 0:
                return 0
            return _color
        
        return RGB(tuple(map(_darken, self._rgb)))
    
    def lighten(self, amount: float):
        def _lighten(color: int) -> int:
            _color = int((255 - color) * amount + color)
            if _color > 255:
                return 255
            elif _color < 0:
                return 0
            return _color
        
        return RGB(tuple(map(_lighten, self._rgb)))

    def saturate(self, amount):
        red, green, blue = self._rgb

        if (max(self._rgb) == red):
            _rgb = tuple(map(int, (red, green * amount, blue * amount)))
            return RGB(_rgb)
        elif (max(self._rgb) == green):
            _rgb = tuple(map(int, (red * amount, green, blue * amount)))
            return RGB(_rgb)
        else:
            _rgb = tuple(map(int, (red * amount, green * amount, blue)))
            return RGB(_rgb)
        

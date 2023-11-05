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


class RGB:
    def __init__(self, rgb: tuple[int, int, int]) -> None:
        if not is_rgb(rgb):
            raise NotRGBError()
        self._rgb = rgb
        self._hex_string = self.to_hex_string()

    def to_hex_string(self):
        red, green, blue = self._rgb
        _hex_red = format(red, "x")
        hex_red = _hex_red if len(_hex_red) == 2 else f"0{_hex_red}"

        _hex_blue = format(blue, "x")
        hex_blue = _hex_blue if len(_hex_blue) == 2 else f"0{_hex_blue}"

        _hex_green = format(green, "x")
        hex_green = _hex_green if len(_hex_green) == 2 else f"0{_hex_green}"

        hex_string = f"#{hex_red}{hex_green}{hex_blue}"

        return hex_string

    def lightness(self, percent: float):
        def _lighten(color: int) -> int:
            _color = int(color + 255 * percent)
            if _color > 255:
                return 255
            elif _color < 0:
                return 0
            return _color

        return RGB(tuple(map(_lighten, self._rgb)))

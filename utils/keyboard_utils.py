import time
from usb.device.keyboard import KeyCode

SPECIAL_KEYS = {
    "!": (KeyCode.N1, True),
    "@": (KeyCode.N2, True),
    "#": (KeyCode.N3, True),
    "$": (KeyCode.N4, True),
    "%": (KeyCode.N5, True),
    "^": (KeyCode.N6, True),
    "&": (KeyCode.N7, True),
    "*": (KeyCode.N8, True),
    "(": (KeyCode.N9, True),
    ")": (KeyCode.N0, True),

    "-": (KeyCode.MINUS, False),
    "_": (KeyCode.MINUS, True),
    "=": (KeyCode.EQUAL, False),
    "+": (KeyCode.EQUAL, True),

    "[": (KeyCode.OPEN_BRACKET, False),
    "{": (KeyCode.OPEN_BRACKET, True),
    "]": (KeyCode.CLOSE_BRACKET, False),
    "}": (KeyCode.CLOSE_BRACKET, True),

    "\\": (KeyCode.BACKSLASH, False),
    "|": (KeyCode.BACKSLASH, True),

    ";": (KeyCode.SEMICOLON, False),
    ":": (KeyCode.SEMICOLON, True),

    "'": (KeyCode.QUOTE, False),
    '"': (KeyCode.QUOTE, True),

    ",": (KeyCode.COMMA, False),
    "<": (KeyCode.COMMA, True),

    ".": (KeyCode.DOT, False),
    ">": (KeyCode.DOT, True),

    "/": (KeyCode.SLASH, False),
    "?": (KeyCode.SLASH, True),

    "`": (KeyCode.GRAVE, False),
    "~": (KeyCode.GRAVE, True),
}


class KeyboardWriter:
    def __init__(self, keyboard):
        self.kb = keyboard

    def type_char(self, char, sleep):
        if char.isupper():
            keys = [KeyCode.LEFT_SHIFT, getattr(KeyCode, char)]

        elif char.islower():
            keys = [getattr(KeyCode, char.upper())]

        elif char.isdigit():
            keys = [getattr(KeyCode, f"N{char}")]

        elif char == " ":
            keys = [KeyCode.SPACE]

        elif char in SPECIAL_KEYS:
            key, shift = SPECIAL_KEYS[char]
            keys = [key]

            if shift:
                keys.insert(0, KeyCode.LEFT_SHIFT)

        else:
            return

        self.kb.send_keys(keys)
        time.sleep_ms(sleep)
        self.kb.send_keys([])
        time.sleep_ms(sleep)


    def type_string(self, text, sleep = 0):
        for char in text:
            self.type_char(char, sleep)
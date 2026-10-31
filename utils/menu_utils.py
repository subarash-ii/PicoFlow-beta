from ssd1306 import SSD1306_I2C


def draw_list_menu(display: SSD1306_I2C, options: list[str], selected: int, start_index: int, stop_index: int):
    if selected >= stop_index:
        start_index += 1
        stop_index += 1

    if selected < start_index:
        start_index -= 1
        stop_index -= 1

    display.fill(0)

    display.text("Main menu: ", 0, 0)

    for i, option in enumerate(options[start_index:stop_index]):
        x = 8
        y = 10 + i * 10
        text = option

        if len(option) > 15:
            truncated_text = option[0:15]
            text = truncated_text[:-2] + ".."

        if selected - start_index == i:
            display.fill_rect(0, y - 1, 128, 10, 1)
            display.text(">", 0, y, 0)
            display.text(text, x, y, 0)
        else:
            display.text(text, x, y, 1)

    display.show()

    return start_index, stop_index


def draw_script_running_menu(display: SSD1306_I2C, name: str):
    display.fill(0)

    text = f"RUN: {name}"

    if len(text) > 14:
        truncated_text = text[0:15]
        text = truncated_text[:-2] + ".."

    y = 28
    x = (128 - len(text) * 8) // 2

    display.text(text, x, y, 1)

    exit_text = "[ Exit ]"
    exit_x = (128 - len(exit_text) * 8) // 2
    exit_y = y + 8 + 8 # 8px is text height and 8px margin

    display.fill_rect(exit_x, exit_y - 1, len(exit_text) * 8, 10, 1)
    display.text(exit_text, exit_x, exit_y, 0)

    display.show()
from pynput import mouse
from pynput.keyboard import Controller, Key

top_pixel = 20

keyboard = Controller()


def volume_up():
    keyboard.press(Key.media_volume_up)
    keyboard.release(Key.media_volume_up)


def volume_down():
    keyboard.press(Key.media_volume_down)
    keyboard.release(Key.media_volume_down)


def on_scroll(x, y, dx, dy):
    if y < top_pixel:
        if dy < 0:
            volume_down()
        else:
            volume_up()


with mouse.Listener(on_scroll=on_scroll) as listener:
    listener.join()

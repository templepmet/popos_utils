import os

from Xlib import X, display
from Xlib.ext import record
from Xlib.protocol import rq

Screen_resolution = (1920, 1080)
top_pixel = 20
volume_rate = 4


def volume_up():
    os.system(f"pactl set-sink-volume 0 +{volume_rate}% & pid=$!")


def volume_down():
    os.system(f"pactl set-sink-volume 0 -{volume_rate}% & pid=$!")


record_dpy = display.Display()

ctx = record_dpy.record_create_context(
    0,
    [record.AllClients],
    [
        {
            "core_requests": (0, 0),
            "core_replies": (0, 0),
            "ext_requests": (0, 0, 0, 0),
            "ext_replies": (0, 0, 0, 0),
            "delivered_events": (0, 0),
            "device_events": (X.KeyPress, X.MotionNotify),
            "errors": (0, 0),
            "client_started": False,
            "client_died": False,
        }
    ],
)


def record_callback(reply):
    data = reply.data
    while len(data):
        event, data = rq.EventField(None).parse_binary_value(
            data, record_dpy.display, None, None
        )

        if event.type == X.ButtonPress:
            if event.root_y < top_pixel:
                if event.detail == 4:  # wheel up
                    volume_up()
                elif event.detail == 5:  # wheel down
                    volume_down()


record_dpy.record_enable_context(ctx, record_callback)

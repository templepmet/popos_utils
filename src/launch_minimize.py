import subprocess
import sys
import time

command = sys.argv[1]
window_name = str.capitalize(command)
subprocess.Popen(["/bin/bash", "-c", command])


def read_wlist(w_name):
    try:
        l = subprocess.check_output(["wmctrl", "-l"]).decode("utf-8").splitlines()
        return [w.split()[0] for w in l if w_name in w][0]
    except (IndexError, subprocess.CalledProcessError):
        return None


cnt = 0
while cnt < 30:
    window = read_wlist(window_name)
    time.sleep(0.1)

    if window is not None:
        subprocess.Popen(["xdotool", "windowminimize", window])
        break
    time.sleep(1)
    cnt += 1

from pynput.mouse import Listener
import subprocess
import threading

def run_vbs():
    try:

        subprocess.Popen(["wscript", "D:\\Programming\\HackClick\\hack.vbs"])
    except Exception as e:
        print("Failed to run VBS:", e)

def run_bsod():
    try:
        subprocess.Popen(["python", "D:\\Programming\\HackClick\\fake_bsod.py"])
    except Exception as e:
        print("Failed to show fake BSOD:", e)

def on_click(x, y, button, pressed):
    if pressed:
        if button.name == 'left':
            print("Left click → fake BSOD")
            threading.Thread(target=run_bsod).start()
        elif button.name == 'right':
            print("Right click → run VBS")
            threading.Thread(target=run_vbs).start()

with Listener(on_click=on_click) as listener:
    listener.join()

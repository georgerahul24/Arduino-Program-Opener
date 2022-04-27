from pynput import keyboard
import pyautogui
import os
def on_press(key):
    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    print(k)
    if k=='menu':
        os.system('start firefox')
    if k=='ctrl_r':
        pyautogui.hotkey('winleft', 'd')
        

listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys

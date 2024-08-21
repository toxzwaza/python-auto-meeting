import pyautogui
import time

try:
    # 2秒待機してからキー操作を開始
    time.sleep(2)

    # Windows + Alt + R を押す
    pyautogui.hotkey('win', 'alt', 'r')
except Exception as e:
    print(e)
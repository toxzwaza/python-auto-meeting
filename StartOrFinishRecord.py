import pyautogui
import time

try:
    print('録画を実行します。')
    # 2秒待機してからキー操作を開始
    time.sleep(2)

    # Windows + Alt + R を押す
    pyautogui.hotkey('win', 'alt', 'r')
    print('キー操作を終了しました。')
except Exception as e:
    print(e)
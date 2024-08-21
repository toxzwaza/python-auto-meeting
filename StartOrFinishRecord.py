import pyautogui
import time

try:
    print('録画を実行します。')
    
    # 2秒待機してからキー操作を開始
    time.sleep(5)

    # Windows + Alt + R を押す
    pyautogui.hotkey('win', 'alt', 'r')
    
    print('キー操作を実行しました。')
    
    time.sleep(2)
except Exception as e:
    print(e)
import keyboard
import time

try:
    print('録画開始・終了を実行します。')
    
    # 2秒待機してからキー操作を開始
    time.sleep(5)

    # Windows + Alt + R を押す
    keyboard.press_and_release('ctrl+shift+F12')
    
    print('キー操作を実行しました。')
    
    time.sleep(2)
except Exception as e:
    print(e)
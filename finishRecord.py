import keyboard
import time
import psutil

def kill_process_by_name_part(name_part):
    for proc in psutil.process_iter(['pid', 'name']):
        if name_part.lower() in proc.info['name'].lower():
            proc.kill()
            print(f"Process {proc.info['name']} (PID: {proc.info['pid']}) has been terminated.")
            

try:
    print('録画開始・終了を実行します。')
    # 2秒待機してからキー操作を開始
    time.sleep(2)

    # 例: タスク名に 'Teams' が含まれているプロセスを閉じる
    kill_process_by_name_part('Teams')
    
    
    # 2秒待機してからキー操作を開始
    time.sleep(5)

    # Windows + Alt + R を押す
    keyboard.press_and_release('ctrl+shift+F12')
    
    print('キー操作を実行しました。')
    
    time.sleep(2)
except Exception as e:
    print(e)
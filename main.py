import sys
import xml.etree.ElementTree as ET
import datetime
from message import windowDialog
is_success = True
try:
    # コマンドライン引数を三つ取得
    if len(sys.argv) != 4:
        print("使用法: python main.py <arg1> <arg2> <arg3>")
        sys.exit(1)

    # 日付
    arg1 = sys.argv[1]
    # 開始時刻
    arg2 = sys.argv[2]
    # URL
    arg3 = sys.argv[3]

    # print(f"引数1: {arg1}")
    # print(f"引数2: {arg2}")
    # print(f"引数3: {arg3}")

    reserveDateTime = arg1 + ' ' + arg2

    date_obj = datetime.datetime.strptime(reserveDateTime, '%Y/%m/%d %H:%M')
    formatted_date = date_obj.strftime('%Y-%m-%dT%H:%M:%S')
    formatted_nextyear_date = (date_obj + datetime.timedelta(days=365)).strftime('%Y-%m-%dT%H:%M:%S')

    reserveURL = arg3
    if 'teams' in reserveURL:
        reserveURL = reserveURL.replace('https://teams.microsoft.com','')
        reserveURL = f'/c start "" "msteams:{ reserveURL }"'

    elif 'zoom' in reserveURL:
        print('zoom実行')

    # print(reserveURL)
    # sys.exit()

    # ファイルを読み込む
    import os
    # 絶対パスでファイルを読み込む
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(script_dir, 'template.xml')
    tree = ET.parse(template_path)
    root = tree.getroot()

    # 名前空間を定義
    namespaces = {'ns': 'http://schemas.microsoft.com/windows/2004/02/mit/task'}


    # StartBoundaryタグを編集
    start_boundary = root.find('.//ns:StartBoundary', namespaces)
    start_boundary.text = formatted_date  # 新しい日付と時間に置き換える

    end_boundary = root.find('.//ns:EndBoundary', namespaces)
    end_boundary.text = formatted_nextyear_date

    # Argumentsタグを編集
    arguments = root.find('.//ns:Arguments', namespaces)
    arguments.text = reserveURL

    # 新しいXMLファイルとして保存
    tree.write('reserve.xml', encoding='UTF-16')
    
except Exception as e:
    is_success = False
    print(e)

if is_success:
    windowDialog('正常終了')
else:
    windowDialog('XML作成失敗')
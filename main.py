import sys
import xml.etree.ElementTree as ET
import datetime
from message import windowDialog
import os

def main(arg1, arg2, arg3):
    is_success = True
    try:

        reserveDateTime = arg1 + ' ' + arg2
        date_obj = datetime.datetime.strptime(reserveDateTime, '%Y/%m/%d %H:%M')
        formatted_date = date_obj.strftime('%Y-%m-%dT%H:%M:%S')
        formatted_nextyear_date = (date_obj + datetime.timedelta(days=365)).strftime('%Y-%m-%dT%H:%M:%S')
            
        if arg3 == 'startRecord':
            createXML(formatted_date, formatted_nextyear_date, 'StartRecord')
        elif arg3 == 'finishRecord':
            createXML(formatted_date, formatted_nextyear_date, 'FinishRecord')
        else:
            reserveURL = arg3
            if 'teams' in reserveURL:
                reserveURL = reserveURL.replace('https://teams.microsoft.com','')
                reserveURL = f'/c start "" "msteams:{ reserveURL }"'

            elif 'zoom' in reserveURL:
                print('zoom実行')
                

            createXML(formatted_date,formatted_nextyear_date, reserveURL)
    except Exception as e:
        is_success = False
        print(e)

    if is_success:
        windowDialog('正常終了')
    else:
        windowDialog('XML作成失敗')
    
def createXML(formatted_date, formatted_nextyear_date, cmd):

    # 絶対パスでファイルを読み込む
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if cmd == 'StartRecord' :
        template_path = os.path.join(script_dir, 'StartTemplate.xml')
    elif cmd == 'FinishRecord':
        template_path = os.path.join(script_dir, 'FinishTemplate.xml')
    else :
        template_path = os.path.join(script_dir, 'template.xml')

    # ファイル確認
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"テンプレートファイルが見つかりません: {template_path}")
        return

    try:
        with open(template_path, 'rb') as file:
            content = file.read()
            if content.startswith(b'\xff\xfe'):
                content = content.decode('utf-16')
            else:
                content = content.decode('utf-8-sig')
            tree = ET.ElementTree(ET.fromstring(content))  # UTF-8 BOMを考慮してデコード

    except ET.ParseError as e:
        print(e)
        return



    root = tree.getroot()
    
    print(formatted_date)
    print(formatted_nextyear_date)
    print(cmd)
    print(template_path)


    # 名前空間を定義
    namespaces = {'ns': 'http://schemas.microsoft.com/windows/2004/02/mit/task'}


    # StartBoundaryタグを編集
    start_boundary = root.find('.//ns:StartBoundary', namespaces)
    start_boundary.text = formatted_date  # 新しい日付と時間に置き換える

    end_boundary = root.find('.//ns:EndBoundary', namespaces)
    end_boundary.text = formatted_nextyear_date

    if cmd != 'none' :
        # Argumentsタグを編集
        arguments = root.find('.//ns:Arguments', namespaces)
        arguments.text = cmd
    
    # 絶対パスで保存
    output_path = os.path.join(script_dir, 'reserve.xml' if cmd == 'StartRecord' or cmd == 'FinishRecord' else 'reserveRecord.xml')
    tree.write(output_path, encoding='UTF-8')
        




if __name__ == '__main__':
            # コマンドライン引数を三つ取得
    if len(sys.argv) != 4:
        print("引数が設定されていません。")
        sys.exit(1)

    # 日付
    arg1 = sys.argv[1]
    # 開始時刻
    arg2 = sys.argv[2]
    # URL
    arg3 = sys.argv[3]
        
    main(arg1, arg2, arg3)
import requests
import json

url = "http://shortcutgame.kumaa9.dev/api/keymap/"

for letter in range(ord('A'), ord('Z')+1):
    data = {
        "key": f"{chr(letter)}",
        "usable": False,
        }

        # JSONデータを辞書からJSON文字列に変換
    json_data = json.dumps(data)

        # POSTリクエストを送信
    response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

        # # レスポンスを表示
    print(response.text)
    # print(json_data)

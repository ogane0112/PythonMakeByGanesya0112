from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

MET_API_URL = "https://collectionapi.metmuseum.org/public/collection/v1/objects"

@app.route('/')
def index():
    return display_random_artwork()

@app.route('/reroll')
def reroll():
    return display_random_artwork()

def display_random_artwork():
    # ランダムなアートワークのIDを取得
    response = requests.get(MET_API_URL)
    if response.status_code != 200:
        return "APIの呼び出しに失敗しました。"

    object_ids = response.json().get("objectIDs")
    image_url = ""
    valid_image = False

    # 画像が存在し、アクセス可能なアートワークを見つけるまで繰り返す
    while not valid_image:
        random_id = random.choice(object_ids)

        # アートワークの詳細情報を取得
        art_detail = requests.get(f"{MET_API_URL}/{random_id}")
        if art_detail.status_code != 200:
            continue

        art_data = art_detail.json()
        image_url = art_data.get("primaryImage")

        # 画像のURLが存在し、アクセス可能であるかを確認
        if image_url and image_url.startswith("http"):
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                valid_image = True

    title = art_data.get("title")
    artist = art_data.get("artistDisplayName")

    return render_template('index.html', title=title, artist=artist, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)



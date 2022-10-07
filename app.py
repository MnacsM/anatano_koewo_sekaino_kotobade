import uuid

import requests
from flask import Flask  # Flaskと、HTMLをレンダリングするrender_templateをインポート
from flask import render_template, request

import settings

app = Flask(__name__)  # Flask の起動


def microsoft_translator(input, source, target):
    # Add your subscription key and endpoint
    subscription_key = settings.AP  # YOUR API KEY
    endpoint = "https://api.cognitive.microsofttranslator.com"

    # Add your location, also known as region. The default is global.
    # This is required if using a Cognitive Services resource.
    location = "japaneast"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': source,
        'to': target
    }
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': input
    }]

    apirequest = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = apirequest.json()

    trans_texts = [response[0]['translations'][i]['text'] for i in range(9)]
    # print(trans_texts)

    return trans_texts


@app.route('/')  # localhost:50000/を起動した際に実行される
def index():
    return render_template('index.html')  # index.htmlをレンダリングする


# 入力値の表示ページ
@app.route('/result', methods=['GET', 'POST'])
def result():

    trans_target = [
        "en", "de", "es", "fr", "it", "ko", "zh-chs", "ru", "th"
    ]
    # syntesis_target = [
    #     "en-US", "de-DE", "es-ES", "fr-FR", "it-IT", "ko-KR", "zh-CN", "ru-RU", "th-TH"
    # ]

    # country_target = [
    #     "アメリカ", "ドイツ", "スペイン", "フランス", "イタリア", "韓国", "中国", "ロシア", "タイ"
    # ]

    # index.htmlのinputタグ内にあるname属性itemを取得し、textに格納した
    text = request.form.get('text')

    # もしPOSTメソッドならresult.htmlに値textと一緒に飛ばす
    if request.method == 'POST':
        trans_texts = microsoft_translator(text, 'ja', trans_target)
        print(trans_texts)

        # return か...
        return render_template(
            'result.html',
            input_text=text,
            trans_text0=trans_texts[0],
            trans_text1=trans_texts[1],
            trans_text2=trans_texts[2],
            trans_text3=trans_texts[3],
            trans_text4=trans_texts[4],
            trans_text5=trans_texts[5],
            trans_text6=trans_texts[6],
            trans_text7=trans_texts[7],
            trans_text8=trans_texts[8],
        )

    # POSTメソッド以外なら、index.htmlに飛ばす
    else:
        return render_template('index.html')


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=334, ssl_context=('openssl/server.crt', 'openssl/server.key'), threaded=True, debug=True)

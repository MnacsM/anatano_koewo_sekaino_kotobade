# あなたの声を世界の言葉で　〜WEBプログラムで同時通訳〜

（オープンキャンパス展示用のデモシステム）

あなたの声をマイクで聞き取り，各国の言葉に言い換え，スピーカーからその声を発話する，ブラウザで動作するWEBプログラムです．

既存技術の組み合わせでシンプルな実装を実現しています．

- 音声認識/合成: [Web Speech API](https://developer.mozilla.org/ja/docs/Web/API/Web_Speech_API)
- 翻訳: [Microsoft Azure Translator API](https://azure.microsoft.com/ja-jp/services/cognitive-services/translator/#overview)
  - API_KEY が必要．取得して，.env.sample を参考に .env ファイルを作成して記入
- Webページ: python, Flask

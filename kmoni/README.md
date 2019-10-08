# kmoni-uttr

## 内容
  [強震モニタ](http://www.kmoni.bosai.go.jp/) を起動し、
  EEW受信時に読み上げるプログラムです。
  
  読み上げには `Open JTalk` か `WebSpeechAPI` を利用します。

## 準備

- 実行には以下のパッケージが必要です。
  - selenium
  - time
  - subprocess
- [seleniumのchrome用ドライバをダウンロード](https://sites.google.com/a/chromium.org/chromedriver/downloads)し、
  `kmoni_uttr.py` あるいは `kmoni_uttr_jtalk.py` 内の
  'DRIVER_PATH' にパスを格納してください。
- Open JTalk 版を利用する場合
  （ChromeなどWebSpeechAPI対応ブラウザが利用できない場合）、
  Open JTalkの導入が必要です。
  - [こちらのQuita記事がすこぶるわかりやすくておすすめです。](https://qiita.com/kkoba84/items/b828229c374a249965a9)

## 実行方法
python コマンドで python3系 が動く場合の実行例です。
環境によっては python3 コマンドで実行してください。

- WebSpeechAPI読み上げ版
```
python kmoni-uttr.py
```

- Open JTalk読み上げ版
```
python kmoni-uttr_jtalk.py
```

# 謝辞
- NIED 様
  - 強震モニタを運営してくださりありがとうございます。
- kkoba84 様
  - Open JTalkの実装で
  [こちらのQuita記事](https://qiita.com/kkoba84/items/b828229c374a249965a9)
  に助けられました。ありがとうございます。

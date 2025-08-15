# AI Tuber

AI Tuber を作って配信するためのリポジトリ。

[阿部由延.AITuber を作ってみたら生成 AI プログラミングがよくわかった件.日経 BP.2023](https://www.amazon.co.jp/AITuber%E3%82%92%E4%BD%9C%E3%81%A3%E3%81%A6%E3%81%BF%E3%81%9F%E3%82%89%E7%94%9F%E6%88%90AI%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E3%81%8C%E3%82%88%E3%81%8F%E3%82%8F%E3%81%8B%E3%81%A3%E3%81%9F%E4%BB%B6-%E9%98%BF%E9%83%A8-%E7%94%B1%E5%BB%B6-sald_ra/dp/4296070789)

上記を参考にしました。

## 開発手順

1. `python3 -m venv .venv`を実行し仮想環境を作成する

2. `source .venv/bin/activate`を実行し仮想環境を実行する

3. `pip install -r requirements.txt`で依存パッケージをインストールする

4. `.env.template`をコピーして`.env`を作成し、必要なクレデンシャルを埋める

## 配信手順

1. OBS で画面右下「配信の管理」を押す(ここでエラーが出た場合は OAuth の認可期限が切れている可能性があるので、OBS の「設定」→「配信」からアカウントの再接続を行う)

2. 配信タイトルを設定し、プライバシーを「限定公開」にして「配信を作成」を押す(このとき「配信を作成して配信開始」を押さないこと)

3. [YouTube Studio](https://studio.youtube.com/channel/UCl7bYJTnpvbYebYCZ8wpMeA/videos/live?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D)から該当の配信枠の管理画面を開き、`video_id` (URL の `video/`以下)をコピーし、以下に貼り付ける:

   - .env ファイルの `YOUTUBE_VIDEO_ID`
   - コメント欄用ブラウザソースの参照する URL の末尾(`v=`の部分)

4. Style-Bert-VITS2 フォルダ直下で仮想環境に入り、`python3 server_fastapi.py`で Style Bert VITS2 のサーバーを起動する

5. OBS の「音声ミキサー」下にある歯車マーク(「オーディオの詳細プロパティ」)を開き、「マイク」の「音声モニタリング」を「モニターと出力」に変更する

6. 仮想環境上で`python3 run.py` を実行し、実際に配信画面からコメントして回答生成・読み上げが行われるかテストする

7. OBS の「マイク」の「音声モニタリング」を「モニターオフ」に戻す

8. 「配信の管理」から先ほど作成した既存の配信を選択し、配信開始する

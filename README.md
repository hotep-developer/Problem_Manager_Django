# ウェブアプリのテスト for y.y

## はじめに

y.yに向けてのDjangoプロジェクトです。

とりあえず，動きそうなものを作ってみた。

テストとかはやってないから，その道の人に怒られそうだけど，，，

もし良かったらダウンロードしてみてね。


## 動作環境

自分が動かしていた環境

- macOS 12.3 (Monterey)
- Python 3.9.10
- Django 4.0.3
- ネットに接続できる環境

他はきりがないので省略

Windows環境では試していないので，動作は保証しません。

## インストール方法

基本的にmacOSであると想定しています。

1. 緑色の`Code`ボタンから`Download ZIP`でダウンロード
1. 解凍したフォルダを好きなところに配置(外部ストレージなど)
1. `manage.py`と同じディレクトリに仮想環境`.venv`を作成しアクティブにする。

   (Windows ではコマンドが違うみたい)

    ```bash
    $ python3 -m venv .venv
    $ source .venv/bin/activate
    ```

2. 必要なパッケージをインストールする。(今回は`requirements.text`を使ってインストール)

    ```bash
    (.venv) $ pip install -r requirements.text
    ```

## 使い方

1. 仮想環境に入る

    ```bash
    $ source .venv/bin/activate
    ```

1. スーパーユーザーを作成

    ```bash
    (.venv) $ python manage.py createsuperuser
    ```

1. マイグレーションする

    ```bash
    (.venv) $ python manage.py makemigrations
    (.venv) $ python manage.py migrate
    ```

1. ローカルサーバーを立ち上げる

    ```bash
    (.venv) $ python manage.py runserver
    # または
    (.venv) $ python manage.py runserver 127.0.0.1:8000
    ```

1. http://127.0.0.1:8000 にアクセスすれば動作するはずです。

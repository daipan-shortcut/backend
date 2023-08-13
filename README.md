# backend_API

## Windows の場合

```bash
# 仮想環境の作成
python -m venv .venv

# 仮想環境に入る
.venv/Scripts/Activate

# 仮想環境から抜ける
deactivate

# 必要なライブラリのインストール
pip3 install -r requirements.txt

#プロジェクトの作成
django-admin startproject config

#アプリケーションの作成
python manage.py startapp <アプリケーション名>

# マイグレーション
python manage.py makemigrations <アプリケーション名>
python manage.py migrate <アプリケーション名>

# サーバの起動
python manage.py runserver

## スーパーユーザの作成
python manage.py createsuperuser

## データの挿入(Windows PowerShell)
psql -f C:\パスを記載\vending-machine\backend\sql\<ファイル名>.sql -U postgres -d <db名>
```

## Mac の場合

```bash
# 仮想環境の作成
python3 -m venv .venv

# 仮想環境に入る
. .venv/bin/activate

# 仮想環境から抜ける
deactivate

#プロジェクトの作成
django-admin startproject config

#アプリケーションの作成
python manage.py startapp API

# 必要なライブラリのインストール
pip3 install -r requirements.txt

# マイグレーション
python manage.py makemigrations
python manage.py migrate

# サーバの起動
python manage.py runserver

## スーパーユーザの作成
python manage.py createsuperuser


## データの挿入()
psql -f /パスを記載/vending-machine/backend/sql/<ファイル名>.sql -U postgres -d <db名>

```


# 共通設定
## データベース
PostgreSQL 15.0
APIディレクトリに.envファイルを作成し、以下のように記述する。
```
DATABASE_ENGINE="django.db.backends.postgresql_psycopg2"
DATABASE_URL='postgres://postgres:<自身のパスワード>@localhost:5432/u22_api'

```
# 各種バージョン
python 3.11.0(3.9.xでも動作確認済み)  
django 4.1.7  
djangorestframework 3.14.0  
django-environ 0.9.0  
django-cors-headers 3.13.0  
psycopg2-binary 2.9.5  
requests 2.28.1  
Pillow 9.2.0  
pytz 2022.7.1  
PostgreSQL 15.0
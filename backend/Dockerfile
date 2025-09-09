# Python公式イメージ
FROM python:3.11-slim

# 作業ディレクトリ
WORKDIR /code

# 依存関係をコピーしてインストール
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# プロジェクトコードをコピー
COPY . .

# 開発用コマンド
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

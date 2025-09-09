# 済
プロジェクト作成
マイグレーション実施
スーパーユーザー作成
簡易的なログイン、ログアウト機能の実装
posetgresとの連携

# Todo
noteアプリの実装
　ソート機能

ログアウト時にキャッシュ削除 + 戻るボタン押下でホームに戻れないようにする

docker-compose build --no-cache
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate

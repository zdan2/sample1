import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# DB接続設定
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///local.db')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Userモデルの定義
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

# トップページ
@app.route('/')
def index():
    users = User.query.all()
    if not users:
        return 'ユーザーが登録されていません'
    return ', '.join(user.name for user in users)

if __name__ == '__main__':
    app.run(debug=True)

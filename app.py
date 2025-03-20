import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

# 環境変数DATABASE_URLを使ってDBに接続する設定
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///local.db')
db = SQLAlchemy(app)

# 例のモデル
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

@app.route('/')
def index():
    users = User.query.all()
    return ', '.join([user.name for user in users])

migrate=Migrate(app,db)

if __name__ == '__main__':
    app.run()

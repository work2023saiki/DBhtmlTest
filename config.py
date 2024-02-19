# Flaskアプリケーションとデータベースの動作に関する設定
import MySQLdb, os

class Config(object):
    # CSRFやセッションで使用
    SECRET_KEY = "z2PMiQVn"       #推測されにくいランダムな文字列
    # 警告対策
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # DB設定
    SQLALCHEMY_DATABASE_URI = 'mysql://{user}:{password}@{host}/{dbname}?charset=utf8'.format(**{
        'user': os.getenv('DB_USER', 'root'),
        #公開サーバー用↓
        #'user': os.getenv('DB_USER', 'sa'), 
        'password': os.getenv('DB_PASSWORD', 'adminadmin'),
        #公開サーバー用↓
        #'password': os.getenv('DB_PASSWORD', ''),   
        'host': os.getenv('DB_HOST', 'localhost'),
        'dbname': os.getenv('DB_NAME' 'none')
     })

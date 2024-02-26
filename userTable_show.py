#実行するとtemplatesフォルダ内に「usertable.html」を作成、更新できます。

import MySQLdb

# MySQLに接続する
db = MySQLdb.connect(
    user="root",
    passwd="adminadmin",
    host="localhost",
    db="none"
)

# カーソルを取得する
cursor = db.cursor()

cursor.execute("SELECT * FROM users")
row = cursor.fetchone()

f = open('templates/usertable.html', encoding='utf-8', mode='w')  #'w'はwriteの略で書き込み可にしてる。

#書き込み内容
f.write('{% extends "base.html" %} \n') # \n:改行
f.write('{% block content %} \n')
f.write('<h1>登録ユーザー一覧</h1> \n')

while row is not None:
    f.write('<p>')
    f.write(str(row))
    f.write('</p>')
    f.write('\n')
    
    row = cursor.fetchone()  #次のデータ（行）に移動

f.write('{% endblock %}')
    
    
#ファイル閉じる
f.close()

# カーソルを閉じる
cursor.close()

# 接続を閉じる
db.close()
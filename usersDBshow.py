import MySQLdb

"""  htmlファイル出力テスト
f = open('test.html', 'w')
f.write('test')
f.close()

f = open('test.html', 'w')
f.write('test \n')
f.write('test')
f.close()
"""

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

f = open('test.html', mode='w')

while row is not None:
    f.write(str(row))
    
    print(row)
    row = cursor.fetchone()
    
    f.write('\n')

f.close()

# カーソルを閉じる
cursor.close()

# 接続を閉じる
db.close()
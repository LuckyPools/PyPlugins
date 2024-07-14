
import pymysql

conn = pymysql.connect(user='root',
                       password='root',
                       host='localhost',
                       port=3306,
                       database='luck_product')


cursor = conn.cursor()

selectSql = "select * from sys_user"

try:
    cursor.execute(selectSql)
    result = cursor.fetchall()
    for row in result:
        print(row)
except:
    print("db throw error")
    
deleteSql = "delete from sys_user where id = '10010'"

try:
    cursor.execute(deleteSql)
    conn.commit()
except:
    conn.rollback()
    
conn.close()
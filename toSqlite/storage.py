import sqlite3
import os.path
import time

db_file = os.environ['HOME']+'/.TraDict.db'
file_or = os.path.isfile(db_file)

create_sql = '''
CREATE TABLE `words` ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `cn` TEXT, `en` TEXT, `time` TEXT NOT NULL )
'''


# 本地时间
def local_str_time():
    local_time = time.localtime()
    y = local_time.tm_year
    m = local_time.tm_mon
    day = local_time.tm_mday
    h = local_time.tm_hour
    mi = local_time.tm_min
    s = local_time.tm_sec
    str_time = str(y) + "/" + str(m) + "/" + str(day) + " " + str(h) + ":" + str(mi) + ":" + str(s)
    # print(y, m, day, h, mi, s)
    # print(str_time)
    return str_time


# 数据
def data(cn, en):
    t = local_str_time()
    y = (None, cn, en, t)
    # print(type(y))
    return y


# 连接数据库
def connect_db():
    if not file_or:
        # print("数据库未创建")
        con = sqlite3.connect(db_file)
        con.execute(create_sql)
    else:
        # print(create_sql)
        # print("数据库已创建")
        con = sqlite3.connect(db_file)

    return con


# 插入数据
def insert_db(db, datas):
    sql = 'insert into words values (?,?,?,?)'
    db.execute(sql, datas)
    db.commit()


# 查询数据
def select_db(db, id="*"):
    sql = 'select * from words'
    result = db.execute(sql)
    # print(result.fetchall())
    print("|编号|             |中文|                |English|               |time|")
    for i in result:
        print(i[0], "               ", i[1], "               ", i[2], "               ", i[3])


# 删除数据
def delete_db(db, id):
    sql = 'delete from words where id=' + str(id)
    db.execute(sql)
    db.commit()
    print("completed")


# if __name__ == "__main__":
#     s = Tra()
#     con = connect_db()
#
#     while True:
#         if s.state:
#             val = input(">")
#
#             if val == "":
#                 continue
#             elif val == 'q':
#                 print("已退出")
#                 break
#             elif val == "cls":
#                 os.system('clear')
#             elif val == "b":
#                 select_db(con)
#             else:
#                 arr = s.dic(val)
#                 # print(arr)
#                 text = ''
#                 for i in range(len(arr)):
#                     text += arr[i]["tgt"]+';'
#
#                 print(text)
#                 insert_db(con, datas=data(text, val))
#         else:
#             break

    # db = connect_db()
    # d = data("中文", "wingmen")

    # print(d)
    # insert_db(db, d)
    # select_db(db)
    # delete_db(db, "2")


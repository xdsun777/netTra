import os
import storage
import tra

if __name__ == '__main__':
    print("欢迎使用ce")
    print("|cls    |x          |q  |")
    print("|清除屏幕|显示查询记录|退出|")
    con = storage.connect_db()
    t = tra.Tra()

    while True:
        val = input('>')
        val = val.strip()
        if val == '':
            continue
        elif val == 'cls':
            os.system('clear')
        elif val == 'q':
            break
        elif val == 'x':
            storage.select_db(con)
        else:
            li = t.dic(val)
            # print(li)
            text = ''
            for i in li:
                text += i["tgt"]
                # print(i)
            print(text)
            text.strip()
            number = ord(text[0])
            # print(number)
            if number in range(65, 91) or number in range(97, 123):
                # print("val的是英文")
                datas = storage.data(val, text)
            else:
                # print("val的是中文")
                datas = storage.data(text, val)
            storage.insert_db(con, datas)

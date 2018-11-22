import sqlite3
import hashlib
import  random
conn = sqlite3.connect('users.db')
c = conn.cursor()

def hash(h):
    h = hashlib.sha1(str(h).encode())
    h.update(b"$0l")
    h = h.hexdigest()
    return(h)

#89654046734
#123
user = ['Сталлоне', 'Сильвестр', 'Аркадьевич', '1976', '01', '21', '1337', '188888', 'муж', '89654046734', '000-000-000 00|', '89654046734']
user.append(hash(123))
c.execute('INSERT into users(surname, name, middle_name, year_of_birth, month_of_birth, day_of_birth, passport_series, passport_number, sex, phone_number, tin, login, password) values(?,?,?,?,?,?,?,?,?,?,?,?,?)', user)
conn.commit()
c.close()
conn.close()

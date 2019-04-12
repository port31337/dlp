#create table admins (id integer not null primary key AUTOINCREMENT,surname text,name text,middle_name text,login varchar(20),password text);
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


admin1 = ['Федорчук', 'Елена','Дмитриевна','fedorchuk', hash(123)]
admin2 = ['Алоскин', 'Максим', 'Максимович','aloskin', hash(456)]
admin3 = ['Паков', 'Александр', 'Александрович', 'pakov', hash(789)]


c.execute('INSERT into admins(surname, name, middle_name, login, password) values(?,?,?,?,?)', admin1)
c.execute('INSERT into admins(surname, name, middle_name, login, password) values(?,?,?,?,?)', admin2)
c.execute('INSERT into admins(surname, name, middle_name, login, password) values(?,?,?,?,?)', admin3)
conn.commit()
c.close()
conn.close()

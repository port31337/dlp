#create table users (id integer not null primary key AUTOINCREMENT, surname text, name text, middle_name  text, year_of_birth varchar(4), month_of_birth varchar(2), day_of_birth varchar(2), passport_series integer, passport_number integer, sex varchar(3), phone_number varchar(12), tin varchar(14), login varchar(20), password text);

import sqlite3, random
import hashlib

surname_men = ['Абрамович', 'Сафонов',  'Лазарев', 'Моисеев',
 'Власов', 'Ершов', 'Власов', 'Маслов', 'Попов', 'Поляков',
 'Соболев', 'Котов', 'Орехов', 'Кабанов', 'Костин', 'Лапин',
 'Крылов', 'Зайцев', 'Исаев', 'Архипов', 'Суханов', 'Громов',
 'Гурьев', 'Гришин', 'Савин', 'Блинов', 'Хохлов', 'Гуляев', 'Дроздов', 'Мишин']

surname_women = ['Соловьева', 'Волкова', 'Третьякова', 'Сидорова',
 'Орехова', 'Исхакова', 'Жукова', 'Панова', 'Зимина', 'Гусева',
 'Суханова', 'Ильина', 'Андреева', 'Ковалева', 'Белякова',
 'Молчанова', 'Галкина', 'Кулакова', 'Рогова', 'Филатова', 'Фокина',
  'Блохина', 'Пестова', 'Фадеева', 'Денисова', 'Мельникова',
 'Романова', 'Хохлова', 'Сысоева', 'Турова']

name_men = ['Алексей', 'Александр', 'Дмитрий', 'Григорий', 'Евгений', 'Константин', 'Олег',
  'Ростислав', 'Игорь', 'Михаил', 'Борис', 'Всеволод', 'Кирилл', 'Лев', 'Максим', 'Николай',
 'Павел', 'Сергей', 'Тимур', 'Федор', 'Эдуард', 'Юрий', 'Ярослав', 'Илья',
 'Андрей', 'Артем', 'Артур', 'Никита', 'Матвей', 'Лука']

name_women = ['Антонина', 'Анна', 'Ольга', 'Елена', 'Яна', 'Ксения', 'Дарья',
'Юля', 'Вероника', 'Светлана', 'Тамара', 'Марина', 'Лидия', 'Галина', 'Вера',
 'Анастасия', 'Ульяна', 'Инна', 'Эвелина', 'Луиза', 'Кристина', 'Раиса', 'Жанна', 'Ирина', 'Людмила', 'Александра', 'Евгения']

middle_name_men = ['Андреевич', 'Анатольевич', 'Дмитриевич', 'Игоревич', 'Олегович',
 'Кириллович', 'Максимович', 'Маратович', 'Алексеевич', 'Никитович', 'Павлович',
 'Петрович', 'Робертович', 'Рудольфович', 'Семенович', 'Святославович',
  'Степанович', 'Федорович', 'Янович', 'Богданович', 'Борисович', 'Вадимович',
  'Георгиевич', 'Артемович', 'Данилович', 'Романович', 'Филиппович', 'Александрович', 'Платонович']

middle_name_women = ['Андреевна', 'Анатольевна', 'Дмитриевна', 'Игоревна', 'Олеговна',
   'Кирилловна', 'Максимовна', 'Маратовна', 'Алексеевна', 'Никитовна', 'Павловна',
   'Петровна', 'Робертовна', 'Рудольфовна', 'Семеновна', 'Святославовна',
    'Степановна', 'Федоровна', 'Яновна', 'Богдановна', 'Борисовна', 'Вадимовна',
    'Георгиевна', 'Артемовна', 'Даниловна', 'Романовна', 'Филипповна', 'Александровна', 'Платоновна']

#month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль',
# 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

sex = ['муж', 'жен']

# Connecting to the database file
conn = sqlite3.connect('users.db')
c = conn.cursor()


def hash():
    h = hashlib.sha1(str(random.randint(1000, 100000)).encode())
    h.update(b"$0l")
    h = h.hexdigest()
    return(h)

for i in range(1,500):
    if i % 2 == 0:
        user = []
        user.append(random.choice(tuple(surname_men)))
        user.append(random.choice(tuple(name_men)))
        user.append(random.choice(tuple(middle_name_men)))
        user.append(random.randint(1960,2000))
        user.append('{0:02}'.format(random.randint(1, 12)))
        if user[4] == '02':
            user.append('{0:02}'.format(random.randint(1,29)))
        else:
            user.append('{0:02}'.format(random.randint(1,31)))
        user.append('{0:04}'.format(random.randint(1000, 9999)))
        user.append('{0:06}'.format(random.randint(100000, 999999)))
        user.append(sex[0])
        user.append('89' + '{0:09}'.format(random.randint(0, 999999999)))
        user.append('{0:03}'.format(random.randint(0, 999)) + '-' + '{0:03}'.format(random.randint(0, 999)) + '-' + '{0:03}'.format(random.randint(0, 999)) + ' ' + '{0:02}'.format(random.randint(0, 99)))
        #print(user)
        user.append(user[9])
        user.append(hash())
        c.execute('INSERT into users(surname, name, middle_name, year_of_birth, month_of_birth, day_of_birth, passport_series, passport_number, sex, phone_number, tin, login, password) values(?,?,?,?,?,?,?,?,?,?,?,?,?)', user)


    else:
            user = []
            user.append(random.choice(tuple(surname_women)))
            user.append(random.choice(tuple(name_women)))
            user.append(random.choice(tuple(middle_name_women)))
            user.append(random.randint(1960,2000))
            user.append('{0:02}'.format(random.randint(1, 12)))
            if user[4] == '02':
                user.append('{0:02}'.format(random.randint(1,29)))
            else:
                user.append('{0:02}'.format(random.randint(1,31)))
            user.append('{0:04}'.format(random.randint(1000, 9999)))
            user.append('{0:06}'.format(random.randint(100000, 999999)))
            user.append(sex[1])
            user.append('89' + '{0:09}'.format(random.randint(0, 999999999)))
            user.append('{0:03}'.format(random.randint(0, 999)) + '-' + '{0:03}'.format(random.randint(0, 999)) + '-' + '{0:03}'.format(random.randint(0, 999)) + ' ' + '{0:02}'.format(random.randint(0, 99)))
            user.append(user[9])
            user.append(hash())
            c.execute('INSERT into users(surname, name, middle_name, year_of_birth, month_of_birth, day_of_birth, passport_series, passport_number, sex, phone_number, tin, login, password) values(?,?,?,?,?,?,?,?,?,?,?,?,?)', user)


#Подтверждение отправки данных в базу
conn.commit()
#Завершение соединения
c.close()
conn.close()

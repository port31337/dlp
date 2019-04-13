import tkinter as tk
from tkinter import ttk
import sqlite3, hashlib, pickle
from tkinter import *
from tkinter import messagebox

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

        root = tk.Tk()
        app = Main(root)
        app.pack()
        root.title("Mybank")
        root.geometry("850x450+300+200")


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def insert_user(self,surname, name, middle_name, year_of_birth, month_of_birth, day_of_birth, passport_series, passport_number, sex, phone_number, tin, login, password):
        password = hashlib.sha1(str(password).encode())
        password.update(b"$0l")
        password = password.hexdigest()
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute(''' INSERT INTO users(surname, name, middle_name, year_of_birth, month_of_birth, day_of_birth, passport_series, passport_number, sex, phone_number, tin, login, password) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)''', (surname, name, middle_name, year_of_birth, month_of_birth, day_of_birth, passport_series, passport_number, sex, phone_number, tin, login, password))
        conn.commit()

    def init_child(self):
        self.title("Регистрация")
        self.geometry("550x650+300+200")
        self.grab_set() #Перехватывает все события происходящие в приложении
        self.focus_set() #Захватывает и удерживает фокус
        #Подписать поля ввода
        label_two = ttk.Label(self, text = "Фамилия")
        label_two.place( x = 50, y = 50)
        label_tree = ttk.Label(self, text = "Имя")
        label_tree.place( x = 50, y = 80)
        label_four = ttk.Label(self, text = "Отчество")
        label_four.place( x = 50, y = 110)
        label_five = ttk.Label(self, text = "Год рождения")
        label_five.place( x = 50, y = 140)
        label_six = ttk.Label(self, text = "Месяц рождения")
        label_six.place( x = 50, y = 170)
        label_seven = ttk.Label(self, text = "Число рождения")
        label_seven.place( x = 50, y = 200)
        label_eight = ttk.Label(self, text = "Серия паспорта")
        label_eight.place( x = 50, y = 230)
        label_nine = ttk.Label(self, text = "Номер паспорта")
        label_nine.place( x = 50, y = 260)
        label_ten = ttk.Label(self, text = "Пол")
        label_ten.place( x = 50, y = 290)
        label_eleven = ttk.Label(self, text = "Номер Телефона")
        label_eleven.place( x = 50, y = 320)
        label_twelve = ttk.Label(self, text = "ИНН")
        label_twelve.place( x = 50, y = 350)
        label_thirt = ttk.Label(self, text = "Логин")
        label_thirt.place( x = 50, y = 380)
        label_fourt = ttk.Label(self, text = "Пароль")
        label_fourt.place( x = 50, y = 410)

        #Поля для ввода данных в дочернем окне
        self.entry_two = ttk.Entry(self)
        self.entry_two.place(x = 200, y = 50)
        self.entry_tree = ttk.Entry(self)
        self.entry_tree.place(x = 200, y = 80)
        self.entry_four = ttk.Entry(self)
        self.entry_four.place(x = 200, y = 110)
        self.entry_five = ttk.Entry(self)
        self.entry_five.place(x = 200, y = 140)
        self.entry_six = ttk.Entry(self)
        self.entry_six.place(x = 200, y = 170)
        self.entry_seven = ttk.Entry(self)
        self.entry_seven.place(x = 200, y = 200)
        self.entry_eight = ttk.Entry(self)
        self.entry_eight.place(x = 200, y = 230)
        self.entry_nine = ttk.Entry(self)
        self.entry_nine.place(x = 200, y = 260)
        #Выпaдающий список
        self.combobox = ttk.Combobox(self, value = ["Муж", "Жен"])
        #оборажения пункта по умолчанию
        self.combobox.current(0)
        self.combobox.place(x = 200, y = 290)
        self.entry_eleven = ttk.Entry(self)
        self.entry_eleven.place(x = 200, y = 320)
        self.entry_twelve = ttk.Entry(self)
        self.entry_twelve.place(x = 200, y = 350)
        self.entry_thirt = ttk.Entry(self)
        self.entry_thirt.place(x = 200, y = 380)
        self.entry_fourt = ttk.Entry(self)
        self.entry_fourt.place(x = 200, y = 410)

        #Кпонки добавление содержимого и сохранять в бд, вторая закрытие окна
        btn_ok = ttk.Button(self, text = 'Добавить')
        btn_ok.place(x = 190, y = 450)
        btn_ok.bind('<Button-1>', lambda event: self.insert_user(self.entry_two.get(), self.entry_tree.get(),self.entry_four.get(),self.entry_five.get(), self.entry_six.get(), self.entry_seven.get(),self.entry_eight.get(),self.entry_nine.get(),self.combobox.get(),self.entry_eleven.get(),self.entry_twelve.get(),self.entry_thirt.get(),self.entry_fourt.get()))

        btn_cancel = ttk.Button(self, text = "Закрыть", command = self.destroy)
        btn_cancel.place(x = 290, y =450)



class Check_in(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_admin()

    def insert_admin(self,surname, name, middle_name, login, password):
        password = hashlib.sha1(str(password).encode())
        password.update(b"$0l")
        password = password.hexdigest()
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute(''' INSERT INTO admins(surname, name, middle_name, login, password) VALUES(?,?,?,?,?)''', (surname, name, middle_name, login, password))
        conn.commit()

    def init_admin(self):
        self.title("Регистрация администратора")
        self.geometry("550x650+300+200")
        self.grab_set()
        self.focus_set()

        label_surname = ttk.Label(self, text = "Фамилия")
        label_surname.place( x = 50, y = 50)
        label_name = ttk.Label(self, text = "Имя")
        label_name.place( x = 50, y = 80)
        label_middle_name = ttk.Label(self, text = "Отчество")
        label_middle_name.place( x = 50, y = 110)
        label_login = ttk.Label(self, text = "Логин")
        label_login.place( x = 50, y = 140)
        label_password = ttk.Label(self, text = "Пароль")
        label_password.place( x = 50, y = 170)

        self.entry_surname = ttk.Entry(self)
        self.entry_surname.place(x = 200, y = 50)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x = 200, y = 80)
        self.entry_middle_name = ttk.Entry(self)
        self.entry_middle_name.place(x = 200, y = 110)
        self.entry_login = ttk.Entry(self)
        self.entry_login.place(x = 200, y = 140)
        self.entry_password = ttk.Entry(self)
        self.entry_password.place(x = 200, y = 170)

        button_ok = ttk.Button(self, text = 'Добавить')
        button_ok.place(x = 190, y = 200)
        button_ok.bind('<Button-1>', lambda event: self.insert_admin(self.entry_surname.get(), self.entry_name.get(),self.entry_middle_name.get(),self.entry_login.get(), self.entry_password.get()))

        button_cancel = ttk.Button(self, text = "Закрыть", command = self.destroy)
        button_cancel.place(x = 290, y =200)


class Child2(tk.Toplevel):
    def __init__(self, root, currentuser, previouswindow):
        super().__init__()
        self.previouswindow = previouswindow
        self.currentuser = currentuser
        previouswindow.pack_forget()
        previouswindow.destroy()
        self.table()
        self.logout()
        if self.is_admin(currentuser):
            self.search()

    def view_records(self):
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute('''SELECT * from users''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        for row in c:
            self.tree.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))

    def table(self):
        self.title("Просмотр базы клиентов")
        self.geometry("1000x700+0+500")
        self.grab_set() #Перехватывает все события происходящие в приложении
        self.focus_set() #Захватывает и удерживает фокус

        self.tree = ttk.Treeview(self, columns = ('id','surname', 'name', 'middle_name', 'year_of_birth', 'month_of_birth', 'day_of_birth', 'passport_series',
        'passport_number', 'sex', 'phone_number', 'tin'), height = 30, show = "headings")
        #Параметры для колонок
        self.tree.column('id', width = 60) #anchor  = tk.LEFT- положение теста в колонке
        self.tree.column('surname', width = 110)
        self.tree.column('name', width = 110)
        self.tree.column('middle_name', width = 120)
        self.tree.column('year_of_birth', width = 80)
        self.tree.column('month_of_birth', width = 50)
        self.tree.column('day_of_birth', width = 50)
        self.tree.column('passport_series', width = 60)
        self.tree.column('passport_number', width = 100)
        self.tree.column('sex', width = 40)
        self.tree.column('phone_number', width = 120)
        self.tree.column('tin', width = 150)



        self.tree.heading('id', text = 'Договор')
        self.tree.heading('surname', text = 'Фамилия')
        self.tree.heading('name', text = 'Имя')
        self.tree.heading('middle_name', text = 'Отчество')
        self.tree.heading('year_of_birth', text = 'Год рождения')
        self.tree.heading('month_of_birth', text = 'Месяц')
        self.tree.heading('day_of_birth', text = 'День')
        self.tree.heading('passport_series', text = 'Серия')
        self.tree.heading('passport_number', text = 'Номер паспорта')
        self.tree.heading('sex', text = 'Пол')
        self.tree.heading('phone_number', text = 'Номер телефона')
        self.tree.heading('tin', text = 'ИНН')

        self.tree.pack()





        if self.is_admin(self.currentuser):
            conn = sqlite3.connect("users.db")
            c = conn.cursor()
            c.execute('''SELECT * from users''')
            for row in c:
                self.tree.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))
            conn.commit()
            button_chek_in_admin = ttk.Button(self, text = "Просмотр базы", command =lambda: self.view_records())
            button_chek_in_admin.place(x = 300, y = 650)
            button_chek_in_admin = ttk.Button(self, text = "Регистрация администратора", command = Check_in)
            button_chek_in_admin.place(x = 420, y = 650)
        else:
            u = self.currentuser
            self.tree.insert('', 'end', values=(u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7], u[8], u[9], u[10], u[11]))

    def logout(self):
        self.button_logout = ttk.Button(self, text = "Выйти", command = lambda: sys.exit(0))
        self.button_logout.pack()
        self.button_logout.place(x = 640, y = 650)

    # todo: сделать определение администратора через БД
    def is_admin(self, user):
        return user == True

    def search(self):
        self.enter_search = ttk.Entry(self)
        self.enter_search.place(x = 0, y = 650)
        self.button_logout = ttk.Button(self, text = "Поиск", command = lambda: self.do_search(self.enter_search.get()))
        self.button_logout.pack()
        self.button_logout.place(x = 200, y = 650)

    def do_search(self, q):
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute('SELECT * from users where (id = :q) or (surname = :q) or (name || \' \' || surname = :q) or (surname || \' \' || name = :q) or (name || \' \' || middle_name || \' \' || surname = :q) or (surname || \' \' || name || \' \' || middle_name = :q)', {"q": q})
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in c:
            self.tree.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))
        conn.commit()



class Entrance(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.login()


    def log_pass(self, l, p):
        p = hashlib.sha1(str(p).encode())
        p.update(b"$0l")
        p = p.hexdigest()
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute('SELECT * from users WHERE login = ? and password = ?', (l,str(p)))
        user = c.fetchone()
        c.execute('SELECT * from admins WHERE login = ? and password = ?', (l,str(p)))
        admin = c.fetchone()
        if user == None and admin == None:
            messagebox.showerror("Ошибка!", "Веден неверный логин или пароль")
        else:
            if admin:
                user = True
            try:
                nextwindow = Child2(self._root, user, self)
                nextwindow.tkraise()
            except Exception as ex:
                print(ex)


    def login(self):
        text_enter_log = Label(text = "Введите ваш логин")
        enter_login = Entry()
        text_enter_pas = Label( text = "Введите Ваш пароль")
        enter_pas = Entry(show = "*")
        button_enter = Button(text = "Войти", command = lambda: self.log_pass(enter_login.get(), enter_pas.get()))
        button_chek_in = Button(text = "Регистрация", command = Child)
        text_enter_log.pack()
        enter_login.pack()
        text_enter_pas.pack()
        enter_pas.pack()
        button_enter.pack()
        button_chek_in.pack()



root = tk.Tk()
app = Entrance(root)
app.pack()
root.geometry("400x500+100+200")
root.title("Вход в систему")
root.mainloop()

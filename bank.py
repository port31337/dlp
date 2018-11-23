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
    #toolbar
    def init_main(self):
        toolbar = tk.Frame(bg = 'grey', bd = 2)
        toolbar.pack(side = tk.TOP, fill = tk.X)

        btn_open_dia = tk.Button(toolbar, text = "Регистрация", command = self.open_dialog, bg ="grey", bd = 0, compound = tk.TOP)
        btn_open_dia.pack(side = tk.RIGHT)
        btn_open_dia2 = tk.Button(toolbar, text = "Просмотр", command = self.look_base, bg ="grey", bd = 0, compound = tk.TOP)
        btn_open_dia2.pack(side = tk.RIGHT)
        btn_open_dia3 = tk.Button(toolbar, text = "Администратор", command = self.open_dialog, bg ="grey", bd = 0, compound = tk.TOP)
        btn_open_dia3.pack(side = tk.LEFT)

    def open_dialog(self):
        Child()
    def look_base(self):
        Child2()



class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title("Регистрация")
        self.geometry("650x450+300+200")
        self.grab_set() #Перехватывает все события происходящие в приложении
        self.focus_set() #Захватывает и удерживает фокус

        #Подписать поля ввода
        label_two = ttk.Label(self, text = "Наименование two")
        label_two.place( x = 50, y = 50)
        label_tree = ttk.Label(self, text = "Наименование tree")
        label_tree.place( x = 50, y = 80)
        label_four = ttk.Label(self, text = "Наименование four")
        label_four.place( x = 50, y = 110)

        #Поля для ввода данных в дочернем окне
        self.entry_two = ttk.Entry(self)
        self.entry_two.place(x = 200, y = 50)
        self.entry_tree = ttk.Entry(self)
        self.entry_tree.place(x = 200, y = 110)
        self.entry_four = ttk.Entry(self)
        self.entry_four.place(x = 200, y = 150)
        #Выпaдающий список
        self.combobox = ttk.Combobox(self, value = ["Муж", "Жен"])

        #оборажения пункта по умолчанию
        self.combobox.current(0)
        self.combobox.place(x = 200, y = 80)

        #Кпонки добавление содержимого и сохранять в бд, вторая закрытие окна
        btn_ok = ttk.Button(self, text = 'Добавить')
        btn_ok.place( x = 220, y = 170)
        btn_ok.bind('<Button-1>') #срабатывание по левой кнопки мыши
        btn_cancel = ttk.Button(self, text = "Закрыть", command = self.destroy)
        btn_cancel.place(x = 300, y =170)



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
        else:
            u = self.currentuser
            self.tree.insert('', 'end', values=(u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7], u[8], u[9], u[10], u[11]))

    def logout(self):
        self.button_logout = ttk.Button(self, text = "Выйти", command = lambda: sys.exit(0))
        self.button_logout.pack()
        self.button_logout.place(x = 300, y = 650)

    # todo: сделать определение администратора через БД
    def is_admin(self, user):
        return user[0] == 500

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
        print(user)
        if (user == None):
            messagebox.showerror("Ошибка!", "Веден неверный логин или пароль")
        else:
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
        text_enter_log.pack()
        enter_login.pack()
        text_enter_pas.pack()
        enter_pas.pack()
        button_enter.pack()



root = tk.Tk()
app = Entrance(root)
app.pack()
root.geometry("400x500+100+200")
root.title("Вход в систему")
root.mainloop()

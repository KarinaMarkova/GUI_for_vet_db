import psycopg2
import bcrypt
from psycopg2 import Error

# создание переменных, которые пригодятся в процессе:


from tkinter import *
from tkinter import Radiobutton
from tkinter import Checkbutton
from tkinter import messagebox
from tkinter import ttk
from tkinter import font

x = 'parolforivan35'
y = 'Qzawxsvet017'
print(bcrypt.hashpw(x.encode(), bcrypt.gensalt()).decode())
print(bcrypt.hashpw(y.encode(), bcrypt.gensalt()).decode())

# окно для входа(для сотрудника)(ввода логина и пароля)
def clicked_sign_in_employee():  # проверка логина и пароля в бд
    global parol_iz_bd
    global employee_id
    global txt_log
    global login
    global password
    global role
    login = txt_log.get()

    try:
        # Подключение к базе данных
        connection = psycopg2.connect(user="postgres",
                                      password="1234",  # пароль PostgreSQL
                                      host="localhost",
                                      port="5432",
                                      database="Vet_DB")

        print("Database connected successfully")
        cursor = connection.cursor()
        cursor.execute(f"""select employee_id from employee """
                       f"""where employee_login = %(login)s""", {'login': login})
        for row in cursor.fetchall():
            employee_id = row[0]
        cursor.execute(f"""select employee_role_user from employee """
                       f"""where employee_login = %(login)s""", {'login': login})
        for row in cursor.fetchall():
            role = row[0]
        cursor.execute("""select employee_password from employee where 
                          employee_login = %(login)s""", {'login': login})
        for row in cursor.fetchall():
            parol_iz_bd = row[0].encode()

        if bcrypt.checkpw(txt_pas.get().encode(), parol_iz_bd):
            lbl.destroy()
            btn_client.destroy()
            btn_vet.destroy()
            window.geometry('300x280+500+300')
            lbl_1 = Label(window, text="Для продолжения работы\n выберите интересующий раздел", font=("Arial", 14),
                          bg="azure", fg="midnight blue")
            lbl_1.grid(column=0, row=0)
            btn_tasks = Button(window, text="История визитов", font=("Arial", 13), bg="LightBlue1",
                               command=history_visit)
            btn_tasks.grid(column=0, row=1)
            btn_organization = Button(window, text="Информация об организациях", font=("Arial", 13), bg="LightBlue1", command = organization_show)
            btn_organization.grid(column=0, row=2)
            btn_employee = Button(window, text="Информация о сотрудниках", font=("Arial", 13), bg="LightBlue1", command = employee_show)
            btn_employee.grid(column=0, row=3)

            if role == 1:
                btn = Button(window, text="Cоздать отчет по приемам", font=("Arial", 13), bg="LightBlue1",
                             command=visit_otchet)
                btn.grid(column=0,row=5)
            elif role == 2:
                btn = Button(window, text="Cоздать отчет по анализам", font=("Arial", 13), bg="LightBlue1",
                             command=visit_otchet)
                btn.grid(column=0, row=5)
            elif role == 4:
                btn_priv = Button(window, text="Привилегии", font=("Arial", 13), bg="LightBlue1", command = priv)
                btn_priv.grid(column=0, row=5)
            btn_exit = Button(window, text="Выход", font=("Arial", 13), bg="LightBlue1", command=lambda: [window.destroy()])
            btn_exit.grid(column=0, row=6)
        else:
            messagebox.showerror('ОШИБКА', 'Ошибка: Неправильно введен логин или пароль!')
        connection.commit()
        connection.commit()
    except (Exception, Error) as error:
        messagebox.showerror('ОШИБКА', 'Ошибка: Неправильно введен логин или пароль!')
        print("Ошибка при работе с PostgreSQL", error)
def visit_otchet():
    window_1 = Toplevel()

def priv():
    window_1 = Toplevel()
    window_1.title("DB_VET_HISTORY_VISIT")
    window_1.geometry('300x200+500+300')
    window_1.configure(bg="azure")
    btn = Button(window_1, text="Cоздать клиента", font=("Arial", 13), bg="LightBlue1",
                               command=create_client)
    btn.grid(column=0, row=0)
    btn = Button(window_1, text="Cоздать сотрудника", font=("Arial", 13), bg="LightBlue1",
                 command=create_employee)
    btn.grid(column = 0, row = 1)
def create_client():
    window_1 = Toplevel()
    window_1.title("DB_VET_NEW_HISTORY_VISIT")
    window_1.geometry('350x320+500+300')
    window_1.configure(bg="azure")
    global txt_name, txt_surname, txt_patronymic
    global txt_telephone_number
    global txt_login
    global txt_password
    global txt_orgId, txt_role
    lbl = Label(window_1, text="Новый сотрудник:",
                font=("Arial", 14), bg="azure", fg='midnight blue')
    lbl.grid(column=1, row=0)
    txt_name = Entry(window_1, width=30)
    txt_name.grid(column=1, row=1)
    lbl_name = Label(window_1, text="имя:", font=("Arial", 12), bg="azure")
    lbl_name.grid(column=0, row=1)
    txt_surname = Entry(window_1, width=30)
    txt_surname.grid(column=1, row=2)
    lbl_surname = Label(window_1, text="фамилия:", font=("Arial", 12), bg="azure")
    lbl_surname.grid(column=0, row=2)
    txt_patronymic = Entry(window_1, width=30)
    txt_patronymic.grid(column=1, row=3)
    lbl_patronymic = Label(window_1, text="отчество:", font=("Arial", 12), bg="azure")
    lbl_patronymic.grid(column=0, row=3)
    txt_telephone_number = Entry(window_1, width=30)
    txt_telephone_number.grid(column=1, row=4)
    lbl_telephone_number = Label(window_1, text="телефон:", font=("Arial", 12), bg="azure")
    lbl_telephone_number.grid(column=0, row=4)
    txt_login = Entry(window_1, width=30)
    txt_login.grid(column=1, row=5)
    lbl_login = Label(window_1, text="логин:", font=("Arial", 12), bg="azure")
    lbl_login.grid(column=0, row=5)
    txt_orgId = Entry(window_1, width=30)
    txt_orgId.grid(column=1, row=6)
    lbl_orgId = Label(window_1, text="ID орг.:", font=("Arial", 12), bg="azure")
    lbl_orgId.grid(column=0, row=6)
    txt_password = Entry(window_1, width=30)
    txt_password.grid(column=1, row=7)
    lbl_password = Label(window_1, text="пароль:", font=("Arial", 12), bg="azure")
    lbl_password.grid(column=0, row=7)
    txt_role = Entry(window_1, width=30)
    txt_role.grid(column=1, row=8)
    lbl_role = Label(window_1, text="роль:", font=("Arial", 12), bg="azure")
    lbl_role.grid(column=0, row=8)
    btn = Button(window_1, text="Создать нового клиента", font=("Arial", 13), bg="LightBlue1",
                 command=lambda: [create_new_client(), window_1.destroy()])
    btn.grid(column=1, row=9)
    btn = Button(window_1, text="Назад", font=("Arial", 13), bg="LightBlue1",
                 command=lambda: window_1.destroy())
    btn.grid(column=1, row=10)
def create_new_client():
    global new_idclient
    hashpas_employee = bcrypt.hashpw(txt_password.get().encode(), bcrypt.gensalt())
    try:
        # Подключение к базе данных
        connection = psycopg2.connect(user=login,
                                      password=parol_iz_bd.decode(),  # пароль PostgreSQL
                                      host="localhost",
                                      port="5432",
                                      database="Vet_DB")

        print("Database connected successfully")
        cursor = connection.cursor()
        cursor.execute("select max(client_id) from client;")
        for row in cursor.fetchall():
            new_idclient = row[0] + 1
        cursor.execute("""CALL create_client(%s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                       (new_idclient, txt_name.get(), txt_surname.get(), txt_patronymic.get(), txt_telephone_number.get(),
                        txt_login.get(),
                        hashpas_employee.decode(), txt_orgId.get(), txt_role.get()))


        connection.commit()
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

def create_employee():
    window_1 = Toplevel()
    window_1.title("DB_VET_NEW_HISTORY_VISIT")
    window_1.geometry('350x320+500+300')
    window_1.configure(bg="azure")
    global txt_name, txt_surname, txt_patronymic
    global txt_telephone_number
    global txt_login
    global txt_password
    global txt_orgId, txt_role
    lbl = Label(window_1, text="Новый сотрудник:",
                font=("Arial", 14), bg="azure", fg='midnight blue')
    lbl.grid(column=1, row=0)
    txt_name = Entry(window_1, width=30)
    txt_name.grid(column=1, row=1)
    lbl_name = Label(window_1, text="имя:", font=("Arial", 12), bg="azure")
    lbl_name.grid(column=0, row=1)
    txt_surname = Entry(window_1, width=30)
    txt_surname.grid(column=1, row=2)
    lbl_surname = Label(window_1, text="фамилия:", font=("Arial", 12), bg="azure")
    lbl_surname.grid(column=0, row=2)
    txt_patronymic = Entry(window_1, width=30)
    txt_patronymic.grid(column=1, row=3)
    lbl_patronymic = Label(window_1, text="отчество:", font=("Arial", 12), bg="azure")
    lbl_patronymic.grid(column=0, row=3)
    txt_telephone_number = Entry(window_1, width=30)
    txt_telephone_number.grid(column=1, row=4)
    lbl_telephone_number = Label(window_1, text="телефон:", font=("Arial", 12), bg="azure")
    lbl_telephone_number.grid(column=0, row=4)
    txt_login = Entry(window_1, width=30)
    txt_login.grid(column=1, row=5)
    lbl_login = Label(window_1, text="логин:", font=("Arial", 12), bg="azure")
    lbl_login.grid(column=0, row=5)
    txt_orgId = Entry(window_1, width=30)
    txt_orgId.grid(column=1, row=6)
    lbl_orgId = Label(window_1, text="ID орг.:", font=("Arial", 12), bg="azure")
    lbl_orgId.grid(column=0, row=6)
    txt_password = Entry(window_1, width=30)
    txt_password.grid(column=1, row=7)
    lbl_password = Label(window_1, text="пароль:", font=("Arial", 12), bg="azure")
    lbl_password.grid(column=0, row=7)
    txt_role = Entry(window_1, width=30)
    txt_role.grid(column=1, row=8)
    lbl_role = Label(window_1, text="роль:", font=("Arial", 12), bg="azure")
    lbl_role.grid(column=0, row=8)
    btn = Button(window_1, text="Создать нового сотрудника", font=("Arial", 13), bg="LightBlue1",
                 command=lambda: [create_new_employee(), window_1.destroy()])
    btn.grid(column=1, row=9)
    btn = Button(window_1, text="Назад", font=("Arial", 13), bg="LightBlue1",
                 command=lambda: window_1.destroy())
    btn.grid(column=1, row=10)

def create_new_employee():
    global new_idemployee
    hashpas_employee = bcrypt.hashpw(txt_password.get().encode(), bcrypt.gensalt())
    try:
        # Подключение к базе данных
        connection = psycopg2.connect(user=login,
                                      password=parol_iz_bd.decode(),  # пароль PostgreSQL
                                      host="localhost",
                                      port="5432",
                                      database="Vet_DB")

        print("Database connected successfully")
        cursor = connection.cursor()
        cursor.execute("select max(employee_id) from employee;")
        for row in cursor.fetchall():
            new_idemployee = row[0] + 1
        cursor.execute("""CALL create_vet(%s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                       (new_idemployee, txt_name.get(), txt_surname.get(), txt_patronymic.get(), txt_telephone_number.get(),
                        txt_login.get(),
                        hashpas_employee.decode(), txt_orgId.get(), txt_role.get()))


        connection.commit()
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


# окно для входа(для клиента)(проверки данных в бд)
def clicked_sign_in_client():  # проверка логина и пароля в бд
    global parol_iz_bd
    global employee_id
    global txt_log
    global login
    global password
    global role
    global client_id
    login = txt_log.get()

    try:
        # Подключение к базе данных
        connection = psycopg2.connect(user="postgres",
                                      password="1234",  # пароль PostgreSQL
                                      host="localhost",
                                      port="5432",
                                      database="Vet_DB")

        print("Database connected successfully")
        cursor = connection.cursor()
        cursor.execute(f"""select client_id from client """
                       f"""where client_login = %(login)s""", {'login': login})
        for row in cursor.fetchall():
            client_id = row[0]
        cursor.execute(f"""select client_role_user from client """
                       f"""where client_login = %(login)s""", {'login': login})
        for row in cursor.fetchall():
            role = row[0]
        cursor.execute("""select client_password from client where 
                             client_login = %(login)s""", {'login': login})
        for row in cursor.fetchall():
            parol_iz_bd = row[0].encode()

        if bcrypt.checkpw(txt_pas.get().encode(), parol_iz_bd):
            lbl.destroy()
            btn_client.destroy()
            btn_vet.destroy()
            window.geometry('300x220+500+300')
            lbl_1 = Label(window, text="Для продолжения работы\n выберите интересующий раздел", font=("Arial", 14),
                          bg="azure", fg="midnight blue")
            lbl_1.grid(column=0, row=0)
            btn_tasks = Button(window, text="Пройденные процедуры", font=("Arial", 13), bg="LightBlue1",
                               command=procedure_show)
            btn_tasks.grid(column=0, row=1)

            btn = Button(window, text="Добавить питомца", font=("Arial", 13), bg="LightBlue1",
                             command=create_pet)
            btn.grid(column=0, row=5)
            btn_exit = Button(window, text="Выход", font=("Arial", 13), bg="LightBlue1",
                              command=lambda: [window.destroy()])
            btn_exit.grid(column=0, row=6)
        else:
            messagebox.showerror('ОШИБКА', 'Ошибка: Неправильно введен логин или пароль!')
        connection.commit()
        connection.commit()
    except (Exception, Error) as error:
        messagebox.showerror('ОШИБКА', 'Ошибка: Неправильно введен логин или пароль!')
        print("Ошибка при работе с PostgreSQL", error)


def my_pet():
    window_1 = Toplevel()
    window_1.title("DB_VET_HISTORY_VISIT")
    window_1.geometry('300x200+500+300')
    window_1.configure(bg="azure")

    btn = Button(window_1, text="Добавить питомца", font=("Arial", 13), bg="LightBlue1",
                 command=create_pet)
    btn.grid(column=0, row=1)
def pet_show():
    try:
        # Подключение к базе данных
        connection = psycopg2.connect(user=login,
                                      password=parol_iz_bd.decode(),  # пароль PostgreSQL
                                      host="localhost",
                                      port="5432",
                                      database="Vet_DB")

        print("Database connected successfully")
        window_1 = Toplevel()
        cursor = connection.cursor()
        cursor.execute("""SELECT pet_name, pet_surname, pet_gender, pet_birthday FROM pet INNER
         JOIN client ON pet.pet_client_id = %s;""", (client_id) )

        result = cursor.fetchall()
        heads = ['имя','фамилия','пол', 'дата рождения']
        table = ttk.Treeview(window_1, show='headings')
        table['columns'] = heads
        for header in heads:
            table.heading(header,text=header,anchor='center')
            table.column(header,anchor='center')

        for hist in result:
            print(hist)
            table.insert('', END, values=hist)
            table.pack()

        connection.commit()
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
def create_pet():
    window_1 = Toplevel()
    window_1.title("DB_VET_NEW_HISTORY_VISIT")
    window_1.geometry('350x320+500+300')
    window_1.configure(bg="azure")
    global txt_name, txt_surname
    global txt_gender, txt_type
    global txt_birthday

    lbl = Label(window_1, text="Новый питомец:",
                font=("Arial", 14), bg="azure", fg='midnight blue')
    lbl.grid(column=1, row=0)
    txt_name = Entry(window_1, width=30)
    txt_name.grid(column=1, row=1)
    lbl_name = Label(window_1, text="имя:", font=("Arial", 12), bg="azure")
    lbl_name.grid(column=0, row=1)
    txt_surname = Entry(window_1, width=30)
    txt_surname.grid(column=1, row=2)
    lbl_surname = Label(window_1, text="фамилия:", font=("Arial", 12), bg="azure")
    lbl_surname.grid(column=0, row=2)
    txt_gender = Entry(window_1, width=30)
    txt_gender.grid(column=1, row=3)
    lbl_gender = Label(window_1, text="пол:", font=("Arial", 12), bg="azure")
    lbl_gender.grid(column=0, row=3)
    txt_birthday = Entry(window_1, width=30)
    txt_birthday.grid(column=1, row=4)
    lbl_birthday = Label(window_1, text="дата рождения:", font=("Arial", 12), bg="azure")
    lbl_birthday.grid(column=0, row=4)
    txt_type = Entry(window_1, width=30)
    txt_type.grid(column=1, row=5)
    lbl_type = Label(window_1, text="тип:", font=("Arial", 12), bg="azure")
    lbl_type.grid(column=0, row=5)

    btn = Button(window_1, text="Создать нового питомца", font=("Arial", 13), bg="LightBlue1",
                 command=lambda: [create_new_pet(), window_1.destroy()])
    btn.grid(column=1, row=9)
    btn = Button(window_1, text="Назад", font=("Arial", 13), bg="LightBlue1",
                 command=lambda: window_1.destroy())
    btn.grid(column=1, row=10)
def create_new_pet():
    global idpet
    try:
        # Подключение к базе данных
        connection = psycopg2.connect(user=login,
                                      password=parol_iz_bd.decode(),  # пароль PostgreSQL
                                      host="localhost",
                                      port="5432",
                                      database="Vet_DB")

        print("Database connected successfully")
        window_1 = Toplevel()
        cursor = connection.cursor()
        cursor.execute("select max(service_id) from service;")
        for row in cursor.fetchall():
            idpet = row[0] + 1
        cursor.execute("""CALL create_service(%s, %s, %s, %s, %s, %s, %s)""",
                       (idpet, {txt_name.get()}, {txt_surname.get()}, {txt_gender.get()},
                        {txt_birthday.get()}, client_id,txt_type.get() ))
        result = cursor.fetchall()
        table = ttk.Treeview(window_1)
        table['columns'] = ['id_tasks', 'name_tasks', 2, 3, 4]

        for hist in result:
            print(hist)
            table.insert('', END, values=hist)
            table.pack()

        connection.commit()
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
def procedure_show():
    try:
        # Подключение к базе данных
        connection = psycopg2.connect(user=login,
                                      password=parol_iz_bd.decode(),  # пароль PostgreSQL
                                      host="localhost",
                                      port="5432",
                                      database="Vet_DB")

        print("Database connected successfully")
        window_1 = Toplevel()
        cursor = connection.cursor()
        cursor.execute("""SELECT service_name, service_price, service_status FROM service,visit_history, client, pet where service_visit_history_id
         = visit_history_id and visit_history_pet_id = pet_id and pet_client_id=client_id;""")
        result = cursor.fetchall()
        heads = ['иназвание','цена','статус']
        table = ttk.Treeview(window_1, show='headings')
        table['columns'] = heads
        for header in heads:
            table.heading(header,text=header,anchor='center')
            table.column(header,anchor='center')

        for hist in result:
            print(hist)
            table.insert('', END, values=hist)
            table.pack()

        connection.commit()
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

def employee_show():
    try:
        # Подключение к базе данных
        connection = psycopg2.connect(user=login,
                                      password=parol_iz_bd.decode(),  # пароль PostgreSQL
                                      host="localhost",
                                      port="5432",
                                      database="Vet_DB")

        print("Database connected successfully")
        window_1 = Toplevel()
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM employee_info;""")
        result = cursor.fetchall()
        heads = ['имя ','фамилия','отчество','телефон', 'ID организации']
        table = ttk.Treeview(window_1, show='headings')
        table['columns'] = heads
        for header in heads:
            table.heading(header,text=header,anchor='center')
            table.column(header,anchor='center')

        for hist in result:
            print(hist)
            table.insert('', END, values=hist)
            table.pack()

        connection.commit()
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
def organization_show():

    try:
        # Подключение к базе данных
        connection = psycopg2.connect(user=login,
                                      password=parol_iz_bd.decode(),  # пароль PostgreSQL
                                      host="localhost",
                                      port="5432",
                                      database="Vet_DB")

        print("Database connected successfully")
        window_1 = Toplevel()
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM organisation_info;""")
        result = cursor.fetchall()
        heads = ['имя организации','телефон','эл.почта','адрес']
        table = ttk.Treeview(window_1, show='headings')
        table['columns'] = heads
        for header in heads:
            table.heading(header,text=header,anchor='center')
            table.column(header,anchor='center')

        for hist in result:
            print(hist)
            table.insert('', END, values=hist)
            table.pack()

        connection.commit()
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


def history_visit():
    global login
    window_1 = Toplevel()
    window_1.title("DB_VET_HISTORY_VISIT")
    window_1.geometry('300x200+500+300')
    window_1.configure(bg="azure")
    lbl_1 = Label(window_1, text="Для продолжения работы\n выберите интересующий раздел", font=("Arial", 14),
                  bg="azure",
                  fg="midnight blue")
    lbl_1.grid(column=0, row=0)
    btn = Button(window_1, text="Просмотр истории визитов", font=("Arial", 13), bg="LightBlue1",
                 command=lambda: [history_visit_show(), window_1.destroy()])
    btn.grid(column=0, row=1)
    btn = Button(window_1, text="Создать новый визит", font=("Arial", 13), bg="LightBlue1",
                 command=lambda: [create_new_history_visit(), window_1.destroy()])
    btn.grid(column=0, row=2)
    btn = Button(window_1, text="Назад", font=("Arial", 13), bg="LightBlue1",
                 command=lambda: window_1.destroy())
    btn.grid(column=0, row=3)


def history_visit_show():
    try:
        # Подключение к базе данных
        connection = psycopg2.connect(user=login,
                                      password=parol_iz_bd.decode(),  # пароль PostgreSQL
                                      host="localhost",
                                      port="5432",
                                      database="Vet_DB")

        print("Database connected successfully")
        window_1 = Toplevel()
        cursor = connection.cursor()
        cursor.execute("""select visit_history_name, visit_history_date, visit_history_simptoms, 
        visit_history_diagnosis, visit_history_pet_id from visit_history INNER JOIN employee ON employee.employee_login 
        =%(login)s and employee.employee_id = visit_history.visit_history_id;""", ({'login': login}))
        result = cursor.fetchall()
        heads = ['цель визита', 'дата', 'симптомы', 'диагноз','ID питомца']
        table = ttk.Treeview(window_1, show='headings')
        table['columns'] = heads
        for header in heads:
            table.heading(header, text=header, anchor='center')
            table.column(header, anchor='center')

        for hist in result:
            print(hist)
            table.insert('', END, values=hist)
            table.pack()

        connection.commit()
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


def create_new_history_visit():
    window_1 = Toplevel()
    window_1.title("DB_VET_NEW_HISTORY_VISIT")
    window_1.geometry('320x220+500+300')
    window_1.configure(bg="azure")
    global txt_name
    global txt_date
    global txt_simptoms
    global txt_diagnosis
    global txt_pet_id
    lbl = Label(window_1, text="Новый визит:",
                font=("Arial", 14), bg="azure", fg='midnight blue')
    lbl.grid(column=1, row=0)
    txt_name = Entry(window_1, width=30)
    txt_name.grid(column=1, row=1)
    lbl_name = Label(window_1, text="цель:", font=("Arial", 12), bg="azure")
    lbl_name.grid(column=0, row=1)
    txt_date = Entry(window_1, width=30)
    txt_date.grid(column=1, row=2)
    lbl_date = Label(window_1, text="дата:", font=("Arial", 12), bg="azure")
    lbl_date.grid(column=0, row=2)
    txt_simptoms = Entry(window_1, width=30)
    txt_simptoms.grid(column=1, row=3)
    lbl_simptoms = Label(window_1, text="симптомы:", font=("Arial", 12), bg="azure")
    lbl_simptoms.grid(column=0, row=3)
    txt_diagnosis = Entry(window_1, width=30)
    txt_diagnosis.grid(column=1, row=4)
    lbl_diagnosis = Label(window_1, text="диагноз:", font=("Arial", 12), bg="azure")
    lbl_diagnosis.grid(column=0, row=4)
    txt_pet_id = Entry(window_1, width=30)
    txt_pet_id.grid(column=1, row=5)
    lbl_pet_id = Label(window_1, text="ID питомца:", font=("Arial", 12), bg="azure")
    lbl_pet_id.grid(column=0, row=5)
    btn = Button(window_1, text="Создать новый визит", font=("Arial", 13), bg="LightBlue1",
                 command=lambda: [create_new_history_visit_in_db(), create_new_procedure(), window_1.destroy()])
    btn.grid(column=1, row=6)
    btn = Button(window_1, text="Назад", font=("Arial", 13), bg="LightBlue1",
                 command=lambda: window_1.destroy())
    btn.grid(column=1, row=7)

def create_new_procedure():
    global txt_price
    global txt_status
    window_1 = Toplevel()
    window_1.title("DB_VET_NEW_HISTORY_VISIT")
    window_1.geometry('320x220+500+300')
    window_1.configure(bg="azure")
    lbl=Label(window_1, text = txt_name.get(), font=("Arial", 14), bg="azure", fg='midnight blue')
    lbl.grid(column=1, row=0)
    txt_price = Entry(window_1, width=30)
    txt_price.grid(column=1, row=1)
    lbl_price = Label(window_1, text="цена:", font=("Arial", 12), bg="azure")
    lbl_price.grid(column=0, row=1)
    txt_status = Entry(window_1, width=30)
    txt_status.grid(column=1, row=2)
    lbl_status = Label(window_1, text="статус:", font=("Arial", 12), bg="azure")
    lbl_status.grid(column=0, row=2)
def create_new_procedure_in_db():
    global idprocedure
    try:
        # Подключение к базе данных
        connection = psycopg2.connect(user=login,
                                      password=parol_iz_bd.decode(),  # пароль PostgreSQL
                                      host="localhost",
                                      port="5432",
                                      database="Vet_DB")

        print("Database connected successfully")
        window_1 = Toplevel()
        cursor = connection.cursor()
        cursor.execute("select max(service_id) from service;")
        for row in cursor.fetchall():
            idprocedure = row[0] + 1
        cursor.execute("""CALL create_service(%s, %s, %s, %s, %s, %s, %s)""",
                       (idprocedure, {txt_name.get()}, txt_price.get(),
                        {txt_status.get()},idvisit))
        result = cursor.fetchall()
        table = ttk.Treeview(window_1)
        table['columns'] = ['id_tasks', 'name_tasks', 2, 3, 4]

        for hist in result:
            print(hist)
            table.insert('', END, values=hist)
            table.pack()

        connection.commit()
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
def create_new_history_visit_in_db():
    global idvisit
    try:
        # Подключение к базе данных
        connection = psycopg2.connect(user=login,
                                      password=parol_iz_bd.decode(),  # пароль PostgreSQL
                                      host="localhost",
                                      port="5432",
                                      database="Vet_DB")

        print("Database connected successfully")
        window_1 = Toplevel()
        cursor = connection.cursor()
        cursor.execute("select max(visit_history_id) from visit_history;")
        for row in cursor.fetchall():
            idvisit = row[0] + 1
        cursor.execute("""CALL create_history_visit(%s, %s, %s, %s, %s, %s, %s)""",
                       ({idvisit}, {txt_name.get()}, {txt_date.get()},
                        {txt_simptoms.get()}, {txt_diagnosis.get()},
                        {txt_pet_id.get()}, employee_id))
        result = cursor.fetchall()
        table = ttk.Treeview(window_1)
        table['columns'] = ['id_tasks', 'name_tasks', 2, 3, 4]

        for hist in result:
            print(hist)
            table.insert('', END, values=hist)
            table.pack()

        connection.commit()
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


def show_pas():
    global var1
    global txt_pas
    global cb
    if var1.get() == 1:
        txt_pas.configure(show="*")
        cb.configure(text='Скрыть пароль')
    else:
        txt_pas.configure(show="")


def client():
    global var1
    global txt_pas
    global txt_log
    global cb
    window_1 = Toplevel()
    window_1.title("DB_VET_CLIENT")
    window_1.geometry('290x220+500+300')
    window_1.configure(bg="azure")
    lbl = Label(window_1, text="Авторизация:",
                font=("Arial", 14), bg="azure", fg='midnight blue')
    lbl.grid(column=1, row=0)
    txt_log = Entry(window_1, width=30)
    txt_log.grid(column=1, row=1)
    lbl_log = Label(window_1, text="логин:", font=("Arial", 12), bg="azure")
    lbl_log.grid(column=0, row=1)
    txt_pas = Entry(window_1, width=30)
    txt_pas.grid(column=1, row=2)
    lbl_pas = Label(window_1, text="пароль:", font=("Arial", 12), bg="azure")
    lbl_pas.grid(column=0, row=2)
    var1 = IntVar()
    cb = Checkbutton(window_1, text="Скрыть пароль", font=("Times New Roman", 10), bg="azure", fg="midnight blue",
                     variable=var1,
                     onvalue=1, offvalue=0,
                     command=show_pas)
    cb.grid(column=1, row=3)
    # кнопка отправки данных в бд
    btn = Button(window_1, text="Выполнить вход", font=("Impact", 15), bg="LightBlue1",
                 command=lambda: [clicked_sign_in_client(), window_1.destroy()])
    btn.grid(column=1, row=4)
    btn = Button(window_1, text="Назад", font=("Impact", 15), bg="LightBlue1", command=lambda: window_1.destroy())
    btn.grid(column=1, row=5)


def employee():
    global var1
    global txt_pas
    global txt_log
    global cb
    window_1 = Toplevel()
    window_1.title("DB_VET_EMPLOYEE")
    window_1.geometry('290x220+500+300')
    window_1.configure(bg="azure")
    lbl = Label(window_1, text="Авторизация:",
                font=("Arial", 14), bg="azure", fg='midnight blue')
    lbl.grid(column=1, row=0)
    txt_log = Entry(window_1, width=30)
    txt_log.grid(column=1, row=1)
    lbl_log = Label(window_1, text="логин:", font=("Arial", 12), bg="azure")
    lbl_log.grid(column=0, row=1)
    txt_pas = Entry(window_1, width=30)
    txt_pas.grid(column=1, row=2)
    lbl_pas = Label(window_1, text="пароль:", font=("Arial", 12), bg="azure")
    lbl_pas.grid(column=0, row=2)
    var1 = IntVar()
    cb = Checkbutton(window_1, text="Скрыть пароль", font=("Times New Roman", 10), bg="azure", fg="midnight blue",
                     variable=var1,
                     onvalue=1, offvalue=0,
                     command=show_pas)
    cb.grid(column=1, row=3)
    # кнопка отправки данных в бд
    btn = Button(window_1, text="Выполнить вход", font=("Impact", 15), bg="LightBlue1",
                 command=lambda: [clicked_sign_in_employee(), window_1.destroy()])
    btn.grid(column=1, row=4)
    btn = Button(window_1, text="Назад", font=("Impact", 15), bg="LightBlue1", command=lambda: window_1.destroy())
    btn.grid(column=1, row=5)


window = Tk()
window.title("DB_VET_WINDOW")
window.geometry('340x185+500+300')
window.configure(bg="azure")
lbl = Label(window, text="Добро пожаловать! \nДля начала работы авторизируйтесь:",
            font=("Arial", 14), bg="azure", fg='midnight blue')
lbl.grid(column=1, row=0)
# открытие окна от имени клиента
btn_client = Button(window, text="Клиент", font=("Impact", 15), bg="LightBlue1", command=client)
btn_client.grid(column=1, row=1)
# открытие окна от имени врача
btn_vet = Button(window, text="Сотрудник", font=("Impact", 15), bg="LightBlue1", command=employee)
btn_vet.grid(column=1, row=2)

window.mainloop()

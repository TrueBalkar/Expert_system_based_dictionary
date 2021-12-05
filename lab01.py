from tkinter import *
import sqlite3


conn = sqlite3.connect("Dict.db")
stm = conn.cursor()
xex = ''
imya = ''


def to_eng(imya, xex, vikno_3, root_1):
    stm.execute(f"""INSERT INTO translate VALUES('{xex}', '{imya}')""")
    conn.commit()
    vikno_3.destroy()
    root_1.destroy()


def to_ukr(imya, xex, vikno_3, root_1):
    stm.execute(f"""INSERT INTO translate VALUES('{imya}', '{xex}')""")
    conn.commit()
    vikno_3.destroy()
    root_1.destroy()


def enter(imya, xex, textBox_1, root_1):
    xex = textBox_1.get().lower()
    vikno_3 = Tk(imya, xex)
    vikno_3.title("Підтвердження")
    vikno_3.geometry("400x100")
    butt_1 = Button(vikno_3, text="Це переклад англійського слова",
                    command=lambda: to_ukr(imya, xex, vikno_3, root_1))
    butt_1.pack(side=TOP, padx=5, pady=5)
    butt_2 = Button(vikno_3, text="Це переклад українського слова",
                    command=lambda: to_eng(imya, xex, vikno_3, root_1))
    butt_2.pack(side=TOP, padx=5, pady=5)
    vikno_3.mainloop()


def func_1(imya):
    root_1 = Tk()
    root_1.title("Словник")
    root_1.geometry("400x100")
    label_1 = Label(root_1, text=f"Введіть переклад слова '{imya}'")
    label_1.pack()
    textBox_1 = Entry(root_1)
    textBox_1.pack(padx=5, pady=5)
    xex = textBox_1.get()
    knopka_1 = Button(root_1, text="Ввести дані",
                      command=lambda: enter(imya, xex, textBox_1, root_1))
    knopka_1.pack(side=TOP, padx=5, pady=5)
    root_1.mainloop()


def reply():
    imya = textBox.get().lower()
    stm.execute(f"""SELECT ukranian FROM translate WHERE english = '{imya}'""")
    mts = stm.fetchone()
    if mts == None:
        stm.execute(
            f"""SELECT english FROM translate WHERE ukranian = '{imya}'""")
        mts = stm.fetchone()
        if mts == None:
            func_1(imya)
    lol.configure(text=mts)


root = Tk()
root.title("Українсько-Англійський словник")
root.geometry("400x125")
label = Label(root, text="Введіть слово для перекладу")
label.pack()
lol = Label(root, text="Тут буде переклад останнього слова, що я знаю")
lol.pack()
textBox = Entry(root)
textBox.pack(padx=5, pady=5)
imya = textBox.get()
knopka = Button(root, text="Перевірити переклад", command=reply)
knopka.pack(side=TOP, padx=5, pady=5)
root.mainloop()

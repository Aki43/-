import sqlite3
spisok = ['apple', 43, 'caw', 'cars', 81, 16,10]
conn = sqlite3.connect('lp_5.bd')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS chisla(id INTEGER PRIMARY KEY AUTOINCREMENT, colon_1 INTEGER)''')
cursor.execute('''DELETE FROM chisla''')
cursor.execute('''CREATE TABLE IF NOT EXISTS bykva(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT)''')
cursor.execute('''DELETE FROM bykva''')
for i in spisok:
    if type(i) is str:
        len(i)
        cursor.execute('''INSERT into bykva(col_1) VALUES(?)''',(i,))
        conn.commit()
        cursor.execute('''INSERT into chisla(colon_1) VALUES(?)''', (len(i),))
        conn.commit()
    elif type(i) is int:
        if i%2==0:
            cursor.execute('''INSERT into chisla(colon_1) VALUES(?)''',(i,))
            conn.commit()
        elif i%2!=0:
            i = 'нечетное'
            cursor.execute('''INSERT into bykva(col_1) VALUES(?)''',(i,))
            conn.commit()
cursor.execute('''SELECT*FROM chisla''')
k = cursor.fetchall()
cursor.execute('''SELECT*FROM bykva''')
p_1 = cursor.fetchall()
if len(p_1) > 5:
    cursor.execute('''DELETE FROM chisla WHERE id = 1''')
    conn.commit()
else:
    cursor.execute('''UPDATE chisla SET colon_1='hello' WHERE id = 1''')
    conn.commit()
print(k)
print(p_1)


# Если число записей во второй таблице больше 5, то удалить 1 запись в первой таблице.
# Если меньше, то обновить 1 запись в первой таблице на «hello»
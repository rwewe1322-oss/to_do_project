import sqlite3
conn = sqlite3.connect('todo.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        completed INTEGER
    )
''')
def add_task(title):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    if not title.strip():
        return False
    else:
        cursor.execute('INSERT INTO tasks (title, completed) VALUES(?,?)',(title,0))
        conn.commit()
        conn.close()
        return True
def get_all_tasks():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    some = cursor.fetchall()
    conn.close()
    return some
conn.commit()


def complete_tasks(task_id):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE id = ?',(task_id,))
    first = cursor.fetchone()
    if first == None:
        return False
    else:
        cursor.execute('UPDATE tasks SET completed = 1 WHERE id = ?',(task_id,))
        conn.commit()
        conn.close()
        return True
print(get_all_tasks())


if __name__ == '__main__':
    add_task('купить хлеб')
    add_task('выучить питон')
    print(get_all_tasks())
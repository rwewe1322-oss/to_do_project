from flask import Flask
from database import get_all_tasks,add_task,complete_tasks

app = Flask(__name__)

@app.route('/')
def main():
    result = '<li>Список задач</li><br>'
    tasks = get_all_tasks()
    for i in tasks:
        result += f'<li>{i[1]}</li><br>'
    return result
@app.route('/add/<title>')
def add(title):
    add_task(title)
    return 'Задача добавлена'
@app.route('/done/<int:task_id>')
def done(task_id):
    complete_tasks(task_id)
    return f'задача {task_id} выполнена'


if __name__ == '__main__':
    app.run(debug=True)
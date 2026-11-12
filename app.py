from flask import Flask,render_template,request,redirect
from database import get_all_tasks,add_task,complete_tasks

app = Flask(__name__)

@app.route('/')
def main():
    result = '<h1>Список задач</h1>'
    tasks = get_all_tasks()
    for i in tasks:
        result += f'<li>{i[1]}</li><br>'
    return result

@app.route('/add/', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form.get('title')
        if title:
            add_task(title)
            return redirect('/')
    return render_template('add_task.html')
@app.route('/done/',methods=['GET', 'POST'])
def done():
    if request.method == 'POST':
        task_id = request.form.get('task_id')
        complete_tasks(int(task_id))
        return redirect('/')
    else:
        return render_template('done_task.html')
if __name__ == '__main__':
    app.run(debug=True)
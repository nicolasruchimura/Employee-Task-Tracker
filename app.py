from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('database.db')
conn.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT, priority TEXT DEFAULT 'Medium', is_done BOOLEAN DEFAULT 0)''')
conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    priority = request.form.get('priority', 'Medium')
    conn = sqlite3.connect('database.db')
    conn.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('database.db')
    conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    conn = sqlite3.connect('database.db')
    print("Current Tasks:", conn.execute('SELECT * FROM tasks').fetchall())
    conn.close()
    app.run(debug=True)
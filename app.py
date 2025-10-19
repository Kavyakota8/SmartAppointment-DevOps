from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB = 'appointments.db'

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            datetime TEXT NOT NULL,
            notes TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('SELECT id, name, email, datetime, notes FROM appointments ORDER BY datetime')
    appointments = c.fetchall()
    conn.close()
    return render_template('index.html', appointments=appointments)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        dt = request.form['datetime']
        notes = request.form.get('notes', '')
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute('INSERT INTO appointments (name, email, datetime, notes) VALUES (?,?,?,?)',
                  (name, email, dt, notes))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/delete/<int:aid>', methods=['POST'])
def delete(aid):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('DELETE FROM appointments WHERE id=?', (aid,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)


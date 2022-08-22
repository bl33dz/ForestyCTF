import json
import sqlite3
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    conn = sqlite3.connect('songs.db')
    cur = conn.cursor()
    data = None
    if request.method == "POST":
        q = filter_words(request.form.get('song'))
        query = "SELECT * FROM songs WHERE title LIKE '%" + q + "%' ORDER BY rank ASC LIMIT 5;"
        try:
            cur.execute(query)
            data = cur.fetchall()
        except:
            data = []
    return render_template('index.html', data=data)

def filter_words(query):
    blacklist = ['--', 'LIKE', 'like', 'ORDER', 'order', 'UNION', 'union', 'SELECT', 'select']
    for word in blacklist:
        query = query.replace(word, "")
    return query

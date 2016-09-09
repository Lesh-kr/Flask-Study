import pymysql

conn = pymysql.connect(host='localhost', user='root', password='12345', db='flasks', charset='utf8')

curs = conn.cursor(pymysql.cursors.DictCursor)

sql = "select * from memo"
curs.execute(sql)

rows = curs.fetchall()

for row in rows:
    print(row['id'])
    print(row['title'])
    print(row['content'])
    print(row['author'])

# configuration
# HOST = 'localhost'
# DEBUG = True
# USERNAME = 'root'
# PASSWORD = '12345'
# DATABASE = 'flasks'
# CHARSET = 'utf-8'

# -----------------------------------------
def connect_db():
    conn = pymysql.connect(host=HOST, user=USERNAME, password=PASSWORD, db=DATABASE, charset=CHARSET)
    return conn

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()
# -----------------------------------------
@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()
# -----------------------------------------

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/lolchampions', methods=['GET'])
def champs():
    return render_template('lolchampions.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

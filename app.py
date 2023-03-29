
# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.String(500), nullable=True)


# @app.route('/tasks', methods=['GET'])
# def get_all_tasks():
#     tasks = Task.query.all()
#     results = []
#     for task in tasks:
#         task_data = {}
#         task_data['id'] = task.id
#         task_data['title'] = task.title
#         task_data['description'] = task.description
#         results.append(task_data)
#     return jsonify(results)


# @app.route('/tasks/<int:task_id>', methods=['GET'])
# def get_task(task_id):
#     task = Task.query.get_or_404(task_id)
#     task_data = {}
#     task_data['id'] = task.id
#     task_data['title'] = task.title
#     task_data['description'] = task.description
#     return jsonify(task_data)


# @app.route('/tasks', methods=['POST'])
# def create_task():
#     title = request.json.get('title')
#     description = request.json.get('description', '')
#     task = Task(title=title, description=description)
#     db.session.add(task)
#     db.session.commit()
#     task_data = {}
#     task_data['id'] = task.id
#     task_data['title'] = task.title
#     task_data['description'] = task.description
#     return jsonify(task_data)


# @app.route('/tasks/<int:task_id>', methods=['PUT'])
# def update_task(task_id):
#     task = Task.query.get_or_404(task_id)
#     title = request.json.get('title')
#     description = request.json.get('description', '')
#     task.title = title
#     task.description = description
#     db.session.commit()
#     task_data = {}
#     task_data['id'] = task.id
#     task_data['title'] = task.title
#     task_data['description'] = task.description
#     return jsonify(task_data)


# @app.route('/tasks/<int:task_id>', methods=['DELETE'])
# def delete_task(task_id):
#     task = Task.query.get_or_404(task_id)
#     db.session.delete(task)
#     db.session.commit()
#     return '', 204


# @app.errorhandler(404)
# def resource_not_found(e):
#     return jsonify(error=str(e)), 404


# @app.errorhandler(500)
# def internal_server_error(e):
#     return jsonify(error=str(e)), 500


# if __name__ == '__main__':
#     db.create_all()
#     app.run(debug=True)


# from flask import Flask, request, jsonify
# import sqlite3
# app = Flask(__name__)

# def db_connection():
#     conn = None
#     try:
#         conn = sqlite3.connect("books.sqlite")
#     except sqlite3.error as e:
#         print(e)
#     return conn


# @app.route('/books', methods=['GET', 'POST'])
# def books():
#     conn = db_connection()
#     cursor = conn.cursor()

#     if request.method == 'GET':
#         cursor = conn.execute("SELECT * FROM book")
#     books = [dict(id = row[0], aurthor = row[1], language = row[2], title = row[3]) for row in cursor.fetchall()]
#     if books is not None:
#         return jsonify(books)

#     if request.method == 'POST':
#         new_author = request.form['author']
#         new_lang = request.form['language']
#         new_title = request.form['title']
#         sql = """INSERT INTO book (author, language, title) VALUES (?, ?, ?)"""

#         cursor = cursor.execute(sql, (new_author, new_lang, new_title))
#         conn.commit()
#         return f"Book with the id: {cursor.lastrowid} created successfully", 201


# @app.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
# def single_book(id):
#     if request.method == 'GET':
#         for book in books_list:
#             if book['id'] == id:
#                 return jsonify(book)
#             pass
#     if request.method == 'PUT':
#         for book in books_list:
#             if book['id'] == id:
#                 book['author'] = request.form['author']
#                 book['language'] = request. form['language']
#                 book['title'] = request.form['title']
#                 updated_book = {
#                     'id': id,
#                     'author': book['author'],
#                     'language': book['language'],
#                     'title': book['title']
#                 }
#                 return jsonify(updated_book)
#     if request.method == 'DELETE':
#         for index, book in enumerate(books_list):
#             if book['id'] == id:
#                 books_list.pop(index)
#                 return jsonify(books_list)

# without db run time -----------------------------------------------------------------------------------------------
# from flask import Flask, request, jsonify
# app = Flask(__name__)

# music_list = [
#     {
#         "id": 0,
#         "artist": "Isac Gracie",
#         "language": "English",
#         "title": "Solhouttes of you"
#     }
# ]


# @app.route('/musics', methods=['GET', 'POST'])
# def musics():
#     if request.method == 'GET':
#         if len(music_list) > 0:
#             return jsonify(music_list)
#         else:
#             'Nothing Found', 404
#     if request.method == 'POST':
#         new_artist = request.form['artist']
#         new_language = request.form['language']
#         new_title = request.form['title']
#         iD = music_list[-1]['id']+1
#         new_music = {
#             "id": iD,
#             "artist": new_artist,
#             "language": new_language,
#             "title": new_title
#         }
#         music_list.append(new_music)
#         return jsonify(music_list), 201


# @app.route('/music/<int:id>', methods=['GET', 'PUT', 'DELETE'])
# def single_music(id):
#     if request.method == 'GET':
#         for music in music_list:
#             if music['id'] == id:
#                 return jsonify(music)
#             pass

#     if request.method == 'PUT':
#         for music in music_list:
#             if music['id'] == id:
#                 music['artist'] = request.form['artist']
#                 music['language'] = request.form['language']
#                 music['title'] = request.form['title']
#                 updated_music = {
#                     'id': id,
#                     'artist': music['artist'],
#                     'language': music['language'],
#                     'title': music['title']
#                 }
#                 return jsonify(updated_music)

#     if request.method == 'DELETE':
#         for index, music in enumerate(music_list):
#             if music['id'] == id:
#                 music_list.pop(index)
#                 return jsonify(music_list)


# if __name__ == '__main__':
#     app.run(debug=True)
# ---------------------------------------------------------------------------------------------------------


from flask import Flask, request, jsonify
import sqlite3
app = Flask(__name__)


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("musics.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn


@app.route('/musics', methods=["GET", "POST"])
def music():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM music")
        musics = [dict(id=row[0], artist=row[1], language=row[2],
                    title=row[3]) for row in cursor.fetchall()]
        if musics is not None:
            return jsonify(musics)

    if request.method == "POST":
        new_artist = request.json['artist']
        new_language = request.json['language']
        new_title = request.json['title']
        sql = """INSERT INTO music (artist, language, title) VALUES (?, ?, ?)"""

        cursor = cursor.execute(sql, (new_artist, new_language, new_title))
        conn.commit()
        message = "Music with the id: " + str(cursor.lastrowid) + " created successfully"
        return jsonify(message), 201


@app.route('/music/<int:id>', methods=["GET", "PUT", "DELETE"])
def single_music(id):
    conn = db_connection()
    cursor = conn.cursor()
    music = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM music WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            music = r
        if music is not None:
            return jsonify(music), 200
        else:
            return "Something Wrong", 404

    if request.method == "PUT":
        sql = """UPDATE music 
                SET artist=?,
                    language=?,
                    title=?
                WHERE id=?"""
        
        artist = request.json['artist']
        language = request.json['language']
        title = request.json['title']
        updated_music = {
            'id': id,
            'artist': artist,
            'language': language,
            'title': title
        }
        conn.execute(sql, (artist, language, title, id))
        conn.commit()
        return jsonify(updated_music)

    if request.method == "DELETE":
        sql = """ DELETE FROM music WHERE id=?"""
        conn.execute(sql, (id,))
        conn.commit()
        return "The music with id: {} has been deleted.".format(id),200

if __name__ == '__main__':
    app.run(debug=True)

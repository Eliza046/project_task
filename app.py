from flask import Flask, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
CORS(app)
db = SQLAlchemy(app)
Migrate(app, db)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    is_done = db.Column(db.Boolean, nullable=False, default=False)

def present_task(task):
    return {
        "id": task.id,
        "title": task.title,
        "is_done": task.is_done
    }

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return [present_task(task) for task in tasks]

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()

    if not data.get('title'):
        return jsonify({'error': 'no title'}), 400

    task = Task(title=data['title'])
    db.session.add(task)
    db.session.commit()

    return present_task(task)

@app.route('/api/tasks/<int:id>', methods=['DELETE'])
def remove_task(id):
    task = Task.query.get(id)

    if task:
        db.session.delete(task)
        db.session.commit()

    return jsonify({"deleted_id": id})

@app.route('/api/tasks/<int:id>', methods=['GET'])
def save_done(id):
    task = Task.query.get(id)

    if task.is_done == True:
        task.is_done = False
    else:
        task.is_done = True


    db.session.add(task)
    db.session.commit()

    return jsonify({"saved_id": id})

@app.route('/api/tasks/<int:id>', methods=['PATCH'])
def change_task(id):
    task = Task.query.get(id)

    data = request.get_json()
    if not data.get('title'):
        return jsonify({'error': 'no title'}), 400

    task.title=data['title']
    task.is_done=data['is_done']

    db.session.add(task)
    db.session.commit()

    return present_task(task)



if __name__ == '__main__':
    app.run(debug=True, port=8080)
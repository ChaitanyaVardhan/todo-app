from flask import Blueprint
from db import get_db


bp = Blueprint(__name__, 'todo/api/v1.0')

bp.route('/tasks', methods=['GET'])
def get_task():
    db = get_db()
    tasks = db.execute(
        'SELECT t.id, title, description, done '
        'FROM User u JOIN Task t ON u.id = t.owner_id '
        'WHERE u.id = ?', 
        (g.user['id'],)
    ).fetchall()

    return jsonify(tasks)


@bp.route('/tasks/<int:id>', methods=['GET'])
def get_task_for_id(id):
    db = get_db()
    task = db.execute(
        'SELECT t.id, title, description, done '
        'FROM User u JOIN Task t on u.id = t.owner_id '
        'WHERE u.id = ? and t.id = ?',
        (g.user['id'], id)
    ).fetchone()

    return jsonfiy(tasks)


bp.route('/tasks', methods=['POST'])
def post_task():
    title = request.data['title']
    description = request.data['description']
    done = request.data['done']
    db = get_db()
    response = db.execute(
        'INSERT INTO Task (title, description, done, owner_id) '
        'VALUES (?,?,?,?) ',
        (title, description, done, g.user['id'])
    )

    return jsonify(response)


@bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    db = get_db()
    resposne = db.execute(
        'UPDATE Task ()'
    )


@bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    pass

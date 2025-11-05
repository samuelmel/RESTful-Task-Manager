# app/routes.py
from flask import Blueprint, request, jsonify
from .models import db, Task 
import os 

bp = Blueprint('api', __name__, url_prefix='/tasks') 

@bp.route("/", methods=['POST'])
def create_tasks():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"message": "O campo 'title' é obrigatório"}), 400

    new_task = Task(
        title=data['title'], 
        description=data.get('description'),
        status=data.get('status', False)
    )

    db.session.add(new_task)
    db.session.commit()

    return jsonify(new_task.to_dict()), 201

@bp.route("/", methods=['GET'])
def get_tasks():
    tasks = db.session.execute(db.select(Task)).scalars().all()
    serializer = [task.to_dict() for task in tasks]
    return jsonify(serializer)


@bp.route("/<int:task_id>", methods=['GET'])
def get_task(task_id):
    task = db.get_or_404(Task, task_id)
    return jsonify(task.to_dict())

@bp.route("/<int:task_id>", methods=['PUT'])
def update_task(task_id):
    task = db.get_or_404(Task, task_id)
    data = request.get_json()
    
    if 'title' in data:
        task.title = data['title']
    if 'description' in data:
        task.description = data['description']
    if 'status' in data:
        task.status = data['status']
        
    db.session.commit()
    return jsonify(task.to_dict())

@bp.route("/<int:task_id>", methods=['DELETE'])
def delete_task(task_id):
    task = db.get_or_404(Task, task_id)
    db.session.delete(task)
    db.session.commit()
    
    return "", 204
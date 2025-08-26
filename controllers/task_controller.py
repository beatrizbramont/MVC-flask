from flask import render_template, request, redirect, url_for
from models import db
from models.task import Task
from models.user import User

class TaskController:
    @staticmethod
    def list_tasks():
        tasks = db.session.query(Task).all()
        # Confirme o nome correto do template abaixo
        return render_template("tasks.html", tasks=tasks)  

    @staticmethod
    def create_task():
        if request.method == 'GET':
            users = db.session.query(User).all()
            return render_template("create_task.html", users=users)
        else:
            title = request.form['title']
            description = request.form['description']
            user_id = request.form['user_id']
            new_task = Task(title=title, description=description, user_id=user_id)
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for('list_tasks'))

    @staticmethod
    def update_task_status(task_id):
        # Você pode usar db.session.get(Task, task_id) se a versão permitir
        task = db.session.query(Task).get(task_id)
        if task:
            task.status = 'Concluído' if task.status == 'Pendente' else 'Pendente'
            db.session.commit()
        return redirect(url_for('list_tasks'))

    @staticmethod
    def delete_task(task_id):
        task = db.session.query(Task).get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
        return redirect(url_for('list_tasks'))

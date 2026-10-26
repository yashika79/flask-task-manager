from flask import Blueprint,render_template,request,redirect,url_for,flash,session
from app import db
from app.models import Task,User
from sqlalchemy import select,case
from app.form import EditForm
from datetime import date

tasks_bp = Blueprint('tasks',__name__)

@tasks_bp.route('/')
def view_tasks():
    form = EditForm()
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    tasks = db.session.scalars(
        select(Task).where(Task.user_id==session['user_id']).order_by(Task.created_at.asc())
    ).all()
    return render_template('tasks.html',tasks=tasks,form=form,edit_task=None,
                             today=date.today().isoformat())


@tasks_bp.route('/add',methods=['POST'])
def add_tasks():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    title = request.form.get('title','').strip()
    date_str = request.form.get('date', '').strip()

    planned_date = date.fromisoformat(date_str) if date_str else None

    if title:
        new_task = Task(title=title,status='Pending',date=planned_date, user_id=session['user_id'])

        db.session.add(new_task)
        db.session.commit()
        flash('Task added','success')
        return redirect(url_for('tasks.view_tasks'))

    return redirect(url_for('tasks.view_tasks'))


@tasks_bp.route('/edit/<int:task_id>',methods=['GET','POST'])
def edit_task(task_id):

    form = EditForm()

    if 'user_id' not in session:
        flash("Please login to edit!",'warning')
        return redirect(url_for('auth.login'))

    task = db.session.scalars(
        select(Task).where(Task.id==task_id,Task.user_id==session['user_id'])
    ).first()

    if task is None:
        flash("Task not found", "danger")
        return redirect(url_for('tasks.view_tasks'))
    
    if form.validate_on_submit():
        task.title = form.title.data.strip()
        task.date = form.date.data

        db.session.commit()

        flash("Task updated", "success")
        return redirect(url_for('tasks.view_tasks'))

    if request.method == 'GET':
        form.title.data = task.title
        form.date.data = task.date

    task_list = db.session.scalars(
        select(Task)
        .where(Task.user_id == session['user_id'])
        .order_by(Task.created_at.asc())
    ).all()

    return render_template(
        'tasks.html',
        tasks=task_list,  
        form=form,
        edit_task=task,
        today=date.today().isoformat()
    )
    
        
     
@tasks_bp.route('/toggle/<int:task_id>',methods=['POST'])
def toggle_tasks(task_id):
    if 'user_id' not in session:
        flash("Please login first.", "warning")
        return redirect(url_for('auth.login'))

    task = db.session.scalars(
        select(Task).where(Task.id==task_id,Task.user_id==session['user_id'])
    ).first()

    if task is None:
        flash("Task not found", "danger")
        return redirect(url_for('tasks.view_tasks'))
    
    if task:
        if task.status == "Pending":
            task.status = "In Progress"
        elif task.status == "In Progress":
            task.status = "Done"
        else:
            task.status = "Pending"
        db.session.commit()

    return redirect(url_for('tasks.view_tasks'))


@tasks_bp.route('/clear',methods=['POST'])
def clear_tasks():
    if 'user_id' not in session:
        flash("You need to login",'warning')
        return redirect(url_for('auth.login'))
    
    Task.query.filter_by(
        user_id = session['user_id']
    ).delete()

    db.session.commit()

    flash('All tasks cleared!','info')
    return redirect(url_for('tasks.view_tasks'))


@tasks_bp.route("/delete/<int:task_id>",methods=['POST'])
def delete_tasks(task_id):
    if 'user_id' not in session:
        flash("You need to login",'warning')
        return redirect(url_for('auth.login'))
    
    task = db.session.scalars(select(Task).filter_by(id=task_id,user_id=session['user_id'])).first()

    if task is None:
        flash("Task not found or unauthorized.", "danger")
        return redirect(url_for('tasks.view_tasks'))

    db.session.delete(task)
    db.session.commit()

    flash("Task deleted", "success")
    return redirect(url_for('tasks.view_tasks'))
from flask import Blueprint,render_template,request,redirect,url_for,flash,session
from app.form import RegistrationForm,LoginForm
from sqlalchemy import select
from app.models import User , Task
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


auth_bp = Blueprint('auth',__name__)


@auth_bp.route('/register',methods=['POST','GET'])
def register():
    form =  RegistrationForm()

    if form.validate_on_submit():

        username = form.name.data
        email = form.email.data

       # Check username
        username_exists = db.session.scalars(
            select(User).where(User.username == username)
        ).first()

        # Check email
        email_exists = db.session.scalars(
            select(User).where(User.email == email)
        ).first()

        if username_exists and email_exists:
            flash("This account is already registered!", "warning")
            return redirect(url_for('auth.login'))

        elif username_exists:
            flash("This username already exists. Please choose another username.", "warning")
            return redirect(url_for('auth.register'))

        elif email_exists:
            flash("You have already registered with this email!", "warning")
            return redirect(url_for('auth.login'))

        else:
            hashed_password = generate_password_hash(form.password.data)

            user = User(username=form.name.data,email=form.email.data,password_hash=hashed_password)

            db.session.add(user)
            db.session.commit()  

            session['user_id'] = user.id #automatic login
            session['user_name'] = user.username

            flash('Registration successful', 'success')
            return redirect(url_for('tasks.view_tasks')) 
        
    return  render_template('register.html',form = form)

@auth_bp.route('/login',methods = ['GET','POST'])
def login():
    form =  LoginForm()

    # if 'user_id' in session:
    #     return redirect(url_for('tasks.view_tasks'))

    if form.validate_on_submit():
        username = form.name.data
        password = form.password.data

        stmt  = select(User).where(User.username==username)
        user = db.session.scalars(stmt).first()

        if user is None:
            flash('Invalid username. Please check your username.', 'danger')

        elif not check_password_hash(user.password_hash, password):
            flash('Incorrect password. Please try again.', 'danger')

        else:
            session['user_id'] = user.id
            session['user_name'] = user.username
            flash('Login successful!', 'success')
            return redirect(url_for('tasks.view_tasks'))

    return render_template('login.html', form=form)
    

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Logged out','info')
    return redirect(url_for('auth.login'))

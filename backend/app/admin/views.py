from . import admin
from flask import jsonify, request, render_template, session, url_for, redirect
from .models.Admin import Admin
from ..auth.models.User import User
from app import bcrypt


@admin.route('/api/v1/admin', methods=['GET'])
def get_all_admin():
    return jsonify(Admin.get_all())

@admin.cli.command('create_admin')
def create_admin():
    """Create admin: Allows you to enter a username and password to create an admin"""
    username = input('Enter username: ')
    password = input('Enter password: ')

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    admin = Admin(username=username, password=hashed_password)
    admin.save()
    print('Admin created')


@admin.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        admin = Admin.get_by_username(username)
        print(admin)

        if admin and bcrypt.check_password_hash(admin.password, password):
            session['admin_id'] = admin.id
            return redirect(url_for('admin.create_supervisors'))
        else:
            return render_template("index.html", error="Invalid username or password")


    return render_template("index.html")


@admin.route("/create_supervisor", methods=['GET', 'POST', 'PUT'])
def create_supervisors():
    if request.method == 'PUT':
        username = request.form.get('username')
        print("username: "+username)
        full_name = request.form.get('full_name')
        print("full_name: "+full_name)
        password = request.form.get('password')
        print("password: "+password)
        role = request.form.get('role')
        print(f"role: {role}")
        email = request.form.get('email')
        print(f"email: {email}")
        id = request.form.get('id')
        print(f"id: {id}")
        
        if username is None or password is None or full_name is None or role is None or email is None:
            return render_template("supervisor.html", error="Please fill in all fields")

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        user = User(username=username, full_name=full_name, password=hashed_password, role=role, email=email)
        user.update(id)
        return redirect(url_for('admin.create_supervisors'))
       
    if request.method == 'POST':
        username = request.form.get('username')
        print("username: "+username)
        full_name = request.form.get('full_name')
        print("full_name: "+full_name)
        password = request.form.get('password')
        print("password: "+password)
        role = request.form.get('role')
        print(f"role: {role}")
        email = request.form.get('email')
        print(f"email: {email}")
        
        if username is None or password is None or full_name is None or role is None or email is None:
            return render_template("supervisor.html", error="Please fill in all fields")

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        user = User(username=username, full_name=full_name, password=hashed_password, role=role, email=email)
        user.save()
        return redirect(url_for('admin.create_supervisors'))
    else:
        if session.get('admin_id') is None:
            return redirect(url_for('admin.index'))

        supervisors = User.get_by_role('supervisor')
        print(supervisors)
        return render_template("supervisor.html", supervisors=supervisors)

@admin.route('/supervisor', methods=['GET', 'POST'])
def supervisor():
    if session.get('admin_id') is None:
        return redirect(url_for('admin.index'))
    supervisors = User.get_by_id(request.args.get('id'))
    print(supervisors)
    return render_template("a_supervisor.html", supervisor=supervisors)


@admin.route('/logout')
def logout():
    session.pop('admin_id')
    return redirect(url_for('admin.index'))
from app import app
from flask import render_template
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():  # put application's code here
    user = {'username': 'Thomas'}
    classes = [{'classInfo': {'code': 'CSC324', 'title': 'Software Testing and DevOps'}, 'instructor': 'Baoqiang Yan'},
               {'classInfo': {'code': 'CSC374', 'title': 'Linux Administration'}, 'instructor': 'Baoqiang Yan'},
               {'classInfo': {'code': 'CSC208', 'title': 'Discrete Structures'}, 'instructor': 'Baoqiang Yan'},
               {'classInfo': {'code': 'CSC386', 'title': 'Operating System Concept'}, 'instructor': 'Yipkei Kwok'},
               {'classInfo': {'code': 'CSC318', 'title': 'Simulation and Modeling'}, 'instructor': 'Kent Pickett'}]
    return render_template('index.html', title='Home', user=user, classes=classes)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


now = datetime.now()
iso_now = now.isoformat()
print(iso_now)

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'MLXH243GssUWwKdTWS7FDhdwYF56wPj8'

db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    projectName = db.Column(db.String(100), nullable=False)
    projectDescription = db.Column(db.Text, nullable=True)
    projectParticipant = db.Column(db.String(500), nullable=False)
    dateCreated = db.Column(db.DateTime(timezone=True), server_default=iso_now)
    
    def __init__(self, projectName, projectDescription, projectParticipant):
        self.projectName = projectName
        self.projectDescription = projectDescription
        self.projectParticipant = projectParticipant

@app.route('/')
def index():
    projects = Project.query.order_by(Project.dateCreated.desc()).all()
    return render_template('index.html', projects=projects)

@app.route('/addProject')
def addProject():
    return render_template('createProject.html')

@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == "POST":
        projectName = request.form.get("projectName")
        projectDescription = request.form.get("projectDescription")
        projectParticipant = request.form.get("projectParticipant")
        newProject = Project(projectName, projectDescription, projectParticipant)
        db.session.add(newProject)
        db.session.commit()
    return redirect("/")

@app.route("/<int:id>/delete")
def delete(id):
    project_to_delete = Project.query.get_or_404(id)
    # print(project_to_delete)
    db.session.delete(project_to_delete)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='80')
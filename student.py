
from flask import Flask, request,render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import matplotlib.pyplot as plt
import numpy as np

app=Flask(__name__)
app.secret_key="A Coder"
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:''@localhost/students"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
class Data(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    fathername=db.Column(db.String(200))
    age=db.Column(db.String(100))
    classs=db.Column(db.String(200))
    phone=db.Column(db.Integer())
    email=db.Column(db.String(200))
    address=db.Column(db.String(100))
    def __init__(self,name,fathername,age,classs,phone,email,address):
        self.name=name
        self.fathername=fathername
        self.age=age
        self.classs=classs
        self.phone=phone
        self.email=email
        self.address=address
@app.route('/')
def index():
    #data
    year=np.array([2018,2019,2020,2021,2022])
    student=np.array([150,240,200,220,300])
    plt.ylabel('Years')
    plt.xlabel('Students')
    plt.title("Students Chart In 5 Years")
    plt.bar(year,student)
    plt.savefig('static/student.png')
    all_data=Data.query.all()
    return render_template('index.html',students=all_data,surl='/static/student.png')

@app.route('/insert',methods= ['POST'])
def insert():
  if request.method == 'POST':
        name=request.form['name']
        fathername=request.form['fathername']
        age=request.form['age']
        classs=request.form['classs']
        phone=request.form['phone']
        email=request.form['email']
        address=request.form['address']

        studentdata=Data(name,fathername,age,classs,phone,email,address)
        db.session.add(studentdata)
        db.session.commit()
        return redirect(url_for('index'))
@app.route('/update',methods=['GET','POST'])
def update():
        
        if request.method=='POST':
            all_data=Data.query.get(request.form.get('id'))
            all_data.name=request.form['name']
            all_data.fathername=request.form['fathername']
            all_data.age=request.form['age']
            all_data.classs=request.form['classs']
            all_data.phone=request.form['phone']
            all_data.email=request.form['email']
            all_data.address=request.form['address']
            db.session.commit()
            return redirect(url_for('index'))
@app.route('/delete/<id>/',methods=['GET','POST'])
def delete(id):
    students=Data.query.get(id)
    db.session.delete(students)
    db.session.commit()
    return redirect(url_for('index'))
if __name__=='__main__':
    app.run(debug=True)


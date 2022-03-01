import re
from flask import Flask,render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///students.db"
db=SQLAlchemy(app)

class Student(db.Model):
    SNo= db.Column(db.Integer, primary_key=True)
    Department= db.Column(db.String(255),nullable=False)
    Name=db.Column(db.String(255),nullable=False)
    Marks=db.Column(db.String(255),nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.name}"



@app.route("/",methods=["GET", "POST"])
def home():
    if request.method=="POST":
        Department=(request.form["Department"])
        Name=(request.form["name"])
        Marks=(request.form["marks"])
        students=Student(Department=Department,Name=Name,Marks=Marks)
        db.session.add(students)
        db.session.commit()
    allstudents=Student.query.all()
    return render_template("index.html", allstudents=allstudents)



@app.route("/delete/<int:SNo>")
def delete(SNo):
    deletestudent=Student.query.filter_by(SNo=SNo).first()
    db.session.delete(deletestudent)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
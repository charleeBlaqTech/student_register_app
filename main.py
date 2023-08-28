from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
from models.db_connect  import register_new_student
load_dotenv()


app = Flask(__name__)

student= register_new_student


# Routes===============SECTION=============

@app.route('/')
@app.route('/index')
def index_render():
    students= student.find({})
    return render_template('index.html',
                           students = students
                           )


@app.route('/admin/')
def admin_render(): 
    return render_template('admin.html')
    


@app.route('/admin/create_student', methods=["GET", "POST"])
def create_new_student():
    student_name = request.form.get('fullname')
    student_age = request.form.get('age')
    student_courses = request.form.get('courses')
    if not bool(student_name.strip()):
        student_name = ""

    if not bool(student_age.strip()):
        student_age = ""
    
    if not bool(student_courses.strip()):
        student_courses = ""
   
    if student_name == "" or student_age == "" or student_courses == "":
        return render_template("admin.html", ERROR= "Inputs cannot be empty")
    else:
        create_student_database= student.insert_one({
            "name": student_name,
            "age": int(student_age),
            "courses": int(student_courses)
        })   
        if bool(create_student_database):
            return redirect("/index") 
        else:
            return render_template('admin.html', ERROR= "Database error, student data not created successfully")  

    
   
    











if __name__ == "__main__":
    app.debug= True
    app.run(host="localhost", port= 3030)
    # serve(app,host="localhost", port= 3030) this is for production server
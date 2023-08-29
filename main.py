from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
from models.db_connect  import register_new_student
from models.db_connect  import register_new_tutor
load_dotenv()


app = Flask(__name__)

# Database collections
student= register_new_student
teacher= register_new_tutor


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
    total_students= student.count_documents({})
    total_tutors= teacher.count_documents({})
    return render_template('admin.html', students= total_students, teachers= total_tutors)
    


@app.route('/admin/create_student', methods=["GET", "POST"])
def create_new_student():
    student_name = request.form.get('fullname')
    student_DOB = request.form.get('dateofbirth')
    student_age = request.form.get('age')
    student_course = request.form.get('stdCourse')
    if not bool(student_name.strip()):
        student_name = ""

    if not bool(student_DOB.strip()):
        student_DOB = ""

    if not bool(student_age.strip()):
        student_age = ""
    
    if not bool(student_course.strip()):
        student_course = ""
   
    if student_name == "" or student_age == "" or student_course == "" or student_DOB == "":
        return redirect("/admin/", 302)
    else:
        try:
            created_student = student.insert_one({
                "name": student_name,
                "age": int(student_age),
                "courses": student_course,
                "DOB": student_DOB
            })   
            if bool(created_student):
                return redirect("/admin/")  
                    
        except Exception as error:
            # ERROR= "Database error, student data not created successfully"
            return render_template('admin.html', ERROR= error ) 
        

@app.route('/admin/create_tutor', methods=["GET", "POST"])
def create_new_tutor():

    tutor_name = request.form.get('fullname')
    tutor_DOB = request.form.get('dateofbirth')
    tutor_course = request.form.get('course')
    tutor_class = request.form.get('classDay')
    if not bool(tutor_name.strip()):
        tutor_name = ""

    if not bool(tutor_DOB.strip()):
        tutor_DOB = ""

    if not bool(tutor_course.strip()):
        tutor_course = ""
    
    if not bool(tutor_class.strip()):
        tutor_class = ""
   
    if tutor_name == "" or tutor_class == "" or tutor_course == "" or tutor_DOB == "":
        return redirect("/admin/", 302)
    else:
        try:
            created_tutor = teacher.insert_one({
                "name": tutor_name,
                "class": tutor_class,
                "course": tutor_course,
                "DOB": tutor_DOB
            })   
            if bool(created_tutor):
                return redirect("/admin/")  
                    
        except Exception as error:
            # ERROR= "Database error, student data not created successfully"
            return render_template('admin.html', ERROR= error ) 



       
    
   
    











if __name__ == "__main__":
    app.debug= True
    app.run(host="localhost", port= 3030)
    # serve(app,host="localhost", port= 3030) this is for production server
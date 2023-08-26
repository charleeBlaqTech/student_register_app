from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

# MONGODB CONNECTION SECTION USING PYMONGO
mongo_uri   = "mongodb://localhost:27017/zenith_DB"
client      = MongoClient(mongo_uri)
register_new_student       = client.zenith_DB.register



# Routes===============SECTION=============

@app.route('/')
@app.route('/index')
def index_render():
    students=register_new_student.find({})
    return render_template('index.html',
                           students = students
                           )


@app.route('/admin/')
def admin_render(): 
    return render_template('admin.html')
    


@app.route('/admin/create_student', methods=["GET", "POST"])
def create_new_student():
    student_name = request.form.get('fullname')
    student_courses = int(request.form.get('courses'))
    student_age = int(request.form.get('age'))
    create_student_database= register_new_student.insert_one({
        "name": student_name,
        "age": student_age,
        "courses": student_courses
    })
    if bool(create_student_database):
        return redirect("/index")
    











if __name__ == "__main__":
    app.debug= True
    app.run(host="localhost", port= 3030)
    # serve(app,host="localhost", port= 3030) this is for production server
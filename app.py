from flask import Flask, request  
from data import students

app = Flask(__name__)

@app.route('/students', methods=['GET'] )
def list_students_all():
    return students

@app.route('/students/<int:student_id>', methods=['GET'])
def list_student_id(student_id):
  return students.get(
      student_id,
      {'error': 'Student not found'}
  )

  @app.route('/students', methods=['POST'])
  def create_student():
    id = sorted(students.keys())[-1] +1
    new_student = {
        'name' : request.json['name'],
        'email' : request.json['email'],
        'room' : request.json['room'],
    }
    students[id] = new_student
    return new_student
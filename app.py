from flask import Flask, request, jsonify
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

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    if student_id not in students:
        return {'error': 'Student not found'}, 404

    updated_student = {
        'name': request.json.get('name', students[student_id]['name']),
        'email': request.json.get('email', students[student_id]['email']),
        'room': request.json.get('room', students[student_id]['room'])
    }
    students[student_id] = updated_student
    return updated_student

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    if student_id not in students:
        return {'error': 'Student not found'}, 404

    del students[student_id]
    return {'message': 'Student deleted successfully'}


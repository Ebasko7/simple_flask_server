from flask import Flask, jsonify
from students import students_list


app = Flask("server")

@app.route('/old_students/')
def old_students ():
    old = []
    for student in students_list:
        if student['age'] > 20:
            old.append(student)
    return jsonify(old)

@app.route('/young_students/')
def young_students():
    young = []
    for student in students_list:
        if student['age'] < 21:
            young.append(student)
    return jsonify(young)

@app.route('/advance_students/')
def advance_students ():
    advance = []
    for student in students_list:
        if student['age'] < 21 and student['grade'] == 'A':
            advance.append(student)
    return jsonify(advance)

@app.route('/student_names/')
def student_names():
    names = []
    for student in students_list:
        names.append({'first_name': student['first_name'],'last_name': student['last_name']})
    return jsonify(names)

@app.route('/student_ages/')
def student_ages():
    ages = []
    for student in students_list:
        ages.append({'first_name' : student['first_name'], 'last_name' : student['last_name'], 'age': student['age']})
    return jsonify(ages)

@app.route('/students/')
def students ():
    all_students = []
    for student in students_list:
        all_students.append(student)
    return jsonify(all_students)

app.run(debug=True, port=8000)

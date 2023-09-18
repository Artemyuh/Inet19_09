from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        last_name = request.form.get('last_name')
        first_name = request.form.get('first_name')
        student_id = request.form.get('student_id')
        
        
        data = {
            'Фамилия': last_name,
            'Имя': first_name,
            'Номер студенческого': student_id
        }
        
        return jsonify(data)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

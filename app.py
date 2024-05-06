from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    program = request.form['program']
    if program == 'International MSc in Management':
        return '1000€'
    else:
        return 'Program not supported'

if __name__ == '__main__':
    app.run(debug=True)

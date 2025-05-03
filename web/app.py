from flask import Flask, render_template, request
from password_generator import generate_password

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ""
    error = ""

    if request.method == 'POST':
        try:
            length = int(request.form.get('length', 12))
            use_upper = bool(request.form.get('uppercase'))
            use_lower = bool(request.form.get('lowercase'))
            use_digits = bool(request.form.get('digits'))
            use_symbols = bool(request.form.get('symbols'))

            password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        except Exception as e:
            error = str(e)

    return render_template('index.html', password=password, error=error)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

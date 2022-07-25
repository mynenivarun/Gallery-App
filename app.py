import flask
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'varun'
@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)

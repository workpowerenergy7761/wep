from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'DOCTOR_JB'


if __name__ == "__main__":
    app.run()

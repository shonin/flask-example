from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/template/<name>')
def hello_person(name):
    return render_template("main_template.html", name=name)

if __name__ == "__main__":
    app.debug = True
    app.run()

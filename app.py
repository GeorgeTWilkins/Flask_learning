from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html", name='what is your name?')


@app.route('/greet', methods=["POST", "GET"])
def greet():
    name = request.form["name_input"]
    return render_template("index.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, redirect 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def results():
    name = request.form['name']
    email = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    return render_template("results.html", name=name, email=email, language=language, comment=comment)

app.run(debug=True)
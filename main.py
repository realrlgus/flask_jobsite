from flask import Flask, render_template, request

app = Flask("SuperScrapper")


@app.route("/")
def home():
    return render_template("main.html")


@app.route("/report")
def report():
    word = request.args.get('word')
    return render_template("report.html", searchingBy=word)


app.run(host="localhost", port="8000")

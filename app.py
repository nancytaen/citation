from flask import Flask, render_template, request

from process import process_url_file, process_url_text

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/reference_form", methods=["POST"])
def reference_form():
    reference = []
    if request.form['urlText']:
        reference = process_url_text(request.form['urlText'])
        print(reference)
    elif request.form['urlFile']:
        process_url_file(request.form['urlFile'])
    return render_template("result.html", reference=reference)
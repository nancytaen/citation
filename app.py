from flask import Flask, render_template, request

from process import process_url_file, process_url_text

UPLOAD_FOLDER = '/uploads'

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/reference_form", methods=["POST"])
def reference_form():
    reference = []
    if request.form['urlText']:
        reference = process_url_text(request.form['urlText'])
    elif 'urlFile' in request.files:
        reference = process_url_file(request.files['urlFile'])
    print(reference)
    return render_template("result.html", reference=reference)
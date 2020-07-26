import os

from flask import Flask, render_template, request, send_from_directory

from process import process_url_file, process_url_text


app = Flask(__name__, template_folder="templates", static_folder="static")
app.config['CLIENT_TXT'] = "static/client"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/reference_form", methods=["POST"])
def reference_form():
    reference = {}
    req_file = False
    if 'reqFile' in request.form and request.form['reqFile'] == 'on':
        req_file = True

    if request.form['urlText']:
        reference, filename = process_url_text(request.form['urlText'], req_file)
    elif 'urlFile' in request.files:
        reference, filename = process_url_file(request.files['urlFile'], req_file)
    return render_template("result.html", reference=reference, filename=filename)


@app.route("/download_file/<filename>")
def download_file(filename):
    """
    download file
    """
    response = send_from_directory(app.config["CLIENT_TXT"], filename)
    return response
import sys
import openpyxl

sys.path.append('../')
dir()

from flask import Flask, render_template, request, send_file

from main import sylvanator

app = Flask(__name__)
app.debug = True


@app.route('/upload', methods=["POST"])
def convert():
    csv_file = request.files['data_file']
    if not csv_file:
        return "No file"

    result = sylvanator(csv_file)
    result.to_excel('sylvanator.xlsx')
    output = "..\sylvanator.xlsx"

    return send_file(output, as_attachment=True)


@app.route('/')
def main():
    render_template
    return render_template('csv_upload.html')


if __name__ == '__main__':
    app.run()

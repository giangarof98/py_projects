from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('db.txt', mode='a') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = db.write(f'\n{email}, {subject},{message}')

def write_to_csv(data):
    with open('db.csv', mode='a', newline='') as db_2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file_csv = csv.writer(db_2, delimiter=',', quotechar='"', quoting= csv.QUOTE_MINIMAL)
        file_csv.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('thank_you.html')
    else:
        return 'try again'


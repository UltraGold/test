
import multitasking
import os
from flask import Flask, render_template

@multitasking.task
def just_do_it():
    os.system("python verygood.py")

just_do_it()

application = Flask(__name__)
@application.route('/')
def home():
    return render_template('log.html')
if __name__ == '__main__':
    application.run(debug=True)

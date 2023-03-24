from flask import Flask, render_template, url_for

main = Flask(__name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/ticket')
def ticket():
    return render_template('ticket.html')

@main.route('/sait')
def sait():
    return render_template('sait.html')

main.run()

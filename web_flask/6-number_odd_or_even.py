#!/usr/bin/python3

"""Script that prepares a Flask web app"""

from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")
app.url_map.strict_slashes = False


@app.route('/')
def hi_hbnb():
    """display “Hello HBNB!” on the terminal"""
    return 'Hello HBNB!'


@app.route('/hbnb',)
def hbnb():
    """Display HBNB"""
    return 'HBNB!'


@app.route('/c/<text>')
def c(text):
    """display c follow by the value"""
    repla = text.replace('_', ' ')
    return 'C {}' .format(repla)


@app.route('/python')
@app.route('/python/<text>')
def python(text="is cool"):
    """Display python follow by the text"""
    repla = text.replace('_', ' ')
    return 'Python {}' .format(repla)


@app.route('/number/<int:n>')
def n_print(n):
    """display “n is a number” only if n is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """displays a HTML page only if n is int"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Displays only if n is integer"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

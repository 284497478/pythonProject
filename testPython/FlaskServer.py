from flask import Flask, render_template
from time import sleep
app = Flask("__main__")


@app.route('/test1')
def test1():
    sleep(2)
    return render_template('test.html')


@app.route('/test2')
def test2():
    sleep(2)
    return render_template('test.html')


@app.route('/test3')
def test3():
    sleep(2)
    return render_template('test.html')


if __name__ == "__main__":
    app.run(debug=True)
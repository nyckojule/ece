from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def admin():
    return render_template("home.html")


@app.route('/main.html')
def main():
    return render_template("main.html")


@app.route('/home.html')
def back():
    return render_template("home.html")


@app.route('/contact.html')
def contact():
    return render_template("contact.html")


@app.route('/about.html')
def about():
    return render_template("about.html")


@app.route('/fpa.html')
def fpa():
    return render_template("fpa.html")


@app.route('/hm.html')
def hm():
    return render_template("hm.html")


@app.route('/lpa.html')
def lpa():
    return render_template("lpa.html")

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    # return "Hello, SmartNinja!"

@app.route("/about")
def about_me():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/portfolio/fakebook")
def portfolio_fakebook():
    return render_template("/Users/andrepereiradevasconcelos/PycharmProjects/Fakebook/index.html")

@app.route("/portfolio/boogle")
def portfolio_boogle():
    return render_template("/Users/andrepereiradevasconcelos/PycharmProjects/Boogle/index.html")

if __name__ == '__main__':
    app.run(use_reloader=True)



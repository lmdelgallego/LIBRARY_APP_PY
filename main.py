from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = [
    # {
    #     "title": "Harry Potter",
    #     "author": "J. K. Rowling",
    #     "rating": 9,
    # }
]


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add")
def add():
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)


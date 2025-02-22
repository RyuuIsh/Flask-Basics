from flask import Flask
app = Flask(__name__)

print(__name__)

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p> ' \
           '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnNqN2hqbDhybXlwN3JvdHRzcW1jMm91ZGU4cjk2NnF6eDJtZ3FkbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/lJNoBCvQYp7nq/giphy.gif" width=200>'

@app.route("/bye")
# @make_bold
# @make_emphasis
# @make_underlined
def bye():
    return "Bye!"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}!, you are {number} year old!"

if __name__ == "__main__":
    app.run(debug=True)

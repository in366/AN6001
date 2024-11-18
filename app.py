#
#


from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/main", methods =["GET","POST"])
def index():
    name = request.form.get("q")

    return (render_template("main.html"))


if __name__ == "__main__":
    app.run(port = 1234)




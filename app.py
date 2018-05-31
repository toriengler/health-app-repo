
from flask import Flask, render_template, request, redirect
import healthapp

app = Flask(__name__)

@app.route("/")
def index():
    ## print the guestbook
    return render_template("hindex.html", entries=healthapp.get_entries())

@app.route("/add")
def addentry():
    ## add a guestbook entry
    return render_template("addentry.html")

@app.route("/postentry", methods=["POST"])
def postentry():
    name = request.form["name"]
    message = request.form["message"]
    healthapp.add_entry( message)
    return redirect("/add")

if __name__=="__main__":
    healthapp.init()
    app.run(debug=True)

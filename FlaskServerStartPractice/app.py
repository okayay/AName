from flask import Flask
from flask import render_template
import templates
from flask import request
from flask import redirect
app = Flask(__name__)
messagelist = []
texto = open("C:/Users/super/Downloads/textfiletest1.txt", "r")
idlist = eval(texto.readline())
print(idlist)
#idlist = open("C:/Users/super/Downloads/textfiletest1.txt", "r")
@app.route('/', methods=["POST","GET"])
def login():
    if request.method == "POST":
        print("logining in " + request.form["username"])
        idlist.append(request.form["username"])
        text = open("C:/Users/super/Downloads/textfiletest1.txt", "r+")
        test = str(idlist)
        text.write(test)
        return redirect("/messages/"+request.form["username"])
    return render_template("login.html")

@app.route('/messages/<id>', methods=["POST","GET"])
def messages(id):
    if id in idlist:
        if request.method == "POST":
            print(request.form["message"])
            messagelist.append(request.form["message"])
            return render_template("messages.html", list=messagelist)
        elif request.method == "GET":
            return render_template("messages.html", list=messagelist)
    else:
        return render_template("login.html")
@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)
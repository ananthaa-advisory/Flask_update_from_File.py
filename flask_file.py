# How to run in Background job as flask application:
# sudo nohup python3.6 /home/flask1.py > /tmp/flask.logs 2>&1 &
import sys
from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__, template_folder="/root/templates")

@app.route('/search4', methods=["GET","POST"])

def search():
    with open("test","r") as file:
         content = file.readlines()
         print(content)

    return render_template("file2.html", content = content)




if __name__ == "__main__":
    app.run(host= "0.0.0.0", debug=True)


from flask import Flask

'''
It Creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''
### WSGI Application

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this best Flask Course. This should be an amazing course."

@app.route("/index")
def index():
    return "Welcome to the index page."

@app.route("/Ankul")
def Ankul():
    return "Bhaiya hm Sikh rhe h flask aur aayega mja isme"


if __name__  == "__main__":
    app.run(debug=True)
from flask import Flask, render_template
app = Flask(__name__)

print(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/4')
def check4():
    return render_template("index4.html")

@app.route('/<int:x>/<int:y>')
def xyindex(x,y):
    return render_template("xyindex.html",id_num1=x,id_num2=y)

@app.route('/listusers')
def listofusers():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("table.html", allofusers=users)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("Table.html")
    
@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/entornos_virtuales_python")
def entornos_virtuales_python():
  return render_template("entornos_virtuales_python.html")

@app.route("/flask_tutorial")
def flask_tutorial():
  return render_template("flask_tutorial.html")
  
if __name__ == '__main__':
  app.run(debug=True)
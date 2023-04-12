from flask import Flask, render_template, url_for 

app = Flask("__name__")

@app.route("/")
def home():
   #return "<h1>Ola Flask, estou rodando no servidor!</>"
   return render_template("home.html")

@app.route("/quemsomos")
def quemsomos():
   return render_template("quemsomos.html")

@app.route("/contato")
def contato():
   return render_template("contato.html")
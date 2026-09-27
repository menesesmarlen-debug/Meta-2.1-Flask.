from flask import Flask, render_template
from productos import productos

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/productos")
def mostrar_productos():
    return render_template("productos.html", productos=productos)


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

lista = []

@app.route("/")
def home():
    return render_template("base.html", lista_front=lista)


@app.route("/add", methods=["POST"])
def add():

    selecao = request.form.get("selecao")
    continente = request.form.get("continente")
    titulos = request.form.get("titulos")

    if selecao and continente and titulos:

        lista.append([
            selecao.strip(),
            continente.strip(),
            titulos.strip()
        ])

    return redirect(url_for("home"))


@app.route("/sort", methods=["POST"])
def sort():

    lista.sort()

    return redirect(url_for("home"))


@app.route("/reverse", methods=["POST"])
def reverse():

    global lista

    lista = sorted(
        lista,
        reverse=True,
        key=lambda x: x[0]
    )

    return redirect(url_for("home"))


@app.route("/clear", methods=["POST"])
def clear():

    global lista

    lista = []

    return redirect(url_for("home"))


@app.route("/delete/<selecao>")
def delete(selecao):

    global lista

    for i in range(len(lista)):

        if selecao == lista[i][0]:

            del lista[i]
            break

    return redirect(url_for("home"))


app = app


if __name__ == "__main__":

    app.run(debug=True)

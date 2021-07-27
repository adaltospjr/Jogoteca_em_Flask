from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def ola():
    lista = ['Gears of War', 'Days Gone', 'AC Origins', 'Journey']
    return render_template('lista.html', titulo='Jogos', jogos=lista)

#app.run(host='0.0.0.0', port=8080)
app.run()

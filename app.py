from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
produtos = []
proximo_id = 1

@app.route('/')
def index():
    return render_template('index.html', produtos=produtos)

@app.route('/add', methods=['POST'])
def add():
    global proximo_id
    nome = request.form['nome']
    preco = float(request.form['preco'])
    quantidade = int(request.form['quantidade'])
    produtos.append({'id': proximo_id, 'nome': nome, 'preco': preco, 'quantidade': quantidade})
    proximo_id += 1
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    global produtos
    produtos = [p for p in produtos if p['id'] != id]
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    produto = next((p for p in produtos if p['id'] == id), None)
    if request.method == 'POST':
        produto['nome'] = request.form['nome']
        produto['preco'] = float(request.form['preco'])
        produto['quantidade'] = int(request.form['quantidade'])
        return redirect(url_for('index'))
    return render_template('edit.html', produto=produto)

if __name__ == '__main__':
    app.run(debug=True)
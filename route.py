from app.controllers.application import Application
from bottle import Bottle, route, run, request, static_file
from bottle import redirect, template, response


app = Bottle()
ctl = Application()


#-----------------------------------------------------------------------------
# Rotas:

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

@app.route('/helper')
def helper(info= None):
    return ctl.render('helper')


#-----------------------------------------------------------------------------
# Suas rotas aqui:

@app.route('/')
def index():
    return redirect('/portal')

@app.route('/portal', method=['GET'])
def portal():
    return ctl.render('portal')

@app.route('/portal/login', method=['POST'])
def login():
    return ctl.login(request.forms.getunicode('username', ''), request.forms.getunicode('password', ''))

@app.route('/portal/logout', method=['POST'])
def logout():
    return ctl.logout()

@app.route('/banco', method=['GET'])
def banco():
    return ctl.render('banco')

@app.route('/banco/livros', method=['POST'])
def create_livro():
    livro = ctl.create_livro(
        request.forms.getunicode('titulo', ''), request.forms.getunicode('autor', ''),
    )
    if livro is None:
        response.status = 401
        return {'erro': 'Autenticação necessária.'}
    if livro is False:
        response.status = 400
        return {'erro': 'titulo e autor são obrigatórios.'}
    response.status = 201
    return {'titulo': livro.titulo, 'autor': livro.autor}

@app.route('/banco/livros/<index>', method=['DELETE'])
def delete_livro(index):
    livro = ctl.delete_livro(index)
    if livro is None:
        if not ctl.authenticated_user():
            response.status = 401
            return {'erro': 'Autenticação necessária.'}
        response.status = 404
        return {'erro': 'Livro não encontrado.'}
    return {'titulo': livro.titulo, 'autor': livro.autor}



#-----------------------------------------------------------------------------


if __name__ == '__main__':

    run(app, host='0.0.0.0', port=8080, debug=True)

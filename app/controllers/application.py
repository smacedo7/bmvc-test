from bottle import redirect, request, response, template

from app.controllers.datarecord import DataRecord


class Application():

    def __init__(self):
        self.pages = {
            'portal': self.portal,
            'banco': self.banco,
        }
        self.models = DataRecord()


    def render(self,page):
       content = self.pages.get(page, self.helper)
       return content()


    def helper(self):
        return template('app/views/html/helper')

    def authenticated_user(self):
        return request.get_cookie('bmvc_user', secret='bmvc-exercicio')

    def portal(self, message=None):
        return template(
            'app/views/html/portal',
            user=self.authenticated_user(),
            message=message,
        )

    def login(self, username, password):
        if not self.models.authenticate(username, password):
            return self.portal('Usuário ou senha inválidos.')
        response.set_cookie('bmvc_user', username, secret='bmvc-exercicio', path='/')
        redirect('/banco')

    def logout(self):
        response.delete_cookie('bmvc_user', path='/')
        redirect('/portal')

    def banco(self, message=None):
        user = self.authenticated_user()
        if not user:
            redirect('/portal')
        return template(
            'app/views/html/banco',
            user=user,
            livros=self.models.list_livros(),
            message=message,
        )

    def create_livro(self, titulo, autor):
        if not self.authenticated_user():
            return None
        if not titulo or not autor:
            return False
        return self.models.create_livro(titulo, autor)

    def delete_livro(self, index):
        if not self.authenticated_user():
            return None
        return self.models.delete_livro(index)

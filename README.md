# Portal e Banco de Livros — BMVC

Aplicação desenvolvida com o framework BMVC para o gerenciamento básico de
livros. O sistema possui dois recursos: `portal`, responsável pela
autenticação, e `banco`, responsável pela consulta dos livros cadastrados.

## Funcionalidades

- Login de usuários pelo modelo `UserAccount`;
- Controle de acesso: somente usuários autenticados acessam o recurso `banco`;
- Listagem de livros no próprio sistema (READ);
- Inclusão de livros por requisição HTTP (CREATE);
- Exclusão de livros por requisição HTTP (DELETE);
- Persistência dos dados em arquivos JSON.

Cada livro possui os atributos `titulo` e `autor`.

## Estrutura

O projeto segue a organização do BMVC:

- `route.py`: definição das rotas da aplicação;
- `app/controllers/application.py`: controlador principal;
- `app/controllers/datarecord.py`: acesso e persistência dos dados;
- `app/models/`: modelos `UserAccount` e `Livro`;
- `app/controllers/db/`: arquivos JSON utilizados como banco de dados;
- `app/views/html/`: páginas do sistema.

## Como executar

Na raiz do projeto, execute:

```bash
docker build -t bmvc-livros .
docker run --rm -p 8080:8080 -v "$(pwd)":/bmeta bmvc-livros
```

Em seguida, acesse no navegador:

```text
http://localhost:8080/portal
```

### Credenciais de demonstração

```text
Usuário: aluno
Senha: 123456
```

Após o login, o recurso `banco` estará disponível em:

```text
http://localhost:8080/banco
```

## Testes com cURL

Abra outro terminal na raiz do projeto e autentique-se:

```bash
curl -i -c cookies.txt -X POST http://localhost:8080/portal/login \
  -d 'username=aluno' \
  -d 'password=123456'
```

Para cadastrar um livro:

```bash
curl -i -b cookies.txt -X POST http://localhost:8080/banco/livros \
  -d 'titulo=O Alienista' \
  -d 'autor=Machado de Assis'
```

Para excluir um livro, informe o índice exibido na primeira coluna da página
`/banco`:

```bash
curl -i -b cookies.txt -X DELETE http://localhost:8080/banco/livros/2
```

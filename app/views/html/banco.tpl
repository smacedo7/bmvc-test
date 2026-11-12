<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Banco de Livros | BMVC</title>
  <link rel="stylesheet" href="/static/css/exercicio.css">
</head>
<body>
  <main class="card wide">
    <header><h1>Banco de Livros</h1><p>Usuário autenticado: <strong>{{user}}</strong></p></header>
    <p>O READ é exibido aqui, no próprio recurso <code>banco</code>.</p>
    <table>
      <thead><tr><th>#</th><th>Título</th><th>Autor</th></tr></thead>
      <tbody>
      % for index, livro in enumerate(livros):
        <tr><td>{{index}}</td><td>{{livro.titulo}}</td><td>{{livro.autor}}</td></tr>
      % end
      </tbody>
    </table>
    <p class="hint">CREATE e DELETE estão disponíveis por cURL. Veja o README.</p>
    <p><a href="/portal">Voltar ao portal</a></p>
  </main>
</body>
</html>

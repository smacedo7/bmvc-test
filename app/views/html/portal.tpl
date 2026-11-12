<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Portal | BMVC</title>
  <link rel="stylesheet" href="/static/css/exercicio.css">
</head>
<body>
  <main class="card">
    <h1>Portal BMVC</h1>
    % if user:
      <p>Você está autenticado como <strong>{{user}}</strong>.</p>
      <p><a href="/banco">Acessar o banco de livros</a></p>
      <form action="/portal/logout" method="post"><button>Sair</button></form>
    % else:
      <p>Faça login para acessar o recurso <code>banco</code>.</p>
      % if message:
        <p class="error">{{message}}</p>
      % end
      <form action="/portal/login" method="post">
        <label>Usuário <input name="username" required></label>
        <label>Senha <input type="password" name="password" required></label>
        <button>Entrar</button>
      </form>
      <p class="hint">Conta de demonstração: <code>aluno</code> / <code>123456</code></p>
    % end
  </main>
</body>
</html>

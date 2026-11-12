"""Camada de persistência JSON do exercício BMVC."""

import json
from pathlib import Path

from app.models.livro import Livro
from app.models.user_account import UserAccount


class DataRecord:
    """Banco de dados JSON para contas de usuário e livros."""

    def __init__(self):
        self.db_path = Path(__file__).resolve().parent / "db"
        self.user_accounts = self._load_users()
        self.livros = self._load_livros()

    def _read_json(self, filename, default):
        arquivo = self.db_path / filename
        try:
            with arquivo.open("r", encoding="utf-8") as json_file:
                return json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError):
            return default

    def _write_json(self, filename, data):
        self.db_path.mkdir(parents=True, exist_ok=True)
        arquivo = self.db_path / filename
        with arquivo.open("w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)

    def _load_users(self):
        data = self._read_json(
            "user_accounts.json",
            [{"username": "aluno", "password": "123456"}],
        )
        return [UserAccount(**account) for account in data]

    def _load_livros(self):
        data = self._read_json(
            "livros.json",
            [
                {"titulo": "Dom Casmurro", "autor": "Machado de Assis"},
                {"titulo": "A Hora da Estrela", "autor": "Clarice Lispector"},
            ],
        )
        return [Livro(**livro) for livro in data]

    def authenticate(self, username, password):
        return any(
            account.username == username and account.password == password
            for account in self.user_accounts
        )

    def list_livros(self):
        return self.livros

    def create_livro(self, titulo, autor):
        livro = Livro(titulo.strip(), autor.strip())
        self.livros.append(livro)
        self._write_json("livros.json", [item.__dict__ for item in self.livros])
        return livro

    def delete_livro(self, index):
        try:
            livro = self.livros.pop(int(index))
        except (ValueError, IndexError):
            return None
        self._write_json("livros.json", [item.__dict__ for item in self.livros])
        return livro

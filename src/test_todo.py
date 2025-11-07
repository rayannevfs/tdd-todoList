import pytest
from todo import (
    criar_tarefa,
    STATUS_PENDENTE
)

def test_criar_tarefa_valida():
    t = criar_tarefa("Estudar TDD", "Ler sobre RED-GREEN-REFACTOR")
    assert t["titulo"] == "Estudar TDD"
    assert t["descricao"] == "Ler sobre RED-GREEN-REFACTOR"
    assert t["status"] == STATUS_PENDENTE
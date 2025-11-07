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

def test_nao_permite_titulos_duplicados_case_insensitive():
    criar_tarefa("Pagar Boleto", "Conta de luz")
    with pytest.raises(ValueError) as e:
        criar_tarefa("pagar boleto", "Conta de água")
    assert "Já existe tarefa com este título." in str(e.value)
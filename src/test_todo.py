import pytest
from todo import (
    criar_tarefa,
    listar_tarefas,
    concluir_tarefa,
    obter_tarefa,
    STATUS_PENDENTE,
    STATUS_CONCLUIDA
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

def test_nao_permite_titulo_vazio_ou_so_espacos():
    with pytest.raises(ValueError) as e:
        criar_tarefa("   ", "desc")
    assert "Título é obrigatório." in str(e.value)

def test_listar_tarefas_sem_filtro_mantem_ordem_de_criacao():
    criar_tarefa("A", "1")
    criar_tarefa("B", "2")
    itens = listar_tarefas()
    assert [i["titulo"] for i in itens] == ["A", "B"]

def test_listar_filtrando_por_status():
    criar_tarefa("A", "1")
    criar_tarefa("B", "2")
    concluir_tarefa("B")
    pendentes = listar_tarefas("pendente")
    concluidas = listar_tarefas("concluída")
    assert [i["titulo"] for i in pendentes] == ["A"]
    assert [i["titulo"] for i in concluidas] == ["B"]

def test_obter_tarefa_existente_ou_none():
    criar_tarefa("Ler livro", "Capítulo 3")
    assert obter_tarefa("Ler livro")["descricao"] == "Capítulo 3"
    assert obter_tarefa("Inexistente") is None

def test_concluir_tarefa_altera_status():
    criar_tarefa("Exercícios", "Lista 1")
    t = concluir_tarefa("Exercícios")
    assert t["status"] == STATUS_CONCLUIDA
    assert obter_tarefa("Exercícios")["status"] == STATUS_CONCLUIDA

def test_concluir_tarefa_inexistente_gera_erro():
    with pytest.raises(ValueError) as e:
        concluir_tarefa("Nada aqui")
    assert "Tarefa não encontrada." in str(e.value)

def test_concluir_tarefa_ja_concluida_gera_erro():
    criar_tarefa("Backup", "HD externo")
    concluir_tarefa("Backup")
    with pytest.raises(ValueError) as e:
        concluir_tarefa("Backup")
    assert "Tarefa já está concluída." in str(e.value)
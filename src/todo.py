_TASKS = {}

STATUS_PENDENTE = "pendente"
STATUS_CONCLUIDA = "concluída"

# ---------- helpers ----------
def _normalizar_titulo(titulo):
    if not isinstance(titulo, str):
        return ""
    return titulo.strip()

def _chave(titulo):
    return _normalizar_titulo(titulo).casefold()

def _clonar(tarefa_dict):
    return dict(tarefa_dict)

def _normalizar_status(status):
    if status is None:
        return None
    s = str(status).strip().casefold()

    if s in {"pendente", "pendentes"}:
        return STATUS_PENDENTE
    if s in {"concluida", "concluída", "concluido", "concluídos", "concluidas"}:
        return STATUS_CONCLUIDA
    raise ValueError("Status inválido. Use 'pendente' ou 'concluída'.")

# ---------- API ----------
def resetar_tarefas():
    _TASKS.clear()

def criar_tarefa(titulo, descricao):
    """
    Cria uma tarefa pendente.
    - título obrigatório
    - títulos são únicos
    Retorna um dicionário da tarefa criada.
    """
    titulo_limpo = _normalizar_titulo(titulo)
    if not titulo_limpo:
        raise ValueError("Título é obrigatório.")
    chave = _chave(titulo_limpo)
    if chave in _TASKS:
        raise ValueError("Já existe tarefa com este título.")

    tarefa = {
        "titulo": titulo_limpo,
        "descricao": descricao if descricao is not None else "",
        "status": STATUS_PENDENTE,
    }
    _TASKS[chave] = tarefa
    return _clonar(tarefa)

def listar_tarefas(status=None):
    """
    Lista as tarefas.
    """
    status_norm = _normalizar_status(status) if status is not None else None
    valores = list(_TASKS.values())
    if status_norm is None:
        return [_clonar(t) for t in valores]
    return [_clonar(t) for t in valores if t["status"] == status_norm]

def obter_tarefa(titulo):
    """Obtém uma tarefa pelo título"""
    chave = _chave(titulo)
    t = _TASKS.get(chave)
    return _clonar(t) if t else None

def concluir_tarefa(titulo):
    """
    Marca a tarefa como concluída.
    """
    chave = _chave(titulo)
    t = _TASKS.get(chave)
    if not t:
        raise ValueError("Tarefa não encontrada.")
    if t["status"] == STATUS_CONCLUIDA:
        raise ValueError("Tarefa já está concluída.")
    t["status"] = STATUS_CONCLUIDA
    return _clonar(t)

def remover_tarefa(titulo):
    """Remove a tarefa."""
    chave = _chave(titulo)
    if chave not in _TASKS:
        raise ValueError("Tarefa não encontrada.")
    del _TASKS[chave]
    return True

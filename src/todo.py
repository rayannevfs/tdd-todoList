_TASKS = {}
STATUS_PENDENTE = "pendente"

def _normalizar_titulo(titulo):
    if not isinstance(titulo, str):
        return ""
    return titulo.strip()

def _chave(titulo):
    return _normalizar_titulo(titulo).casefold()

def _clonar(tarefa_dict):
    return dict(tarefa_dict)

def criar_tarefa(titulo, descricao):
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


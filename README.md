# Projeto TDD To-Do List

**a. Qual projeto foi escolhido:**
- To-Do List

**b. Ferramenta de teste utilizada**
- Python - PyTest

**c. Como executar os testes**
### Requisitos
- Python 3.8+  
- `pip` e `venv` habilitados
- Dependências listadas em `requirements.txt`

### Estrutura
```plaintext
tdd-todoList/
├── src
|   └── todo.py      # código do app
|   └── test_todo.py # testes em Pytest
├── README
├── requirements.txt
```

### Como executar
```plaintext
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt

├── Como executar os testes
pytest -q
# ou
python -m pytest -q
```


**d. Como foi sua experiência utilizando TDD**
- No início foi meio estranho, travou um pouco meu fluxo de pensamento, mas posteriormente percebi que o código saiu mais limpo e com mais segurança.
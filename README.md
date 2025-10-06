# **Objetivo**
**Criar uma Function HTTP em Python que lê JSON do GitHub, transforma com pandas e exibe HTML no navegador.**

## **Pré-requisitos**
- **Azure Functions Core Tools v4**
- **Python 3.12+**
- **VS Code com extensões: Python e Azure Functions**
- **pip instalado**

## ** Criar projeto*
Caminho exemplo:
```bash
cd /mnt/c/Users/tavar/Documents/github/json-manipulation-with-pandas-func
func init . --python
```

## **Dependências**
Edite requirements.txt e deixe:
```bash
azure-functions
pandas
requests
```

## **Criar template de função HTTP**
```bash
func new --name PandasManipulationFunc --template "HTTP trigger"
Auth level: ANONYMOUS
```

Estrutura final esperada:
```bash
.
├── .gitignore
├── .vscode/extensions.json
├── data.json (apenas para referência local)
├── function_app.py
├── function_app test.py
├── host.json
├── local.settings.json
└── requirements.txt
```

## **Executar local**
```bash
func start
```

Abra: http://localhost:7071/api/PandasManipulationFunc

## **Resultado esperado: tabela HTML com os dados processados.**
<img width="496" height="279" alt="image" src="https://github.com/user-attachments/assets/810b2f35-6a73-49d5-9bcd-fd8785746145" />





## **Erros comuns e correção**
– ValueError/JSON vazio: não use req.get_json(); esta função busca do GitHub.
– ModuleNotFoundError: rode pip install -r requirements.txt.
– Breakpoint não ativa: execute com F5 no modo “Azure Functions (Python)”, não “Python File”.
– 400 ao buscar JSON: verifique URL raw do GitHub e conectividade; inclua requests no requirements.txt.

# Template de API - Flask

Documentação técnica completa para configuração e execução do template de projeto API utilizando Flask.

## 📋 Índice

- [Visão Geral](#visão-geral)
- [Pré-requisitos](#pré-requisitos)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Funciona o Copier](#como-funciona-o-copier)
- [Criando um Novo Projeto a Partir do Template](#criando-um-novo-projeto-a-partir-do-template)
- [Pre-Commit](#pre-commit)
- [Instalação e Configuração](#instalação-e-configuração)

## 🎯 Visão Geral

Este é um template de projeto API desenvolvido em Python utilizando o framework Flask. O projeto segue uma arquitetura MVC (Model-View-Controller) e inclui suporte para banco de dados, gerenciamento de sessões, serviços e templates HTML.

Este template utiliza o **Copier** para gerar novos projetos de forma automatizada, permitindo personalização através de perguntas interativas durante o processo de criação.

## 🔧 Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:

- **Python 3.9.6 ou superior** - [Download Python](https://www.python.org/downloads/)
- **Git** - [Download Git](https://git-scm.com/downloads)
- **UV** - Gerenciador de pacotes Python moderno - [Instalação UV](https://github.com/astral-sh/uv)
- **Copier** - Ferramenta para gerar projetos a partir de templates - [Instalação Copier](https://copier.readthedocs.io/en/stable/#installation)
- **Banco de Dados** (Opcional, se necessário) - Configurado conforme suas necessidades

### Verificando as Instalações

Abra um terminal e execute:

```bash
# Verificar versão do Python
python --version
# ou
python3 --version

# Verificar versão do Git
git --version

# Verificar se o UV está instalado
uv --version

# Verificar se o Copier está instalado
copier --version
```

### Instalando o Copier

Se o Copier não estiver instalado, você pode instalá-lo usando:

```bash
# Usando pip
pip install copier

# Ou usando pipx (recomendado)
pipx install copier

# Ou usando uv
uv pip install copier
```

## 📁 Estrutura do Projeto

```
apitemplate/
│
├── App/                        # Módulo principal da aplicação
│   ├── Controllers/            # Controladores (lógica de rotas)
│   │   └── {{module_name}}Controller.py.jinja  # Template do controlador
│   ├── Database/               # Configurações de banco de dados
│   │   └── Session.py          # Gerenciamento de sessões SQLAlchemy
│   ├── Models/                 # Modelos de dados (ORM)
│   │   └── _ORM.py             # Configuração base do ORM
│   ├── Services/               # Camada de serviços (regras de negócio)
│   │   └── Service.py          # Classe base para serviços
│   ├── Template/               # Templates HTML (Jinja2)
│   │   └── index.html.jinja    # Template da página inicial
│   └── Utils/                  # Utilitários
│       └── Logger.py           # Configuração de logging
│
├── app.py                      # Arquivo principal de entrada
├── copier.yaml                 # Configuração do Copier
├── pyproject.toml              # Configurações do projeto e Ruff
├── .pre-commit-config.yaml     # Configuração dos pre-commit hooks
├── .gitignore                  # Arquivos ignorados pelo Git
└── README.md                   # Este arquivo
```

## 🔄 Como Funciona o Copier

O **Copier** é uma ferramenta que permite criar projetos a partir de templates de forma automatizada. Ele funciona através de:

1. **Templates Jinja2**: Os arquivos do template contêm variáveis que serão substituídas durante a criação do projeto (ex: `{{module_name}}`, `{{project_name}}`)

2. **Arquivo de Configuração (`copier.yaml`)**: Define as perguntas que serão feitas ao usuário e as validações para as respostas

3. **Processo de Criação**: O Copier pergunta ao usuário sobre as variáveis definidas, valida as respostas e substitui os placeholders nos arquivos

4. **Arquivo de Respostas (`.copier-answers.yaml`)**: Salva as respostas fornecidas para futuras atualizações do template

### Variáveis do Template

Este template utiliza as seguintes variáveis configuráveis:

- **`project_name`**: Nome do projeto (4-40 caracteres, minúsculas, pode conter hífens)
- **`module_name`**: Nome do módulo Python (4-40 caracteres, minúsculas, pode conter underscores)
- **`formatted_name`**: Nome formatado legível (gerado automaticamente a partir do `project_name`)
- **`mongodb_log_name`**: ID do projeto no MongoDB (gerado automaticamente)
- **`python_version`**: Versão do Python a ser utilizada (padrão: 3.9.6)
- **`use_precommit`**: Se deve configurar o pre-commit (padrão: true)

## 🚀 Criando um Novo Projeto a Partir do Template

Para criar um novo projeto usando este template, siga os passos abaixo:

### Passo 1: Instalar o Copier (se ainda não tiver)

```bash
py -m pip install copier
# ou
py -m pipx install copier
```

### Passo 2: Criar o Novo Projeto

Execute o comando Copier apontando para este repositório:

```bash
py -m copier copy <caminho-para-este-template> <caminho-do-novo-projeto>
```

**Exemplos:**

```bash
# Se o template estiver em um repositório Git remoto
py -m copier copy https://github.com/usuario/apitemplate_trust.git meu-novo-projeto

# Se o template estiver em um diretório local
py -m copier copy ./apitemplate_trust meu-novo-projeto

# Ou se você estiver dentro do diretório do template
py -m copier copy . ../meu-novo-projeto
```

### Passo 3: Responder às Perguntas

O Copier fará perguntas interativas sobre o projeto. Responda conforme necessário:

```
? Qual o nome do projeto? meu-projeto-api
? Qual o nome do módulo python? meu_projeto_api
? Qual o nome formatado (Legível)? Meu Projeto Api
? QUal o id do projeto no MONGODB? MeuProjetoApi
? Selecione a versão do python [3.9.6]: 3.9.6
? Usar pre-commit? (Y/n) [Y/n]: Y
```

### Passo 4: Tarefas Automáticas

Após responder às perguntas, o Copier executará automaticamente as tarefas definidas em `copier.yaml`:

1. Copiar o arquivo `.env.example` para `.env`
2. Criar o ambiente virtual usando UV
3. Sincronizar as dependências com UV

### Passo 5: Navegar para o Novo Projeto

```bash
cd meu-novo-projeto
```

### Atualizando um Projeto Existente

Se você já criou um projeto a partir deste template e quer atualizá-lo com as mudanças do template:

```bash
cd meu-projeto-existente
copier update
```

O Copier usará o arquivo `.copier-answers.yaml` para manter as respostas anteriores e aplicar apenas as atualizações.

## 🔒 Pre-Commit

O **Pre-Commit** é uma ferramenta que executa hooks (ganchos) automaticamente antes de cada commit no Git. Isso garante que o código siga padrões de qualidade antes de ser versionado.

### Como Funciona

O pre-commit funciona através de hooks que são executados automaticamente quando você tenta fazer um commit. Se algum hook falhar, o commit é bloqueado até que os problemas sejam corrigidos.

### Hooks Configurados

Este projeto utiliza os seguintes hooks (definidos em `.pre-commit-config.yaml`):

1. **`ruff-check`**: Verifica e corrige automaticamente problemas de linting no código Python
2. **`ruff-format`**: Formata o código Python seguindo o estilo definido no `pyproject.toml`

Ambos os hooks utilizam o **Ruff**, um linter e formatador Python extremamente rápido.

### Instalando o Pre-Commit

Após criar o projeto com o Copier, instale os hooks do pre-commit:

```bash
# Ativar o ambiente virtual (se ainda não estiver ativo)
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate

# Instalar os hooks do pre-commit
pre-commit install
```

### Como Usar o Pre-Commit

#### Uso Automático

Após instalar os hooks, o pre-commit será executado automaticamente a cada tentativa de commit:

```bash
git add .
git commit -m "Minha mensagem de commit"
```

Se houver problemas de formatação ou linting, o pre-commit irá:
1. Corrigir automaticamente os problemas que puder
2. Bloquear o commit se houver problemas que não podem ser corrigidos automaticamente
3. Mostrar mensagens de erro indicando o que precisa ser corrigido manualmente

**Exemplo de saída:**

```
ruff-check.................................................................Passed
ruff-format................................................................Passed
[main abc1234] Minha mensagem de commit
```

Se houver problemas:

```
ruff-check.................................................................Failed
- hook id: ruff-check
- files were modified by this hook

ruff-format................................................................Passed
```

Neste caso, os arquivos foram corrigidos automaticamente. Você precisa adicionar as correções e tentar o commit novamente:

```bash
git add .
git commit -m "Minha mensagem de commit"
```

#### Executando Manualmente

Você também pode executar o pre-commit manualmente em todos os arquivos:

```bash
# Executar em todos os arquivos
pre-commit run --all-files

# Executar apenas um hook específico
pre-commit run ruff-check --all-files
pre-commit run ruff-format --all-files
```

#### Pulando os Hooks (Não Recomendado)

Se por algum motivo você precisar pular os hooks do pre-commit (não recomendado):

```bash
git commit --no-verify -m "Mensagem"
```

⚠️ **Atenção**: Use `--no-verify` apenas em situações excepcionais, pois isso pode comprometer a qualidade do código.

### Configuração do Ruff

As regras de linting e formatação são configuradas no arquivo `pyproject.toml`. O Ruff verifica:

- **Erros de estilo** (E, W): Conformidade com PEP 8
- **Problemas de código** (F): Detecção de erros comuns
- **Atualizações de sintaxe** (UP): Sugestões de modernização
- **Bugs potenciais** (B): Detecção de problemas comuns
- **Compreensões** (C4): Otimização de list/dict comprehensions
- **Ordenação de imports** (I): Organização automática de imports
- **Nomenclatura** (N): Conformidade com PEP 8 naming
- **Documentação** (D): Verificação de docstrings
- **Segurança** (S): Detecção de vulnerabilidades
- **Prints** (T20): Detecção de prints esquecidos

## 🛠️ Instalação e Configuração

### Passo 1: Ativar o Ambiente Virtual

O ambiente virtual já foi criado automaticamente pelo Copier. Ative-o:

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

Após ativar, você verá `(.venv)` no início da linha do terminal.

### Passo 2: Verificar as Dependências

As dependências já foram instaladas automaticamente pelo Copier. Se precisar reinstalar:

```bash
uv sync
```

### Passo 3: Configurar Variáveis de Ambiente

Edite o arquivo `.env` com as configurações do seu projeto:

```bash
# Copiar o exemplo (já foi feito automaticamente)
# cp .env.example .env

# Editar o arquivo .env com suas configurações
```

### Passo 4: Instalar os Hooks do Pre-Commit

```bash
pre-commit install
```

### Passo 5: Executar a Aplicação

```bash
python app.py
```

A aplicação estará disponível na porta configurada no arquivo `.env` (variável `APP_PORT`).

## 📝 Notas Importantes

- O arquivo `.copier-answers.yaml` contém as respostas fornecidas durante a criação do projeto. Não o exclua, pois ele é necessário para atualizações futuras do template.

- Se algum arquivo estiver com problemas de formatação ou sintaxe durante o commit, o pre-commit tentará corrigir automaticamente. Basta adicionar as correções e tentar o commit novamente.

- Para atualizar o projeto com as mudanças do template, use `copier update` dentro do diretório do projeto.


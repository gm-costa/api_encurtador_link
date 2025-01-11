# API - Encurtador de Links

> Projeto desenvolvido na [PSW 12](https://pythonando.com.br "Pythonando").

## Objetivo

    Encurtar links através de uma API.

## Sumário

- <a href='#pré-requesitos'>Pré-requisitos</a>
- <a href='#funcionalidades'>Funcionalidades</a>
- <a href='#como-executar-o-projeto'>Como executar o projeto</a>

### Pré-requisitos

    Django, django-ninja, pillow, qrcode e python-decouple.

### Funcionalidades

- Cadastrar novos links
- Atualizar os links
- Redirecionamento automático
- Estatísticas
- Gerar QRCode

### Como executar o projeto

```bash
# Clone o projeto
git clone https://github.com/gm-costa/diario.git

# A partir daqui vou usar o comando 'python3', pois uso linux, quem for 
# usar no windows, pode substituir por 'python' ou somente 'py'

# Crie o ambiente virtual
python3 -m venv venv

# Ative o ambiente
    # No Linux
        source venv/bin/activate
    # No Windows
        venv\Scripts\Activate

# Instale as bibliotecas
pip install -r requirements.txt

# Crie o arquivo .env
python3 gerar_env_file.py

# Execute as migrações
python3 manage.py makemigrations && python3 manage.py migrate

# Crie o super usuário (opcional)
python3 manage.py createsuperuser

# Execute o servidor
python3 manage.py runserver

# Teste o projeto, em um browser digite
http://127.0.0.1:8000

```

---

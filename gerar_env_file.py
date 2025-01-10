"""
Gera arquivo .env com SECRET_KEY
"""
from string import ascii_letters, digits, punctuation
from secrets import choice


def gerar_env():
    text = ascii_letters + digits + punctuation
    secret_key = ''.join(choice(text) for i in range(66))

    content_file = f'SECRET_KEY={secret_key}\nDEBUG=True'

    with open('.env', 'w') as env_file:
        env_file.write(content_file)


if __name__ == '__main__':
    gerar_env()

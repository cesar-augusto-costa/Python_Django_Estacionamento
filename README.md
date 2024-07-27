![Green Retro Vintage Oak Tree Logo (Capa para Facebook) (1640 × 200 px)](markedown/img/capa_face.png)
# Projeto desenvolvido no curso do Senai<br><br>Python com Framework.

## Ferramentas utilizadas

:heavy_check_mark: <b>Python</b><br>
Linguagem de programação.<br>

:heavy_check_mark: <b>Django</b><br>
Framework de Python para renderização de páginas web.<br>

---

<b>Este projeto foi elaborado por:</b>

| Perfil | Nome e Email | Localização | Github | Linkedin |
| ---------------- | ----- | --------- | --------- | --------- |
| <img width="100" alt="Foto de Perfil do GitHub do Cesar" src="https://avatars.githubusercontent.com/u/100310865"> | `Cesar Augusto da Costa`<br><br>cesar.costa.cac.1993@gmail.com | Campinas - SP | <a href="https://github.com/cesar-augusto-costa"> <img height="30" alt="GitHub do Cesar" src="https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white"></a> | [![Github Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/cesar-augusto-costa/) |

## **Como Contribuir Com o GIT**

* [Guia de Principais Funções dos Comandos](markedown/principais_comandos_git.md)
* [Resolver Problema de Credenciais no GitHub](markedown/erro_credenciais_git.md)

## Como utilizar o Projeto

### 1 - Pré-requisitos

O projeto foi desenvolvido dentro do VSCode<br>

- Instalar o VSCode.

- Instalar o Python no Windows / Linux / MacOS.

- Instalar a extensão do Python dentro do VSCode.

- Selecionar Interpretador Python e não o Anaconda.

### 2 - Baixar o arquivo do GitHub e Abrir a pasta com VS Code

```
git clone https://github.com/cesar-augusto-costa/django_senai.git
```

### 3 - Alteração da Política de Execução, caso der erro na criação do venv.

- Executar o `Windows PowerShell` no modo *Administrador* com o botão direito do mouse.

- Executar o comando:
```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
- Aceitar a alteração: S

### 4 - Criar o Ambiente Virtual e Instalar Dependências pelo Terminal

- Criar o Ambiente Virtual no Windows
```
python -m venv venv
```

- Criar o Ambiente Virtual no Linux
```
python3 -m venv venv
```

- Ativar venv no Windows
```
.\venv\Scripts\activate
```

- Ativar venv no Linux
```
source venv/bin/activate
```

- Atualize a versão do pip
```
python -m pip install --upgrade pip
```

- Instalar todos os pacotes necessários (dependências)
```
pip install -r requirements.txt
```

- Como gerar o requirements.txt
```
pip freeze > requirements.txt
```

### 5 - Visualizar o Projeto

- Rodar o servidor

```
python manage.py runserver
```

- Clicar em cima do endereço HTTP com CTRL.

- Para parar o servidor use CTRL + C no Terminal




# Microblog API  
Esta é uma API de microblog desenvolvida com Python e Django, que oferece funcionalidades como registro de usuários, seguir outros usuários, criar posts, curtir e comentar posts, além de exibir um feed.

# 🛠️ Funcionalidades  
Login e Registro de usuários.  
Seguir usuários.  
Criar, curtir e comentar posts.  
Feed: exibe posts dos usuários que você segue.  

🚀 Tecnologias utilizadas  
Python  
Django
Django REST Framework  
SQLite (ou outro banco de dados configurado)  
Postman (para documentação e testes)  

📋 Pré-requisitos  
Python instalado.  
Git para clonar o repositório. 

🛑 Como rodar o projeto
1. Clone o repositório  
git clone https://github.com/seu-usuario/microblog-api.git  
cd microblog-api

2. Configure o ambiente virtual  
python -m venv venv  
source venv/bin/activate  # No Windows: venv\Scripts\activate

3. Instale as dependências  
pip install -r requirements.txt

4. Realize as migrações do banco de dados  
python manage.py migrate

5. Crie um superusuário  
python manage.py createsuperuser

6. Inicie o servidor  
python manage.py runserver

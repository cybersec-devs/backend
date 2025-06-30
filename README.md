# 🏥 Sistema de Hospital - BACKEND - Projeto Prático  

## Integrantes

- Enrico Carrano  
- Glauber Ariel Magalhães  
- Gregorio Queiroz  
- Eduardo Silva  
- Welther Moraes  

---

## ✅ Requisitos Funcionais (RF)

- **RF001** - Permitir o cadastro de médicos com nome, especialidade e CRM.  
- **RF002** - Permitir o cadastro de pacientes vinculados a um médico.  
- **RF003** - Permitir o cadastro de consultas vinculadas a um paciente, informando data, horário e descrição.  
- **RF004** - Listar todos os médicos cadastrados.  
- **RF005** - Listar todos os pacientes de um médico específico.  
- **RF006** - Listar todas as consultas de um paciente específico.  
- **RF007** - Permitir atualizar os dados de médicos, pacientes e consultas.  
- **RF008** - Permitir excluir médicos, pacientes e consultas.  

---

## ✅ Requisitos Não Funcionais (RNF)

- **RNF001** - Utilizar arquitetura RESTful.  
- **RNF002** - Utilizar banco de dados relacional (ex: PostgreSQL, MySQL, SQLite).  
- **RNF003** - Garantir integridade referencial entre médicos, pacientes e consultas.  
- **RNF004** - Respostas da API em formato JSON.  

---

## ✅ Diagrama de Classes

![Diagrama UML](Classe%20UML.png)

**Relacionamentos:**

- **Médico 1:N Paciente** (um médico pode ter vários pacientes)  
- **Paciente 1:N Consulta** (um paciente pode ter várias consultas)  

---

## 🚀 Como executar o projeto

### 1. Pré-requisitos

- Python 3.8+ instalado  
- Git instalado (opcional)  

### 2. Clone o repositório (se ainda não clonou)

```bash
git clone https://github.com/cybersec-devs/backend.git
cd seu-repositorio/backend/api
```

### 3. Crie e ative o ambiente virtual
#### No Linux/macOS:  
```bash
python3 -m venv venv  
source venv/bin/activate  
pip install --upgrade pip
```

#### No Windows (PowerShell):  
```bash
python -m venv venv  
.\venv\Scripts\Activate.ps1  
python -m pip install --upgrade pip
```
#### No Windows (cmd):   

```bash
python -m venv venv  
venv\Scripts\activate.bat  
python -m pip install --upgrade pip
```

### 4. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 5. Rodar o servidor Flask
```bash
python api/app.py  
```

O servidor estará rodando em http://127.0.0.1:5000/

### 📋 Documentação da API - Swagger
Com o servidor rodando, acesse a documentação interativa via Swagger UI em: http://127.0.0.1:5000/

Lá você poderá testar todos os endpoints do sistema (médicos, pacientes, consultas), ver modelos de dados, parâmetros e respostas.


#### Considerações finais
Para criar as tabelas, o sistema usa db.create_all() na inicialização do app.

Em caso de dúvidas, verifique os logs no terminal onde o Flask está rodando.

---

#### Tecnologias Utilizadas
- Python + Flask + SQLAlchemy
- Swagger (Flask-RESTX)

---

**Atenção - Visitar o Projeto em Produção**: 

- Aplicação Backend está disponível em: <https://hospital-backend-yeq5.onrender.com/>
- Aplicação FrontEnd está disponível em: <https://cybersec-devs.github.io/frontend/>


Caso queira executar na sua própria máquina, siga as orientações deste documento.
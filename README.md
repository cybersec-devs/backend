🏥 Sistema de Hospital - Projeto prático

Integrantes:

Enrico Carrano
Glauber Ariel Magalhães
Gregorio Queiroz
Eduardo Silva
Welther Moraes

## ✅ Requisitos Funcionais (RF)

- **RF001** - O sistema deve permitir o cadastro de médicos com nome, especialidade e CRM.
- **RF002** - O sistema deve permitir o cadastro de pacientes vinculados a um médico.
- **RF003** - O sistema deve permitir o cadastro de consultas vinculadas a um paciente, informando data, horário e descrição.
- **RF004** - O sistema deve listar todos os médicos cadastrados.
- **RF005** - O sistema deve listar todos os pacientes de um médico específico.
- **RF006** - O sistema deve listar todas as consultas de um paciente específico.
- **RF007** - O sistema deve permitir atualizar os dados de médicos, pacientes e consultas.
- **RF008** - O sistema deve permitir excluir médicos, pacientes e consultas.

---

## ✅ Requisitos Não Funcionais (RNF)

- **RNF001** - O sistema deve ser desenvolvido utilizando a arquitetura RESTful.
- **RNF002** - O sistema deve utilizar um banco de dados relacional (ex: PostgreSQL, MySQL).
- **RNF003** - O sistema deve garantir integridade referencial entre médicos, pacientes e consultas.
- **RNF004** - O sistema deve ter respostas em formato JSON.

---

## ✅ Diagrama de Classes

![Texto alternativo](Classe%20UML.png)

**Relacionamentos:**

- **Médico 1:N Paciente** (um médico pode ter vários pacientes)
- **Paciente 1:N Consulta** (um paciente pode ter várias consultas)


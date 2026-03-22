# 🐓🤖 Sistema de gestão - Cantina FATEC 2026
Projeto Cantina Atlética

Este repositório contém o desenvolvimento do projeto prático para as disciplinas de **Linguagem de programação 2** e **estrutura de dados**. O objetivo é gerenciar o estoque e as vendas de uma cantina utilizando conceitos de POO (Programação Orientada a Objetos) e Estruturas de Dados Dinâmicas.

## ⚙️ Configuração do ambiente

Este projeto utiliza um **ambiente virtual (venv)** para isolar as dependências e garantir que o sistema rode com as versões corretas das bibliotecas.

### Como configurar o ambiente de desenvolvimento:

1. **Clone o repositório e abra o terminal na pasta do projeto.**
2. **Ative o ambiente virtual:**
   - **No Windows (PowerShell):** `.\venv\Scripts\Activate.ps1`
   - **No Windows (CMD):** `.\venv\Scripts\activate.bat`
   - **No Linux/macOS:** `source venv/bin/activate`
3. **Instale as dependências:**
   - `pip install -r requirements.txt`

### Como rodar o projeto:
- Certifique-se de que o venv está ativo e execute: `python sistemacantina.py`

## 🛠️ Funcionalidades atuais

### 🔐 Painel administrativo
- Sistema de login com validação de senha (`atletica26`).
- Proteção contra erros de digitação e caracteres inválidos.

### 🛒 Painel de compras
- Identificação de clientes por **Nome**, **Categoria** (Aluno, Servidor, Professor) e **Curso** (IA ou ESG).
- **Validação de dados:** Implementação de `try-except` para capturar `ValueError`, garantindo que o sistema não encerre ao receber letras em campos numéricos ou números decimais.
- **Fluxo inteligente:** A pergunta sobre o "Curso" é exibida exclusivamente para usuários da categoria "Aluno".

### 📦 Gestão de Estoque
- **Modelagem de lotes:** Cadastro completo contendo Nome, Preço de Compra/Venda, Quantidade e Datas (Compra/Vencimento).
- **Lógica FIFO (First-In, First-Out):** Estrutura preparada para priorizar a venda dos itens mais velhos.
- **Edição dinâmica:** Inplementação de método para o Administrador realizar o ajuste manual de quantidades em estoque.

## 📚 Tecnologias e conceitos aplicados
- **Linguagem:** Python
- **Tratamento de exceções:** Uso de `try`, `except`, `continue` e `break` para controle de fluxo robusto.
- **Modularização e Encapsulamento:** Organização do sistema em múltiplos arquivos (`.py`) para separação de responsabilidades entre as classes (Sistema, Usuário, Produto e Estoque).
- **Estruturas de dados dinâmicas:** Uso de listas para armazenamento e manipulação de objetos complexos em tempo de execução.
- **Tipagem de dados:** Conversão explícita para `float` e `int`, assegurando a integridade de cálculos financeiros e contagem de itens.
- **Controle de versão:** GitHub com commits incrementais e organizados.

---
*Status do projeto: Em desenvolvimento (identificação de usuários e gestão de estoque concluídas).*
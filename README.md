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

## 📚 Tecnologias e conceitos aplicados
- **Linguagem:** Python
- **Tratamento de exceções:** Uso de `try`, `except`, `continue` e `break` para controle de fluxo robusto.
- **Controle de versão:** GitHub com commits incrementais e organizados.

---
*Status do projeto: Em desenvolvimento (identificação de usuários concluída).*
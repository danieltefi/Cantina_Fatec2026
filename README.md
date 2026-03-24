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

### 🔐 Painel Administrativo
- **Autenticação Segura:** Sistema de login com validação de senha (`atletica26`) e uso de atributos privados (Encapsulamento).
- **Interface de gestão:** Menu interno que permite ao administrador navegar entre as funções de estoque sem necessidade de reautenticação.
- **Proteção contra erros:** Uso de `try-except` para garantir que a navegação no menu não quebre com entradas inválidas.
- **Automação de Preços:** Cálculo automático de margem de lucro (40%) para preço de venda.

### 🛒 Painel de Compras
- **Identificação de clientes:** Coleta de dados por **Nome**, **Categoria** (Aluno, Servidor, Professor) e **Curso** (IA ou ESG).
- **Validação de dados:** Implementação de `try-except` para capturar `ValueError`, garantindo que o sistema não encerre ao receber letras em campos numéricos ou números decimais.
- **Fluxo inteligente:** A pergunta sobre o "Curso" é exibida exclusivamente para usuários da categoria "Aluno".
- **Vitrine de produtos:** Visualização dos produtos cadastrados no estoque.
- **Busca por produto:** Lógica de busca que valida se o produto escolhido existe e se possui quantidade disponível para venda.

### 📦 Gestão de Estoque
- **Cadastro de produtos:** Cadastro contendo Nome, Preço de compra/venda, Quantidade e Datas (Compra/Vencimento).
- **Lógica FIFO (First-In, First-Out):** Estrutura que prioriza a venda dos itens mais velhos (primeiros comprados).
- **Edição de produtos:** Implementação de método para o Administrador realizar o ajuste manual de quantidades em estoque.

### 💸 Controle de pagamento (PIX)
- **Registro de vendas:** Captura de Nome, Categoria, Curso, Valor e Produto no momento da confirmação do PIX.
- **Baixa automática:** Integração entre os módulos de Pagamento e Estoque, subtraindo a unidade vendida.
- **Relatório de vendas:** Interface para o Administrador visualizar o histórico completo de transações realizadas.

## 📚 Tecnologias e conceitos aplicados
- **Linguagem:** Python
- **Tratamento de exceções:** Uso de `try`, `except`, `continue` e `break` para controle de fluxo robusto.
- **Modularização e Encapsulamento:** Organização do sistema em múltiplos arquivos, uso de atributos privados e métodos de acesso (Getters/Setters).
- **Estruturas de dados dinâmicas:** Uso de listas para armazenamento e manipulação de objetos complexos em tempo de execução.
- **Tipagem de dados:** Conversão explícita para `float` e `int`, assegurando a integridade de cálculos financeiros e contagem de itens.
- **Data e hora de transação:** Uso da biblioteca `datetime` para registrar data e hora exatas de cada venda.
- **Controle de versão:** GitHub com commits incrementais e organizados.

---
*Status do projeto: Em desenvolvimento (Identificação de usuários, gestão de estoque, vendas e relatórios financeiros concluídas).*
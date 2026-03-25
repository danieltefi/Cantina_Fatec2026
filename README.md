# 🐓🤖 Sistema de gestão - Cantina FATEC 2026

Projeto prático para as disciplinas de **Linguagem de Programação 2** e **Estrutura de Dados**. 
O sistema foca em Programação Orientada a Objetos e estruturas dinâmicas para gestão de estoque e vendas.

## ⚙️ Configuração do ambiente
O projeto utiliza **ambiente virtual (venv)** para isolamento de dependências.

### Instalação:
1. **Ative o ambiente:**
   - Windows (PowerShell): `.\venv\Scripts\Activate.ps1`
   - Windows (CMD): `.\venv\Scripts\activate.bat`
   - Linux/macOS: `source venv/bin/activate`
2. **Dependências:** `pip install -r requirements.txt` (Necessário para a biblioteca **Faker**).

### Execução:
- Com o venv ativo: `python sistemacantina.py`

## 🛠️ Funcionalidades concluídas

### 🔐 Painel administrativo
- **Autenticação:** Acesso via senha privada com atributos encapsulados.
- **Gestão de margem:** Cálculo automático de lucro sobre o preço de compra.
- **Persistência:** Carregamento e salvamento automático de dados via **Pickle**.

### 🛒 Painel de compras
- **Triagem de usuários:** Coleta de Nome, Categoria (Aluno, Servidor, Professor) e Curso (IA/ESG).
- **Carrinho dinâmico:** Seleção de múltiplos itens com validação de estoque em tempo real.
- **Simulação de venda:** Fluxo de checkout integrado para confirmação de pagamento via PIX.

### 📦 Gestão de estoque
- **FIFO (First-In, First-Out):** Estrutura que prioriza a saída de itens mais antigos.
- **Controle manual:** Permite ao administrador editar quantidades diretamente no estoque.

### 💸 Relatórios e consumo
- **Baixa automática:** Sincronização entre venda e estoque por unidade consumida.
- **Histórico completo:** Relatório detalhado de consumo, incluindo data e hora exata.

## 📚 Tecnologias e conceitos
- **Linguagem:** Python 3.
- **Estruturas próprias:** Implementação de fila e lista encapsuladas, evitando o uso direto de built-ins.
- **Persistência de dados:** Armazenamento não volátil em arquivos binários (`.dat`) com **Pickle**.
- **Tratamento de erros:** Blocos `try-except` para validar entradas e formatação de preços.
- **Modularização:** Divisão do sistema em múltiplos arquivos para separação de responsabilidades.

---
*Status do projeto: **Concluído** (Requisitos de estoque, vendas, relatórios e persistência de dados).*
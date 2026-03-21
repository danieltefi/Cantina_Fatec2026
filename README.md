# 🐓🤖 Sistema de gestão - Cantina FATEC 2026
Projeto Cantina Atlética

Este repositório contém o desenvolvimento do projeto prático para as disciplinas de **Linguagem de programação 2** e **estrutura de dados**. O objetivo é gerenciar o estoque e as vendas de uma cantina utilizando conceitos de POO (Programação Orientada a Objetos) e Estruturas de Dados Dinâmicas.

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
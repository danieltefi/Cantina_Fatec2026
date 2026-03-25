# 📋 Controle de Requisitos - Cantina FATEC 2026

## ✅ Requisitos Funcionais
- [x] **Controle de estoque:**
    - [x] Armazenar: Nome, Preço de Compra, Preço de Venda, Data de Compra, Data de Vencimento e Quantidade.
    - [x] Lógica FIFO: Priorizar a venda dos produtos mais velhos.
    - [x] Edição: Permitir ajuste manual da quantidade em estoque.
- [x] **Controle de pagamento (PIX):**
    - [x] Registrar: Nome do pagador, Categoria (Aluno, Servidor, Professor), Curso (IA ou ESG), Valor, Data e Hora.
- [x] **Simulação de consumo:**
    - [x] Realizar a baixa automática do estoque no momento da compra.
    - [x] Vincular o registro de pagamento ao consumo e ao produto.
- [x] **Geração e persistência de dados:**
    - [x] Popular o sistema com dados aleatórios usando a biblioteca Faker.
    - [x] Implementar salvamento e carregamento não volátil via pickle.
- [x] **Relatórios:**
    - [x] Criar relatórios de vendas e relatórios de consumo.

## 🛠️ Requisitos Técnicos
- [x] **POO e Classes:** Criar classes próprias para implementar as estruturas de cada problema.
- [x] **Encapsulamento:** Usar o encapsulamento internamente nas estruturas criadas (atributos privados).
- [x] **Separação de responsabilidades:** Divisão clara de funções entre as classes.

## ⚠️ Critérios de avaliação e prazos
- [x] **Entregas incrementais:** Realizar commits frequentes no GitHub.
- [ ] **Domínio do código:** Estar apto a explicar as escolhas técnicas na apresentação.
- [ ] **Data Final:** Entrega e apresentação em 26/03/2026.

## 🚫 NÃO fazer
- [x] **NÃO usar bibliotecas built-in de forma direta:** Proibido usar listas, pilhas ou filas do Python para lidar com a lógica do problema fora de classes próprias.
- [x] **NÃO ignorar o Encapsulamento:** Garantir que as estruturas internas não estejam expostas sem proteção.
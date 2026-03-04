# 🖥️ Sistema de Cadastro Automático de Produtos com Python

Automação de processos utilizando **Python + PyAutoGUI** para realizar o cadastro automático de produtos em um sistema web a partir de uma base de dados em CSV.

Este projeto simula um cenário real de automação de tarefas repetitivas, reduzindo tempo operacional e minimizando erros humanos.

---

## 🚀 Sobre o Projeto

O sistema realiza automaticamente:

- Abertura do navegador
- Acesso ao sistema web
- Login automático
- Leitura de uma base de dados (`produtos.csv`)
- Cadastro automático de cada produto no sistema

A automação é feita através do controle do mouse e teclado com a biblioteca **PyAutoGUI**.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **PyAutoGUI** (automação de mouse e teclado)
- **Pandas** (manipulação de dados)
- **Time** (controle de execução)
  
---

## 📊 Estrutura do Arquivo CSV

O sistema espera um arquivo `produtos.csv` com as seguintes colunas:

| codigo | marca | tipo | categoria | preco_unitario | custo | obs |
|--------|-------|------|-----------|----------------|--------|-----|

### Exemplo:

```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
001,Nike,Tênis,Esporte,299.90,150.00,Promoção
002,Adidas,Camiseta,Roupa,99.90,40.00,

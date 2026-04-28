# controle-de-estoque
Um sistema de controle de estoque 

# 📦 Controle de Estoque em Python

## 📖 Descrição do Projeto

Este projeto foi desenvolvido como parte do desafio **Checkpoint 2 - Computational Thinking With Python**.

O objetivo é criar um sistema simples de **controle de estoque**, utilizando conceitos fundamentais da linguagem Python, como:

* Listas
* Estruturas de repetição (loops)
* Funções (métodos)
* Validação de dados

O sistema permite cadastrar produtos, validar informações e organizar os dados, garantindo a integridade das informações.

---

## 🎯 Problema Proposto

O sistema simula um controle de estoque onde:

* Produtos possuem **código, nome e quantidade**
* Produtos com dados inválidos são separados automaticamente
* O sistema mantém uma lista de produtos válidos e outra de erros

---

## ⚙️ Funcionalidades

✔ Cadastrar produtos
✔ Validar código do produto (mínimo de 5 dígitos numéricos)
✔ Validar quantidade (não pode ser negativa)
✔ Armazenar produtos válidos no estoque
✔ Separar produtos inválidos em uma lista de erros
✔ Listar produtos cadastrados
✔ Listar produtos com erro

---

## 🧠 Regras de Validação

### Código do Produto:

* Deve conter apenas números
* Deve ter **no mínimo 5 dígitos**

### Quantidade:

* Deve ser um número inteiro
* Não pode ser negativa

Caso alguma dessas regras não seja atendida, o produto é enviado para a lista de **erros de cadastro**.

---

## 🗂️ Estrutura de Dados

O sistema utiliza listas para armazenar os dados:

* `estoque`: lista de produtos válidos
* `erros`: lista de produtos inválidos

Cada produto é armazenado no formato:

```
[codigo, nome, quantidade]
```

---

## ▶️ Como Executar o Projeto

1. Certifique-se de ter o Python instalado
2. Clone este repositório:

```
git clone https://github.com/seu-usuario/seu-repositorio.git
```

3. Acesse a pasta do projeto:

```
cd seu-repositorio
```

4. Execute o arquivo:

```
python nome_do_arquivo.py
```

---

## 🖥️ Exemplo de Uso

```
1 - Cadastrar produto
2 - Listar estoque
3 - Listar erros
4 - Sair

Escolha uma opção: 1
Digite o código do produto: 123
Digite o nome do produto: Mouse
Digite a quantidade: 10

Produto inválido! Enviado para lista de erros.
```

---

## 📚 Conceitos Aplicados

* Manipulação de listas
* Estruturas de repetição (`for`, `while`)
* Funções em Python
* Validação de dados
* Organização de informações

---


